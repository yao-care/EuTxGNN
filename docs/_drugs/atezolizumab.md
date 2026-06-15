---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Bladder Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is a PD-L1 checkpoint inhibitor immunotherapy globally approved for multiple cancers including urothelial carcinoma, though it currently holds no Taiwan marketing authorization.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma** as its top-ranked new indication,
with **2 clinical trials** supporting this direction through biological equivalence with anatomically adjacent urothelial carcinoma subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Taiwan-registered indications (globally: urothelial carcinoma, NSCLC, TNBC, hepatocellular carcinoma) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (Data Gap DG002). Based on established clinical knowledge, Atezolizumab is a humanised monoclonal antibody that selectively binds PD-L1 (Programmed Death-Ligand 1), blocking its interaction with both PD-1 and B7.1 receptors. This restores cytotoxic T-cell activity within the tumour microenvironment. The mechanism is particularly potent in tumours with high PD-L1 expression — a hallmark of the urothelial carcinoma family regardless of anatomical site.

Prostatic urethra urothelial carcinoma is an anatomical subsite within the urothelial carcinoma spectrum. Bladder urothelial carcinoma and prostatic urethral involvement share identical cellular origin (transitional epithelium), equivalent PD-L1 overexpression profiles, and frequently co-exist in non-muscle invasive bladder cancer (NMIBC). The prostatic urethra is one of the most common sites of NMIBC extension, meaning the BCG-unresponsive NMIBC population studied in Phase 2 (NCT02844816) very likely included patients with prostatic urethral disease.

The combination of a completed Phase 2 trial in the directly adjacent disease population, near-perfect TxGNN prediction score (99.98%), and mechanistic equivalence across the urothelial carcinoma family makes this prediction biologically sound. The primary uncertainty is not biological plausibility but rather the absence of a trial specifically enrolling prostatic urethra urothelial carcinoma as a defined endpoint.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive recurrent/refractory NMIBC; immunotherapy may help the body's immune system attack cancer and interfere with tumour cell growth and spread |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, Not Recruiting | 914 | Cabozantinib ± atezolizumab in multiple solid tumours including advanced urothelial carcinoma (bladder, renal pelvis, ureter, urethra), RCC, CRPC, NSCLC, TNBC, and ovarian cancer; safety, tolerability, preliminary efficacy and pharmacokinetics assessment |

---

## Literature Evidence

Currently no related literature available for Prostatic Urethra Urothelial Carcinoma.

---

## Taiwan Market Information

Atezolizumab currently has no marketing authorization in Taiwan (0 registered licenses). No approved product records are available from TFDA. Please refer to the originator's (Roche/Genentech) global SmPC (Tecentriq) for complete product information.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — PD-L1 Checkpoint Inhibitor (monoclonal antibody; non-cytotoxic) |
| Myelosuppression Risk | Low (immune-mediated haematological events are uncommon; not associated with the typical myelosuppression of conventional cytotoxics) |
| Emetogenicity Classification | Minimal (not associated with clinically significant emetogenicity) |
| Monitoring Items | Liver function tests (ALT/AST/bilirubin), thyroid function (TSH, free T4), adrenal function, fasting glucose, CBC with differential, urinalysis; close monitoring for immune-related adverse events (irAEs) across all organ systems |
| Handling Protection | Standard biological/monoclonal antibody handling precautions apply; full cytotoxic drug handling protocols are not required |

---

## Safety Considerations

Detailed TFDA prescribing information is not yet available (Data Gap DG001 — Blocking). Please refer to the global Tecentriq SmPC for complete safety data.

Based on the drug class (PD-L1 checkpoint inhibitor), clinically important immune-related adverse events (irAEs) to anticipate include:
- **Immune-mediated pneumonitis** — potentially life-threatening; monitor for new or worsening respiratory symptoms
- **Immune-mediated colitis** — diarrhoea and abdominal pain; grade 3–4 events require corticosteroid management
- **Immune-mediated hepatitis** — ALT/AST elevation; liver function monitoring required before each cycle
- **Endocrinopathies** — hypothyroidism, hyperthyroidism, adrenal insufficiency, and diabetes mellitus (type 1-like)
- **Infusion-related reactions** — typically grade 1–2; pre-medication protocols per institutional policy

---

## Predicted Indications Overview (All 10)

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Prostatic Urethra Urothelial Carcinoma | 99.98% | L2 | Proceed with Guardrails |
| 2 | Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma | 99.98% | L4 | Research Question |
| 3 | Infiltrating Bladder Urothelial Carcinoma Sarcomatoid Variant | 99.98% | L4 | Research Question |
| 4 | Renal Pelvis Papillary Urothelial Carcinoma | 99.98% | L3 | Research Question |
| 5 | Uterine Ligament Adenocarcinoma | 99.93% | L5 | Hold |
| 6 | Endocervical Carcinoma | 99.92% | L2 | Proceed with Guardrails |
| 7 | Adenoid Cystic Carcinoma of the Cervix Uteri | 99.92% | L5 | Hold |
| 8 | Uterine Ligament Serous Adenocarcinoma | 99.92% | L5 | Hold |
| 9 | Signet Ring Cell Variant Cervical Mucinous Adenocarcinoma | 99.91% | L5 | Hold |
| 10 | Intestinal Variant Cervical Mucinous Adenocarcinoma | 99.91% | L5 | Hold |

> **Note on Rank 6 (Endocervical Carcinoma):** This indication also reaches L2, supported by a completed Phase 2 trial (NCT02921269, atezolizumab + bevacizumab in recurrent cervical cancer, n=11) and a completed Phase 1 trial (NCT03738228, atezolizumab + chemoradiotherapy, n=40). HPV-associated high tumour mutational burden and PD-L1 overexpression in endocervical carcinoma provide mechanistic rationale. Key limitation: the Phase 2 sample size (n=11) is very small.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (Prostatic Urethra Urothelial Carcinoma, L2) is supported by a completed Phase 2 trial in BCG-unresponsive NMIBC — a population in which prostatic urethral involvement is a defining clinical feature — and a large Phase 1b basket trial covering the entire urothelial tract. Atezolizumab's PD-L1 blocking mechanism is biologically uniform across the urothelial carcinoma family. Endocervical carcinoma (Rank 6) independently reaches L2 through direct HPV-related immunological rationale and dedicated cervical cancer trials.

**To proceed, the following is needed:**

- **Safety data gap (Blocking):** Obtain TFDA SmPC or global SmPC (Tecentriq) to complete contraindication and warning assessment before any S1 safety evaluation
- **MOA data gap (High):** Retrieve complete DrugBank MOA record (DB11595) to finalise mechanistic link scoring
- **Taiwan regulatory pathway:** Assess feasibility of Taiwan NDA filing or compassionate use pathway, given current zero-license status
- **Prostatic urethra–specific evidence:** Initiate or identify a dedicated clinical trial or registry study enrolling prostatic urethra urothelial carcinoma as a defined patient population
- **Sarcomatoid variants (Ranks 2–3):** Collect PD-L1 expression and EMT biomarker data in sarcomatoid urothelial subtypes before escalating from L4 to a clinical development stage
- **Endocervical carcinoma (Rank 6):** Validate in a larger Phase 2 cohort; the existing n=11 Phase 2 trial is underpowered for definitive conclusions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

