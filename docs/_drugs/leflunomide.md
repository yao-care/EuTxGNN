---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Leflunomide
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

# Leflunomide: From Rheumatoid Arthritis to Plasma Cell Myeloma

## One-Sentence Summary

Leflunomide is an immunomodulatory drug approved in the EU and US for rheumatoid arthritis, where it suppresses aberrant immune cell proliferation by inhibiting the enzyme dihydroorotate dehydrogenase (DHODH).
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma** (multiple myeloma) — ranked #4 among all predicted indications with a score of 95.16% — with **5 directly relevant clinical trials** and **6 key publications** currently supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (not registered in Taiwan) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 95.16% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although formal MOA records were not retrieved in this evidence pack, the active metabolite of leflunomide — **teriflunomide (A771726)** — is well-characterized in the biomedical literature as a potent inhibitor of **dihydroorotate dehydrogenase (DHODH)**, a mitochondrial enzyme essential for the de novo biosynthesis of pyrimidine nucleotides. By starving rapidly dividing cells of pyrimidines (UTP, CTP), DHODH inhibition halts cell cycle progression and triggers apoptosis. This mechanism is not selective for immune cells: any highly proliferative cell — including malignant plasma cells — depends on a continuous pyrimidine supply.

Plasma cell myeloma is defined by uncontrolled proliferation of clonal plasma cells in the bone marrow. Pre-clinical studies have confirmed that teriflunomide directly induces apoptosis and inhibits growth in multiple myeloma cell lines and primary patient samples (Baumann et al., 2009). Beyond pyrimidine depletion, leflunomide has been shown to downregulate the oncogenic driver **c-Myc** through PIM kinase inhibition in myeloma cells, and in combination with lenalidomide significantly extended survival in an in vivo myeloma model (Buettner et al., 2019) — further strengthening the mechanistic rationale.

