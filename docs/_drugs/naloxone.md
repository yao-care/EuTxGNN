---
layout: default
title: Naloxone
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Naloxone
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

Using no specialized skill — this is a direct content-generation task with an explicit, fully-specified output template, so I'll follow it literally against the given Evidence Pack.

# Naloxone: From Opioid Overdose Reversal to Continuous Spikes and Waves During Sleep

## One-Sentence Summary

Naloxone is a competitive opioid receptor antagonist, established as the standard emergency treatment for opioid overdose and opioid-induced respiratory depression.
The TxGNN model predicts it may be effective for **Continuous Spikes and Waves During Sleep (CSWS)**, a rare pediatric epileptic encephalopathy,
but currently **0 clinical trials** and **0 publications** support this specific direction — this is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid overdose / opioid-induced respiratory depression (not present in this Evidence Pack's regulatory records — see data gaps below) |
| Predicted New Indication | Continuous spikes and waves during sleep |
| TxGNN Prediction Score | 88.17% (absolute rank 81,482) |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, Naloxone is a non-selective opioid receptor (mu, kappa, delta) antagonist, whose clinical utility is well established in reversing opioid-induced CNS and respiratory depression. Whether this receptor antagonism has any bearing on the pathophysiology of continuous spikes and waves during sleep (CSWS, also known as ESES — Electrical Status Epilepticus during Slow-wave Sleep) is not addressed in the available evidence.

CSWS is a childhood epileptic encephalopathy driven by disrupted GABAergic/thalamocortical network activity during sleep, a mechanism domain that does not overlap in any documented way with opioid receptor pharmacology. Unlike other predictions in this evidence pack (e.g., naloxone/naltrexone in psychotic disorders, tardive dyskinesia, or hypoglycemia counterregulation, which are backed by decades of opioid-system-related literature), the CSWS prediction has **no supporting clinical trial or literature evidence** at all in the pack. This should be treated as a pure knowledge-graph signal until an independent mechanistic or clinical rationale is found.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but this specific drug–disease pair has zero corroborating clinical trials or literature, and no plausible mechanistic link between opioid receptor antagonism and CSWS is documented. This is an L5, model-only signal and does not meet the bar to advance.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications — currently Blocking safety review) via TFDA label PDF retrieval
- Resolve DG002 (Naloxone MOA detail) via DrugBank API query
- Targeted literature/clinical search specifically on opioid antagonists in pediatric epileptic encephalopathies (CSWS/ESES) to confirm or rule out a mechanistic rationale
- Confirm actual original indication and regulatory licensing status for Naloxone (regulatory record in this pack shows 0 licenses / Not Marketed, which is inconsistent with Naloxone's known global approval status and should be re-verified)
- Consider reprioritizing evaluation toward the same evidence pack's higher-evidence candidates for Naloxone (e.g., **psychotic disorder** — 11 trials/22 publications, **hypoglycemia** — 7 trials/22 publications, **schizophreniform disorder** — 1 trial/22 publications), which show substantially stronger mechanistic and clinical support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

