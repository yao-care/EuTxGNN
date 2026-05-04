---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog alfa: From Hemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa (Idelvion®) is a long-acting, albumin-fused recombinant Factor IX (rIX-FP), approved internationally for prophylaxis and treatment of bleeding in Hemophilia B (congenital Factor IX deficiency). The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease** (Score: 99.94%), the top-ranked prediction among 10 bleeding and coagulation disorder candidates — however, **no supporting clinical trials or publications** currently exist for this specific indication. The overall picture across all 10 predictions is cautious: mechanistic connections are largely indirect, two indications carry active harm signals, and the most scientifically credible candidate is **acquired coagulation factor deficiency** (Rank 7, Research Question stage).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia B (congenital Factor IX deficiency) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Albutrepenonacog alfa is a recombinant Factor IX (FIX) genetically fused to human serum albumin via a cleavable linker. This albumin-fusion technology extends the half-life of FIX to approximately 102 hours — compared to 18–24 hours for conventional FIX concentrates — enabling weekly or less-frequent prophylactic dosing for Hemophilia B patients. Its mechanism centers on replacing deficient FIX in the intrinsic coagulation pathway: FIXa assembles with its cofactor FVIIIa on phosphatidylserine-rich platelet membranes to form the intrinsic "tenase complex," which activates Factor X and drives thrombin generation and stable clot formation.

Pseudo-von Willebrand disease (platelet-type vWD) is a **primary hemostasis disorder** caused by a gain-of-function mutation in the platelet glycoprotein GPIb receptor. The mutant GPIb spontaneously binds large von Willebrand factor (vWF) multimers with abnormally high affinity, depleting high-molecular-weight vWF from plasma and triggering inappropriate platelet aggregation and thrombocytopenia. This pathology is fundamentally distinct from — and upstream of — the plasma coagulation cascade where FIX operates.

The mechanistic rationale is therefore **weak**: FIX supplementation cannot correct the GPIb–vWF binding defect, restore vWF multimer distribution, or normalize platelet counts. The TxGNN prediction is most likely driven by phenotypic co-clustering of bleeding disorder nodes in the underlying knowledge graph, rather than a direct biological relationship. Detailed MOA data (currently unavailable as a High-severity data gap) would be required to formally evaluate any indirect pathway. **The most mechanistically credible repurposing target across all 10 predictions is Rank 7 — acquired coagulation factor deficiency** — where disease-specific FIX depletion (e.g., FIX adsorption in systemic amyloidosis, or FIX deficiency secondary to Gaucher disease) would align directly with albutrepenonacog alfa's primary mechanism and extended half-life advantage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pseudo-von Willebrand disease.

> **Cross-indication note:** A search across all 10 predicted indications identified one trial — [NCT02546622](https://clinicaltrials.gov/study/NCT02546622) — which was retrieved under the "inherited thrombophilia" query (Rank 10). This is a longitudinal observational study (N=310) of Hemophilia A/B patients switching between factor replacement products (albutrepenonacog alfa being one such product), and provides **no evidence** for any of the 10 predicted indications. Its retrieval is an artifact of albutrepenonacog alfa's presence in the switch study, not any connection to inherited thrombophilia.

---

## Literature Evidence

Currently no related literature available for pseudo-von Willebrand disease.

---

## Taiwan Market Information

Albutrepenonacog alfa is currently **not registered** in Taiwan. No TFDA marketing authorizations are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No Taiwan registration found |

> Albutrepenonacog alfa is approved internationally as Idelvion® (CSL Behring) in the European Union (EU/1/15/1072), the United States (FDA), and other major markets for Hemophilia B. A Taiwan registration would require a separate TFDA application and cannot be assumed from existing international approvals.

---

## Safety Considerations

TFDA package insert warnings and contraindications are not currently available (Blocking data gap DG001). Please refer to the EU Summary of Product Characteristics (SmPC) for Idelvion® for full prescribing information.

Based on class-level knowledge of Factor IX replacement therapy, the following safety considerations apply:

- **Hypersensitivity reactions:** Anaphylaxis is possible, with higher risk in patients who have developed FIX inhibitors or those with large gene deletions/null mutations. Adrenaline should be available during infusion.
- **Inhibitor development:** Neutralising antibodies (inhibitors) to FIX may form, particularly in previously untreated patients. Regular inhibitor monitoring is required.
- **Thromboembolism:** Excessive FIX supplementation raising levels above the physiological range may increase thromboembolic risk; dose titration and monitoring of FIX trough/peak levels are required.
- **Nephrotic syndrome:** Reported in patients with FIX inhibitors undergoing immune tolerance induction with high-dose FIX products; mechanism involves immune complex deposition.

No drug-drug interaction data were identified in this Evidence Pack. As a recombinant biologic, classical cytochrome P450-mediated DDIs are not expected.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high mathematical prediction score (99.94%), but the biological mechanism connecting Factor IX to pseudo-von Willebrand disease is indirect and insufficient to justify further development at this time. The disease operates on a fundamentally different hemostatic axis (platelet GPIb–vWF primary hemostasis) from FIX's coagulation function, with zero supporting clinical trials or published literature.

**To proceed, the following is needed:**

- **Pivot to Rank 7 (Acquired Coagulation Factor Deficiency):** This is the only indication in this panel with direct mechanistic alignment to albutrepenonacog alfa. Conduct a targeted literature review for FIX-specific acquired deficiency (e.g., amyloidosis-associated FIX adsorption, Gaucher disease) before deciding whether a formal case series or prospective study is warranted.
- **Resolve DG001 — TFDA Package Insert (Blocking):** Obtain TFDA SmPC warnings and contraindications (download PDF from TFDA website) before any Taiwan-specific safety assessment can proceed.
- **Resolve DG002 — Mechanism of Action (High):** Retrieve complete MOA data from DrugBank (DB13884) to enable formal mechanistic link scoring across all predicted indications.
- **Actively exclude harm-signal indications:** Remove **thrombotic thrombocytopenic purpura** (Rank 8) and **inherited thrombophilia** (Rank 10) from any repurposing program. Both carry a mechanistic harm signal — administering a pro-coagulant FIX to patients with pre-existing thrombotic pathology could directly worsen outcomes.
- **Taiwan regulatory pathway:** Note that albutrepenonacog alfa currently has no TFDA marketing authorization. Any repurposing program targeting Taiwan patients must account for the cost and timeline of an initial TFDA registration in addition to the repurposing indication filing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

