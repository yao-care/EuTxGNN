#!/usr/bin/env python3
"""產生 docs/_data/drug_stats.json，並同步／檢查站上寫死的藥物數（照 TwTxGNN 同名檔的規則移植，2026-10-27）。

為什麼需要這支：
  站上的藥物總數曾經散落寫死在 news.md、smart/*.md、首頁、head_custom.html 的 JSON-LD 裡，
  產線新增藥物後沒人改，出現 642／664 兩種數字（drug-count-text-sync-gap）。

規則（與 TwTxGNN 一致，不要混用）：
  - 能用 Liquid 的地方一律寫 {{ site.data.drug_stats.total_drugs }}（.md 內文、_includes/*.html），
    不列在 COUNT_SPOTS。head_custom.html 全部走 Liquid，所以不在 COUNT_SPOTS 裡——
    同一處不能既是 Liquid 又被本支用正則改回數字（twtxgnn 踩過的坑）。
  - 不能用 Liquid 的地方才列 COUNT_SPOTS：front matter description（jekyll-seo-tag 直接輸出）、
    沒有 front matter 的靜態檔（llms-full.txt）、不經 Jekyll 的 README.md。
  - total_drugs＝公開的藥物報告數＝docs/_drugs/*.md 扣掉 noindex 頁與舊 ID 轉址頁
    （和 docs/drugs.md 列表的 where_exp 篩選相同；_drugs 檔案數會比這個多）。
  - total_indications＝公開藥物頁 front matter indication_count 加總。

守門（兩層）：
  - Jekyll 建置內：docs/drugs.md 比對 drug_stats.json 與實際公開藥物頁數／等級分布，不符就 include
    不存在的檔讓 GitHub Pages 建置失敗（錯誤訊息即修法）。
  - 本支 --check（seo-ops 的 scripts/check_seo_docs.py 第 5 項也會跑）：另外檢查 COUNT_SPOTS 與
    Liquid 檔裡寫死的藥物數，逐檔指名。

用法：
  python3 scripts/generate_drug_stats.py           # 重算 drug_stats.json 並改正 COUNT_SPOTS
  python3 scripts/generate_drug_stats.py --check   # 只檢查，不一致就列出檔案並以非零結束（CI gate）
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRUGS = ROOT / "docs" / "_drugs"
OUT = ROOT / "docs" / "_data" / "drug_stats.json"

# (檔案, 正則（group 2 是數字）, 數字來源)；每條必須剛好命中一處
COUNT_SPOTS = [
    ("docs/index.md", r'(^description: "AI-powered drug repurposing predictions for )(\d+)( EMA-approved drugs)', "total"),
    ("docs/index.md", r'(generating \*\*)([\d,]+)(\*\* potential new therapeutic uses)', "indications"),
    ("docs/index.md", r'(medicines with )([\d,]+)( repurposing predictions)', "indications"),
    ("docs/index.md", r'(^\| Repurposing Predictions \| )([\d,]+)( \|)', "indications"),
    ("docs/llms-full.txt", r'(AI-powered drug repurposing predictions for )(\d+)( EMA-approved drugs)', "total"),
    ("README.md", r'(^\| \*\*Drug Reports\*\* \| )(\d+)( \|)', "total"),
]

# Liquid 可用的檔案裡不得再出現寫死的藥物總數（出現就要改成 {{ site.data.drug_stats.total_drugs }}）
HARDCODE_PATTERNS = [
    re.compile(r"\b(\d{3,4}) (?:EMA[- ]approved|EMA centrally-authorized|EMA drug)"),
    re.compile(r"\*\*(\d{3,4}) Drugs\*\*"),
    re.compile(r"\*\*(\d{3,4})\*\* EMA"),
    re.compile(r"\| Drug Reports \| (\d{3,4}) \|"),
    re.compile(r"\((\d{3,4}) drugs\)"),
    re.compile(r"\bAll (\d{3,4}) drugs\b"),
    re.compile(r"\bhealth news for (\d{3,4}) drugs\b"),
]


def front(text):
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    meta = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def listed_drugs():
    drugs = []
    for p in sorted(DRUGS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = front(text)
        if fm.get("noindex", "").lower() == "true" or fm.get("layout") == "id_redirect":
            continue
        drugs.append({
            "name": fm.get("title", p.stem),
            "slug": p.stem,
            "level": fm.get("evidence_level", "L5"),
            "indication_count": int(fm.get("indication_count") or 0),
        })
    drugs.sort(key=lambda d: (d["name"].lower(), d["slug"]))
    return drugs


def build_stats(drugs, generated):
    counts = {f"L{n}": sum(d["level"] == f"L{n}" for d in drugs) for n in range(1, 6)}
    return {"generated": generated, "total_drugs": len(drugs),
            "total_indications": sum(d["indication_count"] for d in drugs),
            "level_counts": counts, "all_drugs": drugs}


def count_sources(stats):
    return {"total": str(stats["total_drugs"]), "indications": f"{stats['total_indications']:,}"}


def count_spot_problems(stats, fix=False):
    src, errs, by_file = count_sources(stats), [], {}
    for rel, pat, key in COUNT_SPOTS:
        by_file.setdefault(rel, []).append((re.compile(pat, re.M), key))
    for rel, rules in by_file.items():
        path = ROOT / rel
        text = path.read_bytes().decode("utf-8")
        new = text
        for rx, key in rules:
            ms = list(rx.finditer(new))
            if len(ms) != 1:
                errs.append(f"{rel}：找不到（或不只一處）{rx.pattern}")
                continue
            want = src[key]
            if ms[0].group(2) != want:
                errs.append(f"{rel}：寫死的數字 {ms[0].group(2)} 應為 {want}（{key}）")
                new = rx.sub(lambda m: m.group(1) + want + m.group(3), new, count=1)
        if fix and new != text:
            path.write_bytes(new.encode("utf-8"))
    return errs


def hardcode_problems():
    """Liquid 可用的檔（docs 下的 .md／.html，不含 _drugs、_news 內容）不得寫死藥物總數。
    COUNT_SPOTS 管的那幾處先遮掉再掃。"""
    errs = []
    docs = ROOT / "docs"
    for p in sorted(list(docs.rglob("*.md")) + list(docs.rglob("*.html"))):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(("docs/_drugs/", "docs/_news/", "docs/_site/")):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for r2, pat, _ in COUNT_SPOTS:
            if r2 == rel:
                text = re.sub(pat, lambda m: m.group(1) + "#" * len(m.group(2)) + m.group(3), text, flags=re.M)
        for rx in HARDCODE_PATTERNS:
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                errs.append(f"{rel}:{line}：寫死的藥物數「{m.group(0)}」，改用 {{{{ site.data.drug_stats.total_drugs }}}}")
    return errs


def main():
    check = "--check" in sys.argv[1:]
    drugs = listed_drugs()
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    errs = []
    if check:
        want = build_stats(drugs, old.get("generated", ""))
        if {k: v for k, v in old.items() if k != "generated"} != {k: v for k, v in want.items() if k != "generated"}:
            errs.append(f"docs/_data/drug_stats.json：total_drugs={old.get('total_drugs')}，公開藥物頁 {len(drugs)} 頁"
                        f"（或等級／適應症數不符）")
        stats = want
    else:
        stats = build_stats(drugs, old.get("generated", ""))
        if {k: v for k, v in old.items() if k != "generated"} != {k: v for k, v in stats.items() if k != "generated"}:
            stats["generated"] = date.today().isoformat()
            OUT.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"drug_stats.json：{stats['total_drugs']} 個藥，{stats['total_indications']} 個預測適應症，{stats['level_counts']}")
    errs += count_spot_problems(stats, fix=not check)
    errs += hardcode_problems()
    if check:
        if errs:
            print("藥物數同步檢查：✗（修法：python3 scripts/generate_drug_stats.py，Liquid 檔手改）")
            for e in errs:
                print("  ✗", e)
            sys.exit(1)
        print(f"藥物數同步檢查：✓（{stats['total_drugs']} 個藥物報告）")
    else:
        rest = [e for e in errs if "應為" not in e]
        print(f"寫死的藥物數：更新 {len(errs) - len(rest)} 處")
        for e in rest:
            print("  ✗", e)
        sys.exit(1 if rest else 0)


if __name__ == "__main__":
    main()
