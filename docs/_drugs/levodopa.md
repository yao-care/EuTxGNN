---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Levodopa
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is the gold-standard dopamine-replacement precursor therapy for Parkinson's disease, crossing the blood-brain barrier to restore nigrostriatal dopaminergic neurotransmission.
The TxGNN model ranks **Rasmussen Subacute Encephalitis** as the top new indication (score 99.06%), but **no clinical trials or publications** support this direction — it is a model-only prediction (L5) and is not currently actionable.
Across the full top-10 prediction set, more clinically relevant signals emerge for **PLA2G6-associated neurodegeneration**, **Lewy body dementia**, **MSA (parkinsonian type)**, and **juvenile Parkinsonism**, all rated L3 with documented secondary-parkinsonism clinical use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (established clinical standard; not retrieved from EU registry in this dataset) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| EU Market Status | Not found in registry (0 authorizations retrieved — likely a data retrieval gap) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on established pharmacological knowledge, Levodopa is the primary amino acid precursor to dopamine. It crosses the blood-brain barrier via L-type amino acid transporters and is decarboxylated by aromatic L-amino acid decarboxylase (AADC) in nigrostriatal neurons, replenishing the dopamine lost from progressive substantia nigra pars compacta neurodegeneration — the core pathology of Parkinson's disease. In clinical practice, levodopa is always co-administered with a peripheral AADC inhibitor (carbidopa or benserazide) to prevent peripheral conversion and reduce adverse effects.

Rasmussen subacute encephalitis is a rare, progressive, hemispheric autoimmune condition driven by cytotoxic CD8+ T-cell infiltration destroying neurons in one cerebral hemisphere. Its pathophysiology is immune-mediated and neuroinflammatory, manifesting as refractory seizures, progressive hemiplegia, and cognitive decline — without a defined role for dopaminergic deficits or pathway dysfunction.

The TxGNN score of 99.06% most likely reflects high-level graph-embedding proximity between neurodegeneration-associated disease nodes in the knowledge graph, rather than a direct mechanistic or clinical connection. There is currently no biological rationale, case report, or preclinical evidence supporting levodopa repurposing in Rasmussen encephalitis. This should be classified as a **knowledge-graph topology artefact**, not an actionable repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Levodopa in Rasmussen Subacute Encephalitis.

---

## Literature Evidence

Currently no related literature available for Levodopa in Rasmussen Subacute Encephalitis.

---

## EU Market Information

No EU marketing authorizations were retrieved for Levodopa in this evidence pack (0 records). This most likely represents a **data retrieval gap** rather than true market absence — levodopa-containing products (carbidopa/levodopa, levodopa/benserazide) are broadly authorised in EU member states for Parkinson's disease. Verification directly against the EMA public product database is recommended before drawing any regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Additional High-Evidence Predictions

The following table summarises evidence levels and recommendations across all 10 top-ranked TxGNN predictions. While Rasmussen encephalitis scores highest by model score, several lower-ranked predictions carry substantially stronger clinical evidence.

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Rasmussen Subacute Encephalitis | 99.06% | L5 | **Hold** |
| 2 | PLA2G6-Associated Neurodegeneration | 98.75% | L3 | **Proceed with Guardrails** |
| 3 | Myelitis | 98.47% | L4 | **Hold** |
| 4 | Transaldolase Deficiency | 98.20% | L5 | **Hold** |
| 5 | Paralysis Agitans, Juvenile (Hunt) | 98.03% | L3 | **Proceed with Guardrails** |
| 6 | Fructose-1,6-bisphosphatase Deficiency | 97.81% | L5 | **Hold** |
| 7 | Progressive Supranuclear Palsy-CBS | 97.58% | L3 | **Research Question** |
| 8 | Lewy Body Dementia | 97.25% | L3 | **Proceed with Guardrails** |
| 9 | Multiple System Atrophy, Parkinsonian Type | 97.02% | L3 | **Proceed with Guardrails** |
| 10 | X-linked ID-Ataxia-Apraxia Syndrome | 96.46% | L4 | **Research Question** |

