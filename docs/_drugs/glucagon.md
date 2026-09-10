---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Glucagon
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

# Glucagon: From Unknown/Not Marketed Indication to Irritable Bowel Syndrome

## 一句話總結

Glucagon（升糖素）目前在歐盟**未取得上市許可**（0 筆核准），本證據包也未提供其原始適應症文字與作用機轉資料。TxGNN 模型將 **Irritable Bowel Syndrome (IBS)** 列為第一預測適應症，分數達 **99.24%**，並有 **11 篇臨床試驗**與 **20 篇文獻**被檢索到；但仔細核對後，這些證據絕大多數研究的是 **GLP-1（glucagon-like peptide-1）受體促效劑**而非 glucagon 本身，存在明顯的藥名/實體混淆風險。

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | 資料缺口 — 本品於 EU 未上市，證據包未提供核准適應症文字（見 DG001） |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L4 |
| EU Market Status | 未上市 |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable？

目前本品的作用機轉（MOA）資料缺失（DG002，屬 High severity，影響機轉關聯性分析），且因本品於 EU 未上市，證據包中也沒有核准適應症文字可供比對（DG001，屬 Blocking severity，連帶使安全性初評 S1 無法完整進行）。因此無法對「原始適應症」與「預測新適應症」進行常規的機轉層面比對。

必須特別指出：檢索到的 11 篇臨床試驗與 20 篇文獻中，證據高度集中在 **GLP-1 受體促效劑**（如 ROSE-010、exendin-4）及其衍生藥物（dulaglutide、liraglutide、semaglutide、tirzepatide）於 IBS 動力障礙、疼痛緩解的研究，而非 glucagon（升糖素）本身。這是典型的「glucagon」與「glucagon-like peptide-1 (GLP-1)」名稱相似導致的實體混淆，知識圖譜可能因此產生雜訊配對。

臨床上已知 glucagon 具有誘發腸道平滑肌鬆弛的作用（常用於內視鏡/鋇劑攝影前解痙），此與 IBS 的腸道動力障礙具有理論上的關聯性；但目前檢索到的證據裡，**幾乎沒有直接研究 glucagon 本身用於 IBS 的資料**，故此關聯目前仍停留在假說層次，而非被證據支持的機轉路徑。

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | NA | Completed | 12 | 特發性反應性低血糖盛行率與果寡糖補充研究；無 glucagon 藥物介入，相關性低（grade C） |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | NA | Completed | 37 | 研究丁酸鹽於人體結腸的作用機轉；與 glucagon 無關（grade C） |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | NA | Completed | 33 | 腸道菌叢營養介入研究，探討高海拔暴露下的腸道屏障完整性；無 glucagon 成分（grade C） |
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | 評估 ROSE-010（合成 GLP-1 類似物，非 glucagon）對便秘型 IBS 患者腸胃動力的影響（grade C，藥物身份不符） |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | NA | Completed | 66 | 比較兩種運動強度對 IBS 患者腸道菌群失衡與 GLP-1 荷爾蒙的影響 |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | 研究天然 GLP-1（非 glucagon）對餐後胃十二指腸空腸動力的抑制作用（grade C） |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | 建立小腸類器官模型以評估營養抗原或治療劑的影響 |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | NA | Completed | 33 | 研究全穀黑麥麵包對腸-腦軸微生物調節的影響 |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | NA | Unknown | 110 | 比較低熱量飲食合併行為治療 vs. 合併胃內水球對肥胖成人的療效 |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | NA | Completed | 41 | 研究超加工食品進食速度對飲食攝取行為與代謝反應的影響 |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | RCT | Scandinavian Journal of Gastroenterology | GLP-1 受體促效劑 ROSE-010 於 IBS 疼痛緩解之交叉分析（非 glucagon） |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Review | Frontiers in Endocrinology | GLP-1 受體促效劑改善 IBS 之系統性回顧與統合分析 |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Therapeutic Advances in Gastroenterology | IBS 治療現況回顧（纖維、解痙劑之外的療法） |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | 便秘型 IBS 新型研發藥物回顧 |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Preclinical/Early | Advances in Experimental Medicine and Biology | 霧化吸入型 GLP-1 於糖尿病與 IBS 治療之早期研究 |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | GLP-1 在 IBS 病理生理中的內分泌調控角色 |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | 動物實驗 | Neurogastroenterology and Motility | GLP-1 促效劑 exendin-4 改善 IBS 大鼠模型腸胃功能障礙 |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | 觀察性研究 | Clinics and Research in Hepatology and Gastroenterology | 便秘型 IBS 患者血清 GLP-1 濃度下降與腹痛之相關性 |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | 觀察性研究 | Frontiers in Nutrition | 低 FODMAP 飲食對 IBS 患者循環 GLP-1 濃度的影響 |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | 真實世界研究 | Annals of Gastroenterology | GLP-1 受體促效劑在 IBS 患者中的處方與停藥模式 |

> 註：以上文獻主體皆圍繞 **GLP-1 受體促效劑**，非 glucagon 本身的直接療效證據。

## EU Market Information

目前本品於歐盟未取得任何上市許可（0 筆核准紀錄），無法列出授權資訊。

## Safety Considerations

Please refer to the SmPC for safety information.

（DDI 查詢無結果；警語與禁忌症資料均為缺口，對應 DG001 — 屬 Blocking severity，須先取得 TFDA/EU SmPC 仿單資料才能進行安全性初評。）

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本品於歐盟未上市、無安全性標籤資料（DG001，Blocking），且作用機轉未知（DG002）。雖然 IBS 的 TxGNN 分數高達 99.24%、evidence level 達 L4，但支撐證據中絕大多數研究對象實為 GLP-1 受體促效劑而非 glucagon 本身，存在藥物實體混淆的高度風險，其餘 9 個預測適應症（cauda equina syndrome、neurogenic bladder 等）皆為 L5，無任何臨床或文獻支持，或方向相反（如 pharyngitis、filariasis 為藥物副作用/疾病影響荷爾蒙的反向證據）。整體證據品質不足以支持推進。

**To proceed, the following is needed:**
- 取得 TFDA/EU SmPC 仿單警語與禁忌症（DG001）
- 補齊 DrugBank 作用機轉資料（DG002）
- 確認知識圖譜中 glucagon 節點是否與 GLP-1 (glucagon-like peptide-1) 節點發生實體混淆或誤合併
- 針對 glucagon（非 GLP-1 類似物）本身，重新執行 IBS 專一性臨床試驗與文獻檢索
- 若持續推進，需補充 route compatibility 與劑型相容性資料（目前為 pending）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