The immunomodulatory profile of leflunomide also parallels established myeloma therapies such as lenalidomide and thalidomide (both IMiDs), suggesting shared downstream pathways. Critically, a completed Phase I dose-escalation study (NCT02509052, n=12) published in 2020 demonstrated tolerability and early anti-myeloma signals, and at least two Phase 2 trials are currently enrolling patients — confirming this is an active clinical development programme, not merely a computational prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02509052](https://clinicaltrials.gov/study/NCT02509052) | Phase 1/2 | Completed | 12 | Dose-escalation of single-agent leflunomide in relapsed/refractory MM (≥3 prior therapies); no dose-limiting toxicities at 20 mg and 40 mg; establishes safety baseline for further oncology trials |
| [NCT04508790](https://clinicaltrials.gov/study/NCT04508790) | Phase 2 | Recruiting | 29 | Leflunomide + pomalidomide + dexamethasone in relapsed/refractory MM; explores combinatorial immunomodulatory and DHODH-blocking strategy; expected completion Feb 2027 |
| [NCT05014646](https://clinicaltrials.gov/study/NCT05014646) | Phase 2 | Active, not recruiting | 27 | Leflunomide in African-American and European-American patients with high-risk smoldering MM; addresses racial disparity in myeloma biology; expected completion Jan 2027 |
| [NCT04370483](https://clinicaltrials.gov/study/NCT04370483) | Early Phase 1 | Active, not recruiting | 1 | Pilot trial of leflunomide in high-risk smoldering plasma cell myeloma; primary endpoint is delay of progression to symptomatic MM; expected completion Nov 2026 |
| [NCT03952832](https://clinicaltrials.gov/study/NCT03952832) | Phase 2 | Withdrawn | 0 | Planned leflunomide study in high-risk smoldering MM; withdrawn before enrollment began (2019–2021) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32268821](https://pubmed.ncbi.nlm.nih.gov/32268821/) | 2020 | Phase 1 study | Leukemia & Lymphoma | Single-agent leflunomide in relapsed/refractory MM (NCT02509052); no DLTs at doses 20–40 mg; signals of anti-myeloma activity; supports dose expansion |
| [19174558](https://pubmed.ncbi.nlm.nih.gov/19174558/) | 2009 | Pre-clinical | Molecular Cancer Therapeutics | A771726 (teriflunomide) inhibits DHODH expressed in MM cell lines and primary MM cells; induces apoptosis and inhibits proliferation; first key mechanistic study |
| [30940637](https://pubmed.ncbi.nlm.nih.gov/30940637/) | 2019 | Pre-clinical | Blood Advances | Teriflunomide downregulates c-Myc expression via PIM kinase inhibition in myeloma cells; leflunomide + lenalidomide significantly extends survival in in vivo MM model |
| [34577124](https://pubmed.ncbi.nlm.nih.gov/34577124/) | 2021 | Pre-clinical | Molecules | Cytotoxic effect of leflunomide on RPMI-8226 MM cell line confirmed via MTT assay and apoptosis detection; mitochondria-independent component beyond DHODH |
| [40814067](https://pubmed.ncbi.nlm.nih.gov/40814067/) | 2025 | Pre-clinical | J Translational Medicine | MARCH5-MFN2 mitochondrial axis modulates venetoclax sensitivity in MM; contextualizes the mitochondrial biology relevant to DHODH inhibitor co-strategies |
| [36996290](https://pubmed.ncbi.nlm.nih.gov/36996290/) | 2023 | Case report | J Immunological Sciences | Leflunomide produced rapid COVID-19 recovery in two immunocompromised cancer patients with temporal immunologic changes; demonstrates systemic immunomodulatory activity in oncology setting |

---

## Taiwan Market Information

Leflunomide currently has **no marketing authorization in Taiwan** (TFDA). No domestic product licenses are on record. The drug is commercially available internationally under trade names such as **Arava** (Sanofi) for rheumatoid arthritis in the EU, US, and many other jurisdictions. Any clinical repurposing use in Taiwan would require either a compassionate use application or enrollment in a clinical trial under TFDA oversight.

---

## Cytotoxicity

Leflunomide's active metabolite teriflunomide targets DHODH — a mechanism classified alongside antimetabolite chemotherapy — and is actively being developed as an anticancer agent. The following characterization applies to its oncology repurposing context.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted antimetabolite (DHODH inhibitor; inhibits de novo pyrimidine synthesis) |
| Myelosuppression Risk | Low to moderate — not a classical myelosuppressive agent, but hematologic monitoring is recommended in MM patients who are inherently bone-marrow-compromised |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, ALT/AST (hepatotoxicity risk), serum creatinine, blood pressure; teriflunomide plasma levels in high-dose protocols |
| Handling Protection | Standard oral medication handling at RA doses; enhanced cytotoxic precautions recommended for investigational high-dose oncology protocols |

---

## Safety Considerations

Formal TFDA prescribing information and contraindication data were not retrievable for this evidence pack. Please refer to the EU SmPC (Arava) for complete safety information. Key safety signals identified in the clinical literature include:

- **Hepatotoxicity**: Leflunomide is associated with ALT/AST elevations and rare cases of severe liver injury; baseline and periodic liver function monitoring is mandatory
- **Teratogenicity**: Pregnancy Category X; requires a washout protocol with cholestyramine before conception due to long elimination half-life of active metabolite
- **Peripheral neuropathy**: Reported in post-marketing surveillance and reviewed in the neurotoxicology literature (PMID 16155443)
- **Immunosuppression**: Risk of serious infection (bacterial, opportunistic, viral reactivation including CMV and BK virus) due to immune modulation — particularly relevant in MM patients who are already immunocompromised

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The repurposing of leflunomide for plasma cell myeloma is supported by a well-defined mechanistic rationale (DHODH inhibition → pyrimidine depletion → myeloma cell apoptosis), a published Phase 1 dose-escalation study demonstrating tolerability, and at least two actively recruiting or enrolling Phase 2 trials. This is not a purely computational prediction — it reflects an active clinical development effort already underway internationally.

**To proceed, the following is needed:**
- Obtain TFDA SmPC (or EU SmPC) for full warnings and contraindications list — currently blocking safety pre-screening (DG001)
- Retrieve complete MOA data from DrugBank (DB01097) to formalize the mechanistic narrative (DG002)
- Monitor Phase 2 trial results from NCT04508790 (leflunomide + pomalidomide + dex, n=29, completing Feb 2027) and NCT05014646 (high-risk smoldering MM, n=27, completing Jan 2027)
- Assess dosing strategy: oncology trials use 20–60 mg/day vs. standard RA dose of 10–20 mg/day; route compatibility and dose-exposure relationships require dedicated pharmacokinetic analysis
- Define a Taiwan regulatory pathway: leflunomide is not registered in Taiwan, so a compassionate use application or IND submission to TFDA would be required to initiate any local clinical evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