---

### Rank 2 — PLA2G6-Associated Neurodegeneration (PLAN / PARK14)
**L3 · Proceed with Guardrails**

PLAN is an autosomal-recessive neurodegenerative disorder caused by *PLA2G6* mutations, most commonly presenting as early-onset dystonia-parkinsonism with basal ganglia iron accumulation. The pathological mechanism — nigrostriatal dopaminergic neurodegeneration — directly supports levodopa use. Multiple retrospective cohorts and case series document an initial motor response, though long-term efficacy wanes as post-synaptic receptor neurons are also progressively lost. No clinical trials were registered for this specific indication; all evidence is from publications.

**Literature Evidence**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34622992](https://pubmed.ncbi.nlm.nih.gov/34622992/) | 2022 | Retrospective Cohort | Movement Disorders | Complex parkinsonism is the predominant phenotype in late-onset PLAN; levodopa responsiveness documented in a subset |
| [32183746](https://pubmed.ncbi.nlm.nih.gov/32183746/) | 2020 | Case Series | BMC Neurology | Adult-onset PLAN: genotype-phenotype correlations in three patients; variable but present levodopa response |
| [39184971](https://pubmed.ncbi.nlm.nih.gov/39184971/) | 2024 | Multicenter Case Series | Tremor and Other Hyperkinetic Movements | Clinical-radiological-genetic spectrum of PLAN in Asian (Indian) cohort; treatment response characterised |
| [20669327](https://pubmed.ncbi.nlm.nih.gov/20669327/) | 2010 | Case Series | Movement Disorders | Early-onset L-dopa-responsive parkinsonism due to ATP13A2/PLA2G6/FBXO7/Spatacsin mutations |
| [18570303](https://pubmed.ncbi.nlm.nih.gov/18570303/) | 2009 | Phenotype-Genotype Characterization | Annals of Neurology | PLA2G6 as a locus for dystonia-parkinsonism; initial levodopa benefit observed in patients |
| [27268037](https://pubmed.ncbi.nlm.nih.gov/27268037/) | 2016 | Case Series | BMC Research Notes | PLA2G6 parkinsonism in two Saudi families; clinical heterogeneity and levodopa response noted |
| [32767480](https://pubmed.ncbi.nlm.nih.gov/32767480/) | 2020 | Case Series | Annals of Clinical and Translational Neurology | FBXO7 defect (NBIA-related) causes levodopa-responsive parkinsonian-pyramidal syndrome |
| [25197640](https://pubmed.ncbi.nlm.nih.gov/25197640/) | 2014 | Narrative Review | BioMed Research International | ATP13A2 and PLA2G6 mutations linked to PD susceptibility; dopaminergic mechanism discussed |
| [41769496](https://pubmed.ncbi.nlm.nih.gov/41769496/) | 2026 | Case Report | Cureus | Adult-onset PLA2G6 parkinsonism with claval hypertrophy; clinical features and imaging described |
| [3016582](https://pubmed.ncbi.nlm.nih.gov/3016582/) | 1986 | Review | Neuropathology and Applied Neurobiology | Lewy body disease and levodopa-responsive idiopathic Parkinson's disease — foundational review |

---

### Rank 5 — Paralysis Agitans, Juvenile, of Hunt (Juvenile Parkinson's Disease)
**L3 · Proceed with Guardrails**

"Hunt's juvenile paralysis agitans" is the historical nomenclature for juvenile-onset Parkinson's disease (YOPD, onset before age 40). Neuropathologically identical to adult PD — dopaminergic neurodegeneration in the substantia nigra — levodopa is the direct, mechanistically indicated therapy. Evidence level L3 is assigned on the basis of well-established clinical practice rather than specific published trials for this historical disease label. **Important caveat:** young-onset patients are significantly more prone to levodopa-induced dyskinesias and require lower starting doses with careful titration, always in combination with a DDC inhibitor. No clinical trials or publications were retrieved under this specific ICD label in the dataset.

---

### Rank 7 — Progressive Supranuclear Palsy-Corticobasal Syndrome (PSP-CBS)
**L3 · Research Question**

PSP-CBS is a 4R tauopathy causing degeneration of basal ganglia, brainstem, and frontal cortex. Post-synaptic dopamine D1/D2 receptors co-degenerate alongside pre-synaptic neurons, explaining why fewer than 30% of patients have a meaningful levodopa response. The primary clinical role of levodopa in PSP is as a **diagnostic challenge tool** to exclude levodopa-responsive Parkinson's disease, not as ongoing therapy. The large active trial NCT06949865 (n=2,000, recruiting) directly optimises acute levodopa challenge testing across atypical parkinsonisms including PSP.

**Key Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06949865](https://clinicaltrials.gov/study/NCT06949865) | N/A | Recruiting | 2,000 | Acute levodopa challenge test optimisation with AI and motion capture in PD and atypical parkinsonism including PSP |
| [NCT06836921](https://clinicaltrials.gov/study/NCT06836921) | N/A | Not Yet Recruiting | 30 | WECARE APD: multidisciplinary team visit impact on atypical Parkinsonian disorders (PSP/CBS/MSA) |
| [NCT04925622](https://clinicaltrials.gov/study/NCT04925622) | N/A | Completed | 90 | Complex eye movements in PD and PSP as diagnostic differentiation markers |

**Key Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31356287](https://pubmed.ncbi.nlm.nih.gov/31356287/) | 2019 | Review / Disease Overview | Continuum (Minneapolis) | PSP/CBD/MSA overview; levodopa typically non-responsive in PSP, used diagnostically |
| [30051337](https://pubmed.ncbi.nlm.nih.gov/30051337/) | 2018 | Review / Clinical Practice Guidelines | CNS Drugs | Therapeutic management of atypical parkinsonism including PSP-CBS; levodopa role as diagnostic trial |
| [38881158](https://pubmed.ncbi.nlm.nih.gov/38881158/) | 2024 | Case Series / Genetics | Movement Disorders Clinical Practice | GBA1 mutations in non-α-synuclein disorders; expanding atypical parkinsonism spectrum |

---

### Rank 8 — Lewy Body Dementia
**L3 · Proceed with Guardrails**

DLB and Parkinson's disease share α-synuclein pathology and nigrostriatal dopaminergic neurodegeneration, providing a direct mechanistic basis for levodopa to address motor symptoms. However, DLB patients have prominent cholinergic deficits and are at substantially higher risk of levodopa-induced neuropsychiatric complications — hallucinations, agitation, cognitive worsening. The DLB Consortium third report (PMID 16237129) and a systematic review/meta-analysis (PMID 26085043) provide Tier-1 consensus evidence supporting a **cautious, closely monitored levodopa trial** specifically for motor (parkinsonian) features.

**Key Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03305809](https://clinicaltrials.gov/study/NCT03305809) | Phase 2 | Completed | 344 | D1 receptor positive allosteric modulator LY3154207 in LBD — validates dopamine D1 pathway as therapeutic target |
| [NCT06949865](https://clinicaltrials.gov/study/NCT06949865) | N/A | Recruiting | 2,000 | Acute levodopa challenge test optimisation; includes DLB differential diagnosis |

**Key Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26085043](https://pubmed.ncbi.nlm.nih.gov/26085043/) | 2015 | Systematic Review / Meta-analysis | Am J Psychiatry | Pharmacological management of LBD; levodopa modestly effective for motor features, neuropsychiatric monitoring essential |
| [16237129](https://pubmed.ncbi.nlm.nih.gov/16237129/) | 2005 | Clinical Guidelines (DLB Consortium 3rd Report) | Neurology | Cautious levodopa trial recommended for parkinsonian motor symptoms; severe neuroleptic sensitivity warning |
| [19191343](https://pubmed.ncbi.nlm.nih.gov/19191343/) | 2009 | Observational Study | Movement Disorders | Direct study of levodopa effects on sleep and excessive daytime somnolence in DLB patients |
| [30680679](https://pubmed.ncbi.nlm.nih.gov/30680679/) | 2019 | Narrative Review | Drugs & Aging | DLB pharmacological management; levodopa role, hallucination risk, and dose guidance |
| [35619045](https://pubmed.ncbi.nlm.nih.gov/35619045/) | 2022 | Review / Drug Pipeline | Drugs & Aging | Current DLB therapies and development pipeline; levodopa as adjunct motor therapy with caveats |
| [21970305](https://pubmed.ncbi.nlm.nih.gov/21970305/) | 2011 | Review | Drugs & Aging | Treatment of DLB and PDD; six-month RCT evidence for rivastigmine as primary therapy; levodopa as secondary motor adjunct |
| [14594099](https://pubmed.ncbi.nlm.nih.gov/14594099/) | 2003 | Review / Clinical Practice | Can Fam Physician | DLB pharmacological management guide for clinicians; levodopa and medications to avoid |
| [31177296](https://pubmed.ncbi.nlm.nih.gov/31177296/) | 2019 | Observational Study | Exp Brain Research | Quantitative upper limb movement analysis in DLB; mild asymmetrical parkinsonism only mildly responsive to levodopa |
| [38333295](https://pubmed.ncbi.nlm.nih.gov/38333295/) | 2024 | Scoping Review | Ann Med Surg | Insights into LBD management; levodopa among pharmacological options reviewed |
| [36402160](https://pubmed.ncbi.nlm.nih.gov/36402160/) | 2022 | Phase 3 RCT | Lancet Neurology | Foslevodopa-foscarbidopa Phase 3 in advanced PD; continuous levodopa delivery reduces OFF time — mechanism applicable to PDD spectrum |

---

### Rank 9 — Multiple System Atrophy, Parkinsonian Type (MSA-P)
**L3 · Proceed with Guardrails**

MSA-P involves α-synuclein accumulation in oligodendrocytes causing striatonigral and olivopontocerebellar degeneration. Unlike idiopathic PD, both pre- and post-synaptic striatal elements degenerate — explaining the typically poor or transient levodopa response. Approximately 30% of MSA-P patients show an initial moderate response (PMID 7922469, n=100). PMID 39072635 (2024) provides direct evidence of levodopa normalising autonomic sympathetic skin responses in an MSA-P patient. Guidelines recommend a high-dose levodopa trial (≥1,000 mg/day) as first-line symptomatic attempt. The actively recruiting CARBIDOH trial (NCT06831500, Phase 1/2) directly investigates the carbidopa/levodopa ratio in MSA-P.

**Key Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06831500](https://clinicaltrials.gov/study/NCT06831500) | Phase 1/2 | Recruiting | 36 | CARBIDOH: Carbidopa/levodopa ratio effect on orthostatic hypotension in MSA-P and PD — direct levodopa intervention |
| [NCT06836921](https://clinicaltrials.gov/study/NCT06836921) | N/A | Not Yet Recruiting | 30 | WECARE APD: Multidisciplinary management of atypical parkinsonism including MSA |

**Key Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39072635](https://pubmed.ncbi.nlm.nih.gov/39072635/) | 2024 | Case Report | Neurocase | **Direct evidence**: Levodopa normalised sympathetic skin responses and improved orthostatic hypotension in MSA-P |
| [7922469](https://pubmed.ncbi.nlm.nih.gov/7922469/) | 1994 | Retrospective Cohort (n=100) | Brain | Natural history of MSA; ~30% demonstrated initial levodopa response, typically declining over 1–2 years |
| [34776506](https://pubmed.ncbi.nlm.nih.gov/34776506/) | 2021 | Case Report | Am J Case Reports | Video documentation of dopamine-responsive MSA cerebellar subtype; significant carbidopa/levodopa benefit |
| [27787721](https://pubmed.ncbi.nlm.nih.gov/27787721/) | 2016 | Review | Current Treatment Options in Neurology | Current MSA treatment; levodopa recommended as first-line symptomatic trial at adequate doses |
| [17534959](https://pubmed.ncbi.nlm.nih.gov/17534959/) | 2007 | Literature Review | Movement Disorders | Levodopa responsiveness across parkinsonian disorders; higher initial response rates in MSA than expected |
| [24615754](https://pubmed.ncbi.nlm.nih.gov/24615754/) | 2014 | Review | Movement Disorders | MSA clinical state of the art; poorly levodopa-responsive parkinsonism as defining feature, with minority exceptions |
| [41790245](https://pubmed.ncbi.nlm.nih.gov/41790245/) | 2026 | Cohort Study / Biomarker | J Neurology | Balance biomarkers for early PD vs. MSA-P differentiation; levodopa response as key differential criterion |

---

### Rank 10 — X-linked Intellectual Disability-Ataxia-Apraxia Syndrome
**L4 · Research Question**

This heterogeneous disease category encompasses multiple X-linked neurodevelopmental disorders. Two recent publications provide direct levodopa evidence: PMID 41144879 (2026) documents altered dopamine metabolism and levodopa/carbidopa treatment response in MCT8 deficiency (Allan-Herndon-Dudley syndrome), where thyroid hormone transport impairment disrupts dopaminergic circuit maturation. PMID 40088079 (2025) describes parkinsonian symptomatology in MCT8-deficient children responding to levodopa. Additionally, RAB39B-related X-linked parkinsonism with intellectual disability (PMID 41074240) reports subcutaneous L-DOPA infusion use. Evidence is limited to recent case reports and requires genetic subtyping before any clinical application.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41144879](https://pubmed.ncbi.nlm.nih.gov/41144879/) | 2026 | Case Report / Treatment Response | Movement Disorders | **Direct evidence**: Altered dopamine metabolism and levodopa/carbidopa response in MCT8 deficiency (AHDS) |
| [40088079](https://pubmed.ncbi.nlm.nih.gov/40088079/) | 2025 | Case Series | Movement Disorders | MCT8-deficient patients display childhood parkinsonism and respond to levodopa/carbidopa |
| [41074240](https://pubmed.ncbi.nlm.nih.gov/41074240/) | 2026 | Case Report | Ann Clin Transl Neurology | RAB39B-related X-linked parkinsonism with intellectual disability treated with subcutaneous L-DOPA infusion |
| [40767387](https://pubmed.ncbi.nlm.nih.gov/40767387/) | 2025 | Case Report | Am J Med Genet A | MSL3/Basilicata-Akhtar syndrome with motor disturbances; 30-year follow-up case |

---

## Conclusion and Next Steps

**Decision: Hold** (Rasmussen Subacute Encephalitis — Primary Prediction)

**Rationale:**
The top-ranked TxGNN prediction has no mechanistic basis, zero clinical trials, and no supporting publications (L5). The score reflects knowledge-graph topology artefacts in the neurodegeneration domain, not a clinically actionable repurposing hypothesis.

**To advance Rasmussen encephalitis as a candidate, the following is needed:**
- At minimum, a case report or hypothesis-generating preclinical study establishing a link between Rasmussen encephalitis pathology and dopamine pathway dysfunction
- MOA data retrieval from DrugBank (currently Data Gap)
- Full safety profile from EU SmPC (currently Data Gap for warnings and contraindications)

---

**Prioritise instead — the following four secondary predictions should each receive independent evaluation:**

| Priority | Indication | Evidence Level | Rationale |
|---------|-----------|----------------|-----------|
| 1 | **Lewy Body Dementia** | L3 | Tier-1 systematic review + DLB Consortium guidelines support conditional motor use; active trials |
| 2 | **MSA, Parkinsonian Type** | L3 | Direct case evidence (2024); active Phase 1/2 CARBIDOH trial; ~30% initial response rate in n=100 cohort |
| 3 | **PLA2G6-Associated Neurodegeneration** | L3 | Retrospective cohort + multiple case series; direct mechanistic link via nigrostriatal degeneration |
| 4 | **Paralysis Agitans, Juvenile (Hunt)** | L3 | Juvenile-onset PD: direct levodopa indication; highest dyskinesia risk requires special monitoring |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

