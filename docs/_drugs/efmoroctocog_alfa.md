---
layout: default
title: Efmoroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa：從血友病 A 到 Pseudo-von Willebrand Disease

## 一句話摘要

> Efmoroctocog alfa 是長效型重組第八凝血因子（Factor VIII-Fc 融合蛋白），原用於血友病 A 的凝血因子替代治療。TxGNN 模型預測其可能對 **Pseudo-von Willebrand Disease** 具有潛在效益，但目前**無任何臨床試驗、無文獻**支持此方向，且模型自身的機轉描述已註明此關聯「間接且薄弱」。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 血友病 A (Hemophilia A)（依候選適應症機轉描述推論；官方核准適應症文字目前缺失） |
| 預測新適應症 | Pseudo-von Willebrand Disease |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 市場狀態 | 未上市 |
| 核准藥證數量 | 0 |
| 建議決策 | Hold |

## 這個預測合理嗎？

目前尚未取得 Efmoroctocog alfa 的完整作用機轉資料（MOA 為 Data Gap）。根據其他候選適應症的機轉描述可推知，Efmoroctocog alfa 屬於長效型重組第八凝血因子-Fc 融合蛋白（rFVIII-Fc），原始用途為補充血友病 A 患者體內不足的第八凝血因子。

針對排名第一的 Pseudo-von Willebrand Disease（血小板型 VWD），其病理根源是血小板 GPIb 受體異常導致 von Willebrand 因子被過度結合並清除，並非第八凝血因子（FVIII）本身缺乏。雖然 FVIII 與 VWF 在血漿中會形成複合體，但此疾病的根本缺陷在血小板受體而非 FVIII 濃度，因此補充 FVIII 難以糾正核心病生理問題。模型提供的機轉說明也明確指出此關聯「間接且薄弱，無任何試驗或文獻支持」。

值得留意的是，本次預測清單中的 10 個候選裡，機轉關聯性最強的其實是排名第 9 的「hemophilia A with vascular abnormality」——本質上是血友病 A 合併血管異常的亞型，與原始適應症直接重疊——但其 TxGNN 分數（99.78%）與排名（rank 900）都低於排名第一的 Pseudo-von Willebrand Disease（rank 54）。這顯示目前分數最高的候選並非機轉上最合理的候選，評估時應一併參考。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻資料。

## 藥品上市資訊

此藥品於本資料庫轄區目前未上市（核准藥證數量：0），無核准適應症文字可供摘錄。

## 安全性考量

請參閱藥品仿單（SmPC）獲取安全性資訊。

另需注意：本評估存在一項 **Blocking 等級**資料缺口（TFDA 仿單警語/禁忌尚未取得），在補齊前無法進入安全性初評（S1）階段。

## 結論與後續建議

**決策：Hold**

**理由：**
- 支持此預測的唯一依據是 TxGNN 模型分數，無任何臨床試驗或文獻佐證；
- 模型自身的機轉說明已將此關聯定性為「間接且薄弱」；
- TFDA 仿單警語/禁忌資料為 Blocking 等級缺口，尚不具備進入下一階段安全性評估的條件。

**若要推進，需要補齊：**
- TFDA 仿單警語與禁忌資料（DG001，Blocking）
- Efmoroctocog alfa 完整作用機轉（MOA）資料（DG002，High）
- 重新評估時，建議優先檢視機轉重疊度更高的候選——如 rank 9「hemophilia A with vascular abnormality」——而非目前分數最高但機轉薄弱的 rank 1 候選
- 針對 Pseudo-von Willebrand Disease 是否存在以血小板功能為切入點的替代治療機轉，補充文獻檢索
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

