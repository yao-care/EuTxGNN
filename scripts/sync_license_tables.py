"""依成分重建後，把藥物頁「## EU Market Information」段落的許可證表換成程式產生的表（2026-11-06，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles（EMA 人用集中許可，含複方與已撤銷的許可）。
- 段落裡的第一張表（不論原欄位）換成「| Authorization Number | Product Name | Active Substance | Status |」：
  證據包紀錄依原順序（有效在前、單方在前），產品名拿掉 EMA 的「(previously …)」舊名附註；Status 依 EMA「Medicine status」：Authorised 寫 Valid（本站許可證表原本的寫法），
  其他照 EMA 原文（Withdrawn、Lapsed、Expired…）。原表的「(cancelled)」等許可證號註記、適應症摘錄一併換掉（EMA 狀態才是事實）。
  最多列 20 筆，多於 20 筆時表後加一句「Showing 20 of N EMA authorisations.」。
- 表後 known_use_pages 寫的「Only part of the licence list is held in the data; the list may be incomplete.」：
  重建後的紀錄是完整清單，這句跟事實矛盾，一併拿掉（仍是部分紀錄的證據包保留）。
- 新資料沒有任何許可時拿掉表，改一句「No centrally authorised medicine containing this substance was found in the EMA medicines report used for this report.」
- 段落裡沒有表的頁不新增；表以外的文字不動（跟新事實矛盾的句子由 tools/txgnn/.claude/delete_license_sentences.py 處理）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## EU Market Information"
HEAD = ["| Authorization Number | Product Name | Active Substance | Status |", "|------|------|------|------|"]
NONE_LINE = "No centrally authorised medicine containing this substance was found in the EMA medicines report used for this report."
SHOW = "Showing {n} of {m} EMA authorisations."
SHOW_RX = re.compile(r"^Showing \d+ of \d+ EMA authorisations\.$")
PART_NOTE = "Only part of the licence list is held in the data; the list may be incomplete."
MAX_ROWS = 20


def cell(x, n=80):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def table_rows(recs):
    seen, rows = set(), []
    for r in recs:
        k = r.get("license_id")
        if not k or k in seen:
            continue
        seen.add(k)
        st = str(r.get("status") or "").strip()
        name = re.sub(r"\s*\(previously [^()]*\)", "", str(r.get("brand_name_en") or ""))  # 舊名附註拿掉（「… Pharma KG」會被當成知識圖譜字樣）
        rows.append(f"| {k} | {cell(name, 70)} | {cell(str(r.get('ingredients') or '').replace(';', '; '))} | "
                    f"{'Valid' if st == 'Authorised' else (st or 'Not recorded')} |")
    return rows


def process(text, recs, partial=False):
    lines = text.split("\n")
    if SEC not in lines:
        return None
    a = lines.index(SEC) + 1
    b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None
    x, y = tb[0], tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and (partial or l.strip() != PART_NOTE)]
    rows = table_rows(recs)
    if rows:
        block = HEAD + rows[:MAX_ROWS]
        if len(rows) > MAX_ROWS:
            block += ["", SHOW.format(n=MAX_ROWS, m=len(rows))]
    else:
        block = [NONE_LINE]
    out = lines[:x] + block + rest + lines[b:]
    if out[x - 1].strip():
        out.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return t2 if t2 != text else None


def main(argv):
    dry = "--dry-run" in argv
    only = {a for a in argv if not a.startswith("--")}
    n = 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        bf = ROOT / "data/bundles" / page.stem / "drug_bundle.json"
        if not bf.exists():
            bf = ROOT / "data/bundles" / page.stem.replace("-", "_") / "drug_bundle.json"
        if not bf.exists():
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        reg = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        recs = reg.get("records") or []
        new = process(raw.replace("\r\n", "\n"), recs, int(reg.get("total_matches") or 0) > len(recs))
        if new is None:
            continue
        n += 1
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    print(f"許可證表改 {n} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
