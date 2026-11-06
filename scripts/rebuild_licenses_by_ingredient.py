"""EU 依成分重建證據包的許可證紀錄（2026-11-06，用戶核准；全程不用 AI；做法比照 Za／Us／Sg）。

原收集器用 EMA 報表「Active substance」欄的原文字串比對（「abacavir」與「abacavir (as sulfate)」各自一組），結果：
- 同一個有效成分的頁只收到一部分 EMA 集中許可（abacavir 頁只有 Ziagen，沒有含 abacavir 的 Kivexa、Triumeq、Trizivir）；
- 許可證表的狀態註記跟 EMA 狀態不一致（Ziagen 是 Authorised，表上寫 cancelled）。

1. 來源：EMA medicines report（https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx，免金鑰；
   與 scripts/license_adapter.py 每週更新用的是同一個檔）。表頭列含「EMA product number」（前面有說明列，自動找表頭）。
   重建前重新下載，存 data/raw/ema_medicines_report.xlsx（--skip-download 用已存的檔）。
2. 只收人用（Category＝Human；獸用 EMEA/V/C 不算人用藥許可，比照 license_adapter.EXCLUDE_VET）。
   從未取得許可的申請不收：Refused、Application withdrawn、Opinion（意見已出、執委會尚未決定）、Withdrawn from rolling review。
   其餘照 EMA「Medicine status」原文寫進 status：Authorised＝有效；Withdrawn／Lapsed／Expired／Revoked／Suspended…＝註銷（reviewer 依文字判定）。
3. 比對：Active substance 以「;」分隔多個成分；成分名拿掉括號內容（「(as sulfate)」「(as amlodipine besilate)」「(rDNA)」「(18F)」…）、
   鹽類／水合物字樣，得到有效成分（moiety）；頁的 drug.inn 同樣處理。有效成分相同就收（含複方許可，與 Us 的單方頁、Sg 相同）。
   同義名（acetylsalicylic acid＝aspirin、ciclosporin＝cyclosporine、adrenaline＝epinephrine…）與「-ic acid」＝「-ate」鹽視為同一成分。
4. 寫回證據包 tfda：records＝全部比對到的 EMA 集中許可（有效在前、單方在前），total_matches＝筆數（不截斷）；原紀錄整批換掉。
   比對結果是空的、但原紀錄的許可證號仍在 EMA 報表 → 不改這個證據包、列進報告（疑似比對漏掉，要人看）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import io
import json
import re
import sys
import time
from pathlib import Path

import openpyxl
import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
XLSX = RAW / "ema_medicines_report.xlsx"
URL = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"
NEVER = {"refused", "application withdrawn", "opinion", "withdrawn from rolling review", "negative opinion"}

SALT = (r"hydrochloride|dihydrochloride|hydrobromide|besilate|besylate|maleate|mesilate|mesylate|dimesylate|tartrate|bitartrate|fumarate|hemifumarate|"
        r"succinate|citrate|acetate|diacetate|propionate|dipropionate|valerate|phosphate|diphosphate|sulfate|sulphate|hydrogen sulfate|bisulfate|"
        r"hemisulfate|nitrate|lactate|gluconate|palmitate|sodium|disodium|trisodium|potassium|dipotassium|calcium|magnesium|bromide|chloride|iodide|"
        r"tosilate|tosylate|edisilate|pamoate|embonate|stearate|oleate|mandelate|camsilate|xinafoate|furoate|hyclate|trometamol|tromethamine|"
        r"meglumine|olamine|erbumine|benzathine|esilate|isethionate|mononitrate|oxalate|dihydrogen|hydrogen|monosodium|decanoate|enantate|"
        r"cipionate|undecanoate|pivalate|hydroxide|monoethanolamine|methanesulfonate|trifenatate|benzoate|malate|diacid|ditromethamine|diolamine|tetrahydrochloride|carbonate|propanediol|arginine salt|zinc salt|sodium salt|potassium salt")
HYD = (r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|heptahydrate|sesquihydrate|hemihydrate|anhydrous|"
       r"hemiheptahydrate|hemipentahydrate|dimethyl sulfoxide|solvate|ethanolate|crystalline|amorphous")
SALT_RX = re.compile(r"\b(" + SALT + "|" + HYD + r")\b")
HYD_RX = re.compile(r"\b(" + HYD + r")\b")
CANON = [(r"\bacetylsalicylic acid\b", "aspirin"), (r"\bciclosporin\b", "cyclosporine"), (r"\badrenaline\b", "epinephrine"),
         (r"\bnoradrenaline\b", "norepinephrine"), (r"\bcolecalciferol\b", "cholecalciferol"), (r"\bparacetamol\b", "acetaminophen"),
         (r"\bsalbutamol\b", "albuterol"), (r"\bglibenclamide\b", "glyburide"), (r"\blidocaine\b", "lidocaine"), (r"\blignocaine\b", "lidocaine"),
         (r"\bsomatotropin\b", "somatropin"), (r"\bdinoprostone\b", "dinoprostone"), (r"\bl lysine\b", "lysine"), (r"\bl arginine\b", "arginine"),
         (r"\bglyceryl trinitrate\b", "nitroglycerin"),
         # EMA 報表裡的錯字／截斷（2026-11-06 實測）：pseudophedrine（Aerinaze）、voxilaprevi（Vosevi）
         (r"\bpseudophedrine\b", "pseudoephedrine"), (r"\bvoxilaprevi\b", "voxilaprevir")]


def norm(x):
    t = str(x or "").lower().replace("’", "'")
    while re.search(r"\([^()]*\)|\[[^\[\]]*\]", t):
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", " ", t)
    t = re.sub(r"\(.*$", " ", t)  # 沒有收尾的括號
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    t = re.sub(r"\b(as|eq|equivalent to)\b.*$", " ", t).strip()  # 「X as Y」：Y 是鹽類寫法
    t = re.sub(r"^(l|d|dl|\d+)\s+(?=[a-z]{3})", "", t)  # L-alanine、6-mercaptopurine
    for a, b in CANON:
        t = re.sub(a, b, t)
    return " ".join(t.split())


def base(t):
    t = re.sub(r"(?<=[a-z]) (lysine|arginine)$", "", t)  # 鹽類用的胺基酸（aztreonam lysine、ibuprofen lysine）；單獨的 lysine 不動
    s = " ".join(SALT_RX.sub(" ", t).split())
    return s or " ".join(HYD_RX.sub(" ", t).split()) or t  # 整個名字都是鹽類字（sodium chloride…）→ 保留原名


def acid_ate(t):
    out = {t}
    if t.endswith("ic acid"):
        out.add(t[:-7] + "ate")
    elif t.endswith("ate") and " " not in t:
        out.add(t[:-3] + "ic acid")
    return out


def parts(s):
    """成分欄以「;」分隔（胺基酸輸液等少數許可用「,」）"""
    return [p for p in (norm(x) for x in re.split(r"[;,]", str(s or ""))) if len(p) >= 3]


def _get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=180, headers={"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"})
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("不是 xlsx（可能拿到 HTML）")
            return r
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def load_ema(download):
    if download:
        RAW.mkdir(parents=True, exist_ok=True)
        XLSX.write_bytes(_get(URL).content)
    ws = openpyxl.load_workbook(io.BytesIO(XLSX.read_bytes()), read_only=True).active
    rows, hdr = [], None
    for r in ws.iter_rows(values_only=True):
        if hdr is None:
            if r and "EMA product number" in [str(c or "").strip() for c in r]:
                hdr = [str(c or "").strip() for c in r]
            continue
        if any(r):
            rows.append(dict(zip(hdr, r)))
    if not hdr or not {"Category", "EMA product number", "Medicine status", "Active substance", "Name of medicine"} <= set(hdr):
        raise SystemExit(f"EMA 報表欄位改變：{(hdr or [])[:8]}")
    if len(rows) < 2000:
        raise SystemExit(f"EMA 報表只解析出 {len(rows)} 筆，疑似格式改變")
    return rows


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    rows = load_ema("--skip-download" not in argv)
    allids = {str(r.get("EMA product number") or "").strip() for r in rows}
    prods, by_base = {}, {}
    for r in rows:
        lid = str(r.get("EMA product number") or "").strip()
        st = str(r.get("Medicine status") or "").strip()
        if not lid or str(r.get("Category") or "").strip() != "Human" or st.lower() in NEVER:
            continue
        ps = parts(r.get("Active substance")) or parts(r.get("International non-proprietary name (INN) / common name"))
        if not ps:
            continue
        prods[lid] = {"r": r, "n": len(ps), "status": st}
        for p in ps:
            by_base.setdefault(base(p), set()).add((lid, p != base(p)))
    out, held, n_changed, n_found, n_empty = [], [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        ps = parts(inn)
        key = base(ps[0]) if ps else ""
        hit = set()
        if key:
            hit |= {lid for lid, _ in by_base.get(key, set())}
            for v in acid_ate(key) - {key}:  # 「-ic acid」＝「-ate」只認鹽（alendronic acid＝sodium alendronate）
                hit |= {lid for lid, salt in by_base.get(v, set()) if salt}
        old_ids = sorted({str(x.get("license_id") or "").strip() for x in reg.get("records") or []} - {""})
        old_cur = sorted(set(old_ids) & set(prods))
        if not hit and old_cur:
            held.append(page)
            out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old_ids)}\t-\tHELD\t{';'.join(old_cur[:10])}\t")
            continue
        def order(k):
            p = prods[k]
            return (p["status"] != "Authorised", p["n"] > 1, k)
        recs = []
        for lid in sorted(hit, key=order):
            p = prods[lid]; r = p["r"]
            recs.append({"license_id": lid, "brand_name_zh": r.get("Name of medicine") or "", "brand_name_en": r.get("Name of medicine") or "",
                         "ingredients": str(r.get("Active substance") or ""), "indication": str(r.get("Therapeutic indication") or ""),
                         "dosage_form": "", "manufacturer": "", "license_holder": str(r.get("Marketing authorisation developer / applicant / holder") or ""),
                         "approval_date": str(r.get("Marketing authorisation date") or "")[:10], "expiry_date": "", "status": p["status"],
                         "atc_code": str(r.get("ATC code (human)") or ""), "kind": "single" if p["n"] == 1 else "combo",
                         "source": "EMA medicines report (centrally authorised medicines, human)"})
        new = dict(reg, found=bool(recs), records=recs, total_matches=len(recs),
                   rebuilt="2026-11-06 by ingredient (EMA medicines report, human centrally authorised medicines)")
        new_ids = [x["license_id"] for x in recs]
        dropped = sorted(set(old_ids) - set(new_ids))
        out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old_ids)}\t{len(new_ids)}\t{len(dropped)}\t"
                   f"{';'.join(dropped[:15])}{' (not in EMA report: ' + ';'.join(sorted(set(dropped) - allids)) + ')' if set(dropped) - allids else ''}\t"
                   f"{';'.join(sorted(set(new_ids) - set(old_ids))[:15])}")
        n_found += bool(recs)
        n_empty += not recs
        if new != reg:
            n_changed += 1
            b["tfda"] = new
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmatch\told_total_matches\told_records\tnew_records\tdropped\tdropped_ids\tadded_ids\n" + "\n".join(out) + "\n",
                             encoding="utf-8")
    print(f"EMA 人用集中許可 {len(prods)} 筆；改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}、比對落空但原許可證仍在報表而保留 {len(held)}）")
    if held:
        print("保留（要人看）：" + ", ".join(held[:30]))


if __name__ == "__main__":
    main(sys.argv[1:])
