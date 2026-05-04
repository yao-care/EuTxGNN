---
layout: default
title: Abiraterone Acetate
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Abiraterone Acetate: Evidence Pack 不完整 — 無法產生重定向預測報告

## One-Sentence Summary

Abiraterone acetate 是一種用於前列腺癌治療的雄激素生合成抑制劑，在多個國家已獲核准上市。
然而本 Evidence Pack 缺乏原始適應症記錄、TxGNN 預測結果及安全性資料，**目前無法進行完整的老藥新用評估**。
台灣藥品資料庫亦顯示本藥品尚未在台上市（0 份許可證）。

---

## Quick Overview

| 項目 | 內容 |
|------|------|
| 原始適應症 | 本 Evidence Pack 無資料 |
| 預測新適應症 | 無（TxGNN 預測結果為空） |
| TxGNN 預測分數 | N/A |
| 證據等級 | N/A |
| 台灣上市狀態 | ✗ 未上市 |
| 許可證數量 | 0 |
| 建議決策 | **Hold** |

---

## 台灣市場資訊

本 Evidence Pack 在台灣藥品資料庫中查無任何上市許可紀錄（`total_licenses = 0`）。

> **注意**：DrugBank 查詢（`query_log` ID 2）回傳成功（`result_count = 1`），但 `drugbank_id` 欄位為 `null`，顯示資料尚未正確整合至本 Evidence Pack。建議重新執行 DrugBank 映射流程以取得完整藥物資訊。

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本 Evidence Pack 在三個關鍵維度均存在資料缺口：TxGNN 預測結果為空、原始適應症與 MOA 均未取得、安全性資料全數缺失，無法支撐任何重定向評估結論。

**To proceed, the following is needed:**

- **\[Blocking\]** 從 DrugBank 補全 `drugbank_id`、MOA 及原始適應症，DrugBank 查詢已回傳 1 筆結果，需解析並寫入 Evidence Pack
- **\[Blocking\]** 執行 TxGNN 預測流程，取得 `predicted_indications` 列表；目前預測陣列為空，無法進行任何重定向分析
- **\[Blocking\]** 下載並解析台灣 TFDA 仿單 PDF，取得警語、禁忌及藥物交互作用資料
- **\[High\]** 確認台灣上市狀態；abiraterone acetate 在 FDA/EMA 等國際市場已有上市紀錄，台灣未上市狀態需進一步核實
- 完成上述資料補充後，重新產出 Evidence Pack v5 並啟動正式評估流程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

