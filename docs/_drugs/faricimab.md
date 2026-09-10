---
layout: default
title: Faricimab
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Faricimab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Faricimab: From Diabetic Macular Edema/nAMD to Diabetic Retinopathy

> **Selection note**：TxGNN 本次 Top-10 原始預測中，分數最高者（如 primary release disorder of platelets、pseudo-von Willebrand disease 等）皆為機轉不合理、零證據的雜訊項（模型依器官/圖譜關聯外推），評分卡本身也將其列為 Hold。本報告聚焦 Top-10 中唯一有實質臨床與文獻證據支持的項目——**Diabetic Retinopathy**（原始排名第 8，score 96.75%），並附帶提及機轉相近的 severe nonproliferative diabetic retinopathy（排名第 6）作為早期訊號。

## One-Sentence Summary

Faricimab（Vabysmo）是一款雙特異性單株抗體，透過玻璃體內注射同時中和 VEGF-A 與 Angiopoietin-2，已核准用於濕性年齡相關性黃斑部病變（nAMD）與糖尿病黃斑水腫（DME）。TxGNN 模型預測其可延伸應用於更廣泛的**糖尿病視網膜病變（Diabetic Retinopathy）**，目前有 **25 項臨床試驗**與 **20 篇文獻**支持這個方向，其中包含 4 項已完成的第三期關鍵試驗。

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 濕性年齡相關性黃斑部病變（nAMD）、糖尿病黃斑水腫（DME）（依文獻 PMID 35474059 "Faricimab: First Approval" 及 YOSEMITE/RHINE、TENAYA/LUCERNE 試驗登記資訊；台灣尚無核准適應症記錄） |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 |
| Number of Authorizations（台灣） | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Faricimab 為雙特異性單株抗體，同時中和 VEGF-A 與 Angiopoietin-2 兩條路徑，抑制視網膜血管新生與血管滲漏，經玻璃體內注射給藥。此為其已於 nAMD 與 DME 驗證之核心機轉。（原始 `original_moa` 欄位標記為 [Data Gap]，以上機轉描述依藥物已知公開資料補充，非資料庫內建欄位證據。）

糖尿病視網膜病變（DR）與 DME 本質上屬同一疾病譜系——DME 是 DR 的黃斑部併發症，兩者共享「視網膜缺血驅動 VEGF/Ang-2 上調」的核心病理機轉。因此將適應症從 DME 延伸至整體 DR（含非增殖性與增殖性階段），屬於同一機轉在同一器官系統內的自然外推，而非全新機轉假說。

