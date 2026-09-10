---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
---

# Pregabalin
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

# Pregabalin: From Original Indication Not Recorded to Tendinitis

## One-Sentence Summary

Pregabalin's original approved indication is not recorded in this evidence pack (EU market status: **Not Marketed**, 0 authorizations on file). The TxGNN model predicts it may be effective for **Tendinitis**, but this is currently supported only by indirect literature (perioperative pain-management studies, case reports) with **no dedicated clinical trials** and **no established mechanistic pathway** linking pregabalin to tendon inflammation/degeneration.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no licenses or original_indications recorded in evidence pack |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pregabalin is flagged as a data gap in this evidence pack (DG002, High severity). Based on the repurposing rationale associated with this prediction, pregabalin is known to act as an α2δ subunit ligand of voltage-gated calcium channels, modulating presynaptic release of neurotransmitters such as glutamate and substance P — a mechanism established for **neuropathic pain**, not for inflammatory or degenerative tendon pathology.

Tendinitis pathology involves local inflammation, collagen degeneration, and tissue repair processes for which no known interaction with calcium-channel-mediated neurotransmitter modulation has been demonstrated. The literature returned for this prediction largely reflects pregabalin's use as a **perioperative analgesic adjunct** in patients undergoing tendon-related surgery (e.g., arthroscopic rotator cuff repair) — i.e., pain control around a tendon procedure — rather than any therapeutic effect on the tendinopathy itself. This suggests the TxGNN association was likely driven by a shared "pain" node in the knowledge graph rather than a genuine disease-modifying mechanism.

Given the absence of mechanistic support and the indirect nature of all available evidence, this prediction should be treated as hypothesis-generating only at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT (perioperative analgesia, not tendinitis therapy) | Arthroscopy | Compared oral pregabalin vs. interscalene brachial plexus block for postoperative pain after arthroscopic rotator cuff repair; addresses surgical pain, not tendinitis treatment. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort (postoperative analgesia, not tendinitis therapy) | Journal of Orthopaedic Science | Evaluated pregabalin's opioid-sparing/analgesic effect after arthroscopic rotator cuff repair surgery; conflicting evidence on effect size. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Describes fluoroquinolone (ciprofloxacin)-associated disability including tendinopathy; pregabalin not the treatment under study. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Practice | Reports posterior femoral cutaneous nerve impingement caused by hamstring tendonitis in a marathon runner; does not evaluate pregabalin as tendinitis therapy. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial/Commentary | Arthroscopy | Discusses piriformis syndrome and sciatic neurolysis with piriformis tendon release; unrelated to pregabalin's use in tendinitis. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical (different agent, rat model) | Advances in Pharmacological and Pharmaceutical Sciences | Tests *Cissus quadrangularis* plant extract (not pregabalin) for vincristine-induced peripheral neuropathy; only tangentially connected via "tendon" keyword. |

## EU Market Information

No EU marketing authorizations are recorded for this product in the current evidence pack (market status: **Not Marketed**, total licenses: 0).

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Key warnings, contraindications, and drug-interaction data for pregabalin could not be retrieved from the source used to build this evidence pack (flagged as DG001, Blocking severity — TFDA/SmPC label data not yet processed).*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no established mechanistic link between pregabalin's calcium-channel-modulating action and tendon inflammation/degeneration, no clinical trials have directly tested pregabalin for tendinitis, and the available literature reflects incidental perioperative pain-control use rather than tendinitis-directed therapy. This corresponds to Evidence Level L4 (mechanistic/indirect evidence only).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the official product label (warnings, contraindications) before any S1 safety screening can occur
- Resolve DG002 (High): confirm pregabalin's full mechanism of action to properly assess biological plausibility for tendinitis
- Confirm actual EU marketing/authorization status for pregabalin, since this pack currently shows zero licenses despite pregabalin being a well-known marketed product (Lyrica) — this discrepancy should be verified against the source registry
- If pursuing this indication, a targeted preclinical or pilot clinical study specifically measuring anti-inflammatory/tendon-healing effects (not just perioperative analgesia) would be required to generate direct evidence

*Note for prioritization: within this same evidence pack, other candidate indications for pregabalin — notably osteoarthritis (decision_stage S3, "Proceed with Guardrails") and migraine/headache disorder (decision_stage S2, "Research Question") — show substantially stronger clinical trial and literature support and may warrant separate, higher-priority evaluation reports.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

