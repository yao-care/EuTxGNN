---
layout: default
title: Regadenoson
parent: AI Predictions (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Regadenoson
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Regadenoson：從心肌灌注造影壓力劑到全身型過敏反應（Anaphylaxis）— 訊號可信度存疑

## 一句話摘要

Regadenoson 目前在歐盟未取得上市許可（本資料庫查無核准適應症與作用機轉資料），臨床實務上作為心肌灌注造影（MPI）的藥理性壓力測試劑使用。TxGNN 模型將 **全身型過敏反應（Anaphylaxis）** 列為預測分數最高（99.85%）的新適應症，但現有 **1 筆臨床試驗（無直接相關）** 與 **0 篇文獻** 支持，且系統性判讀認為此訊號極可能反映的是藥物本身已知的不良反應（過敏樣反應），而非治療效果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 未登錄（歐盟Not marketed；依臨床試驗文本脈絡，臨床實務用途為心肌灌注造影之藥理性壓力劑） |
| 預測新適應症 | Anaphylaxis（全身型過敏反應） |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 歐盟市場狀態 | Not marketed |
| 核准許可數 | 0 |
| 建議決策 | **Hold（暫緩）** |

---

## 為什麼這個預測需要高度存疑？

目前沒有 Regadenoson 的作用機轉（MOA）資料可供查詢，這是本案的第一個資料缺口，且被標記為 Blocking（阻斷性）等級，代表在補齊之前無法進入標準的安全性初評流程。

更關鍵的問題在於**機轉方向與預測方向相反**。Regadenoson 是選擇性 adenosine A2A 受體促效劑，已知的藥理特性是可能誘發肥大細胞脫顆粒與過敏樣（pseudoallergic）反應——這是文獻中反覆記載的**不良反應**，而非可被此藥「治療」的疾病。同樣的模式也出現在本次預測清單的其他候選適應症中：headache disorder（排名第5）與 migraine disorder（排名第6）的證據來源，全部是研究「如何減少 regadenoson 引發頭痛/偏頭痛副作用」的試驗與個案報告，而非治療頭痛的證據；pseudoallergy（排名第4）同樣被標註為已知副作用而非適應症。

這種一致性的反向因果模式（AI 學到「藥物 X 與副作用 Y 高度共現」，卻被排序演算法解讀為「藥物 X 可能治療 Y」）強烈提示，本組預測結果可能是**不良反應訊號污染**造成的假陽性，而非真正的老藥新用機會。在補齊 MOA 與安全性資料之前，不建議將此候選推進至後續評估階段。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 重點發現 |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | NA | 招募中 | 1000 | 研究主題為心臟壓力灌注 MRI 造影方案，用以評估胸痛/呼吸困難是否源於冠狀動脈疾病；**並非以 regadenoson 治療 anaphylaxis**，相關性評級為 C（低度相關） |

目前沒有任何試驗直接研究 regadenoson 用於治療全身型過敏反應。

---

## 文獻證據

目前無相關文獻資料。

---

## 安全性考量

請參閱 SmPC（產品特性摘要）以取得安全性資訊。

> 補充說明：本資料庫查無 Regadenoson 之關鍵警語、禁忌症與藥物交互作用資料，此為 Blocking 等級之資料缺口（DG001），在此缺口補齊前不應進行任何安全性相關決策。

---

## 結論與下一步

**決策：Hold（暫緩）**

**理由：**
- 頂端預測適應症（anaphylaxis）在機轉上與藥物已知的不良反應方向相反，證據極可能為 AE 訊號污染，而非真實療效訊號。
- 作用機轉（MOA）與 TFDA/EMA 安全性仿單資料為 Blocking 等級缺口，目前無法進行 S1 安全性初評。
- 該藥物在歐盟未取得上市許可，無既有核准適應症可作為機轉延伸的比對基礎。

**若要繼續推進，需要補齊：**
- 透過 DrugBank API 查詢 Regadenoson 完整作用機轉資料（DG002）
- 取得 TFDA／原廠仿單之警語與禁忌症全文，解析後填入安全性初評（DG001）
- 針對本候選藥物之全部預測清單，建議先進行「療效訊號 vs. 不良反應訊號」的人工機轉審查，排除已知副作用被誤判為適應症的候選項目，再決定是否有任何項目值得進入 S1 階段
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

