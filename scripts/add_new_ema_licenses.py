#!/usr/bin/env python3
"""補收 EMA 新的集中許可（2026-11-25 第五輪，用戶決定；做法比照 DkTxGNN 第四輪 add_component_licenses.py）。

證據包的許可證紀錄是 2026-11-06 依成分重建的（scripts/rebuild_licenses_by_ingredient.py）；之後每週排程（license_adapter）只更新既有
號碼的狀態，EMA 之後才核准、照同一套規則也對得到的新集中許可（學名藥、生物相似藥、新複方）不會進證據包
（2026-11-24 量測：EMA medicines report 有、證據包沒收的新號 20 筆）。
這支照 rebuild 的同一套比對規則（index／match_ids，含 config/bundle_record_exclusions.json 的排除）重算每個證據包對到的
人用集中許可，證據包裡還沒有的（records、excluded_records、veterinary_records 都沒有）補進 records：
- 只加不刪、不改既有紀錄；每筆另記 source（報表與規則）、added（補收日）；不設筆數上限（同 rebuild），total_matches 同步加。
- 比對落空的證據包（rebuild 會 HELD 的）不動。
每週 license-refresh.yml 在 license_refresh 前以 --download 跑（下載失敗不擋排程）；有補收就照常發新 Release。可重複執行（第二次 0 筆）。
用法（repo 根目錄，先還原 data/）：python3 scripts/add_new_ema_licenses.py [--download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_licenses_by_ingredient as RB  # noqa: E402

SOURCE = "EMA medicines report (centrally authorised medicines, human); matched by ingredient, same rule as the 2026-11-06 rebuild"


def run(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    rows = RB.load_ema("--download" in argv)
    prods, by_base = RB.index(rows)
    today = time.strftime("%Y-%m-%d")
    added, touched, lines = 0, [], []
    for f in sorted(RB.BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        _, hit = RB.match_ids(page, b, prods, by_base)
        if not hit:
            continue
        have = {str(r.get("license_id") or "").strip()
                for k in ("records", "excluded_records", "veterinary_records") for r in (t.get(k) or [])}
        new = sorted(hit - have, key=lambda k: RB.order(prods, k))
        if not new:
            continue
        recs = [dict(RB.make_record(prods, lid), source=SOURCE, added=today) for lid in new]
        for r in recs:
            lines.append(f"{page}\t{r['license_id']}\t{r['brand_name_en']}\t{r['ingredients']}\t{r['status']}\t{r['approval_date']}")
        added += len(recs)
        touched.append(page)
        if dry:
            continue
        allr = (t.get("records") or []) + recs
        st = {r["license_id"]: (str(r.get("status") or "") != "Authorised", r.get("kind") == "combo", r["license_id"]) for r in allr}
        t["records"] = sorted(allr, key=lambda r: st[r["license_id"]])
        t["total_matches"] = int(t.get("total_matches") or 0) + len(recs)
        t["found"] = True
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tlicense_id\tname\tactive_substance\tstatus\tauthorisation_date\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"補收 EMA 新集中許可：{added} 筆（{len(touched)} 個證據包）{'（試跑，沒寫檔）' if dry else ''}")
    return touched


if __name__ == "__main__":
    run(sys.argv[1:])