支持此延伸的訊號已具體化為臨床試驗：MAGIC 試驗（NCT05681884）專門針對非增殖性 DR（NPDR）之視網膜無灌流區設計 Phase 2 研究；NCT06790784 則以 Phase 3 規模比較 Faricimab+PRP 與傳統玻璃體切除術治療增殖性 DR（PDR）。這顯示產業界已將此假說推進至前瞻性臨床驗證階段，而非僅止於模型推論。

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03622593](https://clinicaltrials.gov/study/NCT03622593) | Phase 3 | Completed | 951 | RHINE：Faricimab vs Aflibercept 治療 DME，療效/安全性/PK 註冊試驗 |
| [NCT03622580](https://clinicaltrials.gov/study/NCT03622580) | Phase 3 | Completed | 940 | YOSEMITE：與 RHINE 為雙生註冊試驗，DME 8 週給藥間隔 vs Aflibercept |
| [NCT03823300](https://clinicaltrials.gov/study/NCT03823300) | Phase 3 | Completed | 658 | LUCERNE：nAMD 適應症關鍵試驗，構成核准基礎的同機轉證據 |
| [NCT03823287](https://clinicaltrials.gov/study/NCT03823287) | Phase 3 | Completed | 671 | TENAYA：nAMD 關鍵試驗，與 LUCERNE 互為對照 |
| [NCT05224102](https://clinicaltrials.gov/study/NCT05224102) | Phase 4 | Active, not recruiting | 218 | 上市後研究，評估未接受治療、代表性不足族群 DME 之治療反應 |
| [NCT05681884](https://clinicaltrials.gov/study/NCT05681884) | Phase 2 | Active, not recruiting | 179 | MAGIC：專門針對非增殖性 DR（NPDR）視網膜無灌流區之隨機對照試驗 |
| [NCT06790784](https://clinicaltrials.gov/study/NCT06790784) | Phase 3 | Recruiting | 426 | 比較 Faricimab+PRP 與玻璃體切除術+雷射治療增殖性 DR（PDR） |
| [NCT04597918](https://clinicaltrials.gov/study/NCT04597918) | Phase 2B | Completed | 99 | ALTIMETER：DME 患者房水生物標記與多模式影像探索性研究 |
| [NCT05476926](https://clinicaltrials.gov/study/NCT05476926) | N/A | Active, not recruiting | 6000 | VOYAGER：多國真實世界長期資料收集（涵蓋 nAMD/DME） |
| [NCT06439576](https://clinicaltrials.gov/study/NCT06439576) | N/A | Recruiting | 1000 | Farseeing：中國真實世界研究，涵蓋 DME/RVO/nAMD 治療模式與安全性 |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38158159](https://pubmed.ncbi.nlm.nih.gov/38158159/) | 2024 | RCT | Ophthalmology | YOSEMITE/RHINE 兩年期結果：Treat-and-Extend 給藥下之療效與安全性 |
| [36246184](https://pubmed.ncbi.nlm.nih.gov/36246184/) | 2022 | RCT | Ophthalmology Science | YOSEMITE/RHINE 研究設計與理論基礎 |
| [38852921](https://pubmed.ncbi.nlm.nih.gov/38852921/) | 2024 | RCT | Ophthalmology | 基線視力較差亞群中 Faricimab vs Aflibercept 療效分析 |
| [36012690](https://pubmed.ncbi.nlm.nih.gov/36012690/) | 2022 | RCT | Int J Mol Sci | Aflibercept 與 Faricimab 治療 nAMD/DME 之比較回顧 |
| [35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/) | 2022 | Cohort | Lancet | YOSEMITE/RHINE：每 16 週延展給藥之療效、持久性與安全性 |
| [37751021](https://pubmed.ncbi.nlm.nih.gov/37751021/) | 2023 | Review | Advances in Therapy | DME 治療之系統性文獻回顧與網絡統合分析 |
| [35474059](https://pubmed.ncbi.nlm.nih.gov/35474059/) | 2022 | (pending) | Drugs | Faricimab 首次核准（nAMD、DME），確立原始適應症與機轉 |
| [30905643](https://pubmed.ncbi.nlm.nih.gov/30905643/) | 2019 | Preclinical | Ophthalmology | BOULEVARD Phase 2：Faricimab vs Ranibizumab 治療 DME |
| [38847896](https://pubmed.ncbi.nlm.nih.gov/38847896/) | 2024 | Review | Graefe's Archive | Faricimab 由臨床前研究至 Phase 3 結果之整體回顧 |
| [35818801](https://pubmed.ncbi.nlm.nih.gov/35818801/) | 2022 | Review | Expert Opin Biol Ther | 玻璃體內抗 VEGF 治療糖尿病視網膜病變之療效與安全性回顧 |

## Taiwan Market Information

台灣目前無 Faricimab 上市許可證記錄（`market_status`: 未上市，`total_licenses`: 0）。

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Faricimab 在同一血管新生機轉（VEGF-A/Ang-2 雙重抑制）下已有 4 項完成的第三期 RCT（YOSEMITE、RHINE、TENAYA、LUCERNE，符合 L1 標準），且已有 Phase 2（MAGIC，NPDR）與 Phase 3（NCT06790784，PDR）試驗專門針對更廣泛的糖尿病視網膜病變族群，機轉外推合理、證據鏈完整，但尚未在台灣取得上市許可，且缺乏台灣仿單安全性資料。

**To proceed, the following is needed:**
- 補齊 TFDA 仿單警語、禁忌症與藥物交互作用資料（DG001，Blocking）
- 補齊正式 MOA/DrugBank 機轉資料以完成機轉關聯性分析（DG002，High）
- 追蹤 MAGIC（NCT05681884）與 NCT06790784 之最終療效讀出，確認 DR（含 NPDR/PDR）適應症延伸之直接證據
- 評估台灣藥證申請/擴增適應症之法規途徑與時程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

