# Deep Morphology Alignment Report

This report audits the current manuscript at sentence level. It does not rewrite the manuscript.

## Summary

- Sentence records: 292.
- Sentences with mismatch or jump relation: 110.

## Highest-Priority Sentence Records

### ABS.S2

Text: This paper reports a two-board Zynq-7020 {} case study showing that this boundary can be insufficient: sampler-side physical implementation can substantially reshape measured restart behavior.

- Dominant function: `GAP`
- Expected top-venue role: `PROBLEM`
- Previous relation: `jumps`
- Claim type/strength: `method` / `medium`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=3; colon_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### ABS.S3

Text: Continuous-stream placement measurements on the primary board expose a large implementation dependence, from a biased placement with $p_1=0.337316$ and bit min-entropy 0.593606 to a near-balanced placement with $p_1=0.499969$ and bit min-entropy 0.999909.

- Dominant function: `SETUP`
- Expected top-venue role: `GAP`
- Previous relation: `elaborates`
- Claim type/strength: `method` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `large`
- Punctuation: `hyphen_count=4; comma_count=1`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### ABS.S7

Text: Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- Dominant function: `RESULT`
- Expected top-venue role: `BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `medium`
- Evidence anchor: `None`
- Risk words: `small`
- Punctuation: `OK`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### ABS.S8

Text: Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show that final all64 output can hide biased internal sampler-vector directions: on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718 while internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- Dominant function: `GAP`
- Expected top-venue role: `BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `causal/generalization` / `medium`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=10; colon_count=1; slash_count=1; comma_count=5`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P1.S3

Text: Placement, routing, clocking, reset sequencing, sampling, and readout can all affect the final bitstream.

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `causal/generalization` / `medium`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `comma_count=5`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P1.S5

Text: It is also where the physical entropy-source boundary should be drawn.

- Dominant function: `BG`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P3.S2

Text: That abstraction is useful for design, but it can fail as a measurement boundary.

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `method` / `medium`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P3.S3

Text: In the measurements reported here, a placement that is near balanced in a continuous stream still shows warmup-dependent fixed-position restart bias.

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `medium`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=2; comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P3.S4

Text: More importantly, small locked changes to the sample-RO physical implementation move restart behavior in both directions: a compact sampler configuration becomes biased when a restart-oriented sample-RO lock is imposed, and the baseline restart configuration is restored near balance when the compact sample-RO lock is imposed.

- Dominant function: `BG`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `elaborates`
- Claim type/strength: `causal/generalization` / `low`
- Evidence anchor: `None`
- Risk words: `small`
- Punctuation: `hyphen_count=4; colon_count=1; comma_count=2`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### INTRODUCTION.P4.S1

Text: {quote} When an FPGA {} is evaluated from hardware measurements, must the sampler-side physical implementation be included in the measured entropy-source boundary? {quote}

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `none`
- Claim type/strength: `method` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=2; question_mark_count=1; comma_count=1`
- Mismatch: `punctuation_issue`
- Revision operation: `CHANGE_PUNCTUATION`

### INTRODUCTION.P5.S2

Text: The claim is not that all FPGA {}s behave identically, nor that the present evidence is a complete {} validation package.

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `method` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P6.S4

Text: A {}-assisted diagnostic layer that constrains a simple persistent pairwise hard-locking explanation under the measured conditions.

- Dominant function: `RESULT`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=2`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P6.S5

Text: A reduced-XOR counterfactual analysis showing same-data-RO direction anisotropy, warmup-dependent complement cancellation, line-direction controls, second-board original and held-out sampler mechanism checks, and a minimal toolflow/directive sensitivity matrix. {enumerate}

- Dominant function: `BG`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `comparative` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=7; slash_count=1; comma_count=4`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P7.S2

Text: Section II summarizes related work and the measurement gap.

- Dominant function: `GAP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `OK`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P7.S5

Text: Sections V--IX present continuous-stream placement, restart, sampler-side counterfactual, {}, and reduced-XOR evidence.

- Dominant function: `SETUP`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `comparative` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=4; comma_count=4`
- Mismatch: `none`
- Revision operation: `KEEP`

### INTRODUCTION.P7.S6

Text: Section X discusses the entropy-source boundary, Section XI lists limitations and future measurements, and Section XII concludes.

- Dominant function: `BOUNDARY`
- Expected top-venue role: `BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=2`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S3

Text: Evaluation may include output statistics, entropy estimates, restart behavior, health-test boundaries, and conditioning documentation [Turan_2018,Lubicz_2015,Lubicz_2024].

- Dominant function: `BG`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `limitation` / `medium`
- Evidence anchor: `Citation`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=6`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S4

Text: Prior work further shows that oscillator-based generators can be sensitive to implementation and environmental conditions, including security-relevant perturbations [Markettos_2009,Fischer_2008].

- Dominant function: `RESULT`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `method` / `medium`
- Evidence anchor: `Citation`
- Risk words: `None`
- Punctuation: `hyphen_count=2; comma_count=2`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S2

Text: Compact multi-RO, RO-PUF/TRNG, and DCM/metastability designs report area, throughput, portability, and platform tradeoffs, and some explicitly evaluate place-and-route dependence as part of the hardware study [Nannipieri_2021,RojasMunoz_2022,Frustaci_2023].

- Dominant function: `SETUP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `method` / `low`
- Evidence anchor: `Citation;Experiment setup`
- Risk words: `some`
- Punctuation: `hyphen_count=4; slash_count=2; comma_count=8`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S3

Text: These works motivate careful reporting of FPGA implementation details, but they do not replace a project-specific boundary diagnosis for the particular sampler, restart protocol, and routed implementation studied here.

- Dominant function: `SETUP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `method` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=3`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S2

Text: They do not, by themselves, close the implementation-level measurement gap addressed here.

- Dominant function: `GAP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `method` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=2`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S5

Text: Restart-style measurements sharpen the problem because they compare fixed positions across repeated starts and can expose startup-position effects that disappear in aggregate continuous streams [Turan_2018].

- Dominant function: `INTERPRETATION`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `medium`
- Evidence anchor: `Citation;Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=2`
- Mismatch: `none`
- Revision operation: `KEEP`

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S2

Text: FPGA {}s have a substantial instrumentation literature [Jian_Song_2006,Wu_2009,Wu_2012,Wang_2017], but raw bins are not automatically linear timing measurements.

- Dominant function: `SETUP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `elaborates`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Citation;Experiment setup`
- Risk words: `substantial`
- Punctuation: `comma_count=4`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S3

Text: In this work, {} data are used conservatively: they help test mechanism explanations, especially persistent pairwise hard locking, but they are not used as calibrated picosecond-level jitter metrology.

- Dominant function: `BG`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; colon_count=1; comma_count=3`
- Mismatch: `none`
- Revision operation: `KEEP`

### DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S2

Text: The core entropy RTL contains eight data ROs, a nine-stage sample RO, sampled-data registers, and a final XOR reduction.

- Dominant function: `BG`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=2; comma_count=3`
- Mismatch: `none`
- Revision operation: `KEEP`

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S4

Text: It includes the data ROs, sample RO, sampled-data registers, sampler-side routing and local implementation, and the restart/warmup/reset timing that directly affects when early samples are taken.

- Dominant function: `SETUP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `causal/generalization` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=2; slash_count=2; comma_count=4`
- Mismatch: `none`
- Revision operation: `KEEP`

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S5

Text: FIFO buffering after entropy-bit formation, UART readout, host capture, and offline analysis are outside the entropy source, but they are part of the measurement chain and must be documented for reproducibility.

- Dominant function: `SETUP`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=4`
- Mismatch: `none`
- Revision operation: `KEEP`

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S2

Text: It is not used as a complete {} validation.

- Dominant function: `BG`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `OK`
- Mismatch: `none`
- Revision operation: `KEEP`

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S3

Text: The 1000-row restart body follows the restart input shape used by the local {ea\_restart} flow, not an argument that 1000 rows alone is sufficient for certification.

- Dominant function: `BG`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S4

Text: Table tab:warmup reports the cutoff, maximum count, and resulting diagnostic outcome to keep the table compact; the diagnostic still inspects many fixed positions jointly and is not a collection of independent single-position claims.

- Dominant function: `RESULT`
- Expected top-venue role: `SECTION_SPECIFIC`
- Previous relation: `evidences`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Table`
- Risk words: `many`
- Punctuation: `hyphen_count=1; semicolon_count=1; colon_count=1; comma_count=2`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S2

Text: The contrast between {} and {} is the simplest entry point.

- Dominant function: `BG`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `OK`
- Mismatch: `none`
- Revision operation: `KEEP`

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S3

Text: In the 10 MiB rows, {} has $p_1=0.337316$, absolute bias 0.162684, and bit min-entropy 0.593606.

- Dominant function: `BG`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=3`
- Mismatch: `none`
- Revision operation: `KEEP`

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S2

Text: The same-column placement is near balanced by $p_1$ and bit min-entropy, but its adjacent-equal ratio differs from the strongest placements.

- Dominant function: `SETUP`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=3; comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S3

Text: This motivates the restart and mechanism measurements: a single continuous-stream statistic cannot define the physical entropy-source boundary.

- Dominant function: `NEED`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=2; colon_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4.S2

Text: The summarized measurements report a maximum 10 MiB/repeat bit-min-entropy mean delta of 0.00841786 among paired placement rows.

- Dominant function: `SETUP`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `Experiment setup`
- Risk words: `None`
- Punctuation: `hyphen_count=2; slash_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`

### RESTART_AND_WARMUP_CHARACTERIZATION.P4.S3

Text: Repeated warmup scans place the observed transition at $10 < {WARMUP\_BYTES} 11$, with warmup 11 still a boundary observation rather than a large-margin engineering rule.

- Dominant function: `RESULT`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `elaborates`
- Claim type/strength: `measurement` / `low`
- Evidence anchor: `None`
- Risk words: `large`
- Punctuation: `hyphen_count=1; comma_count=1`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### RESTART_AND_WARMUP_CHARACTERIZATION.P6.S3

Text: The repeated warmup-10 flagged outcomes and warmup-11 no-flag outcomes support a narrow measured transition, but they should not be generalized as a universal warmup threshold across boards, placements, PVT conditions, or tool runs.

- Dominant function: `RESULT`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `measurement` / `very_high`
- Evidence anchor: `None`
- Risk words: `universal`
- Punctuation: `hyphen_count=3; comma_count=4`
- Mismatch: `unsupported_claim;overstrong_claim;risk_word`
- Revision operation: `ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB`

### SAMPLER_SIDE_COUNTERFACTUALS.P4.S2

Text: Each row summarizes three 1000-row restart artifacts on the same second board; these are capture repeats under the listed condition, not additional boards or PVT points.} tab:board2counter {tabular}{llrrrrrl} Condition & Warmup & $n$ & Mean $p_1$ & Std. $p_1$ & Min.

- Dominant function: `BOUNDARY`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `limitation` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; semicolon_count=1; colon_count=1; comma_count=1`
- Mismatch: `none`
- Revision operation: `ADD_BOUNDARY`

### SAMPLER_SIDE_COUNTERFACTUALS.P4.S3

Text: Min-H & Max worst $x$ & Reading \\ {} compact baseline & 4 & 3 & 0.494077 & 0.000501 & 0.981366 & 556 & compact reference \\ {} compact baseline & 5 & 3 & 0.522394 & 0.001229 & 0.933152 & 576 & compact reference, high-side \\ {} compact baseline & 11 & 3 & 0.490700 & 0.000272 & 0.972532 & 562 & compact reference \\ {} forward lock & 4 & 3 & 0.450792 & 0.001106 & 0.861432 & 719 & repeated biased shift \\ {} forward lock & 5 & 3 & 0.445222 & 0.000603 & 0.848214 & 666 & repeated biased shift \\ {} forward lock & 11 & 3 & 0.411363 & 0.000294 & 0.763719 & 663 & stronger biased shift \\ {} reverse lock & 4 & 3 & 0.498300 & 0.000544 & 0.993649 & 573 & reverse near balance \\ {tabular} {table*}

- Dominant function: `RESULT`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `evidences`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `high`
- Punctuation: `hyphen_count=2; comma_count=1`
- Mismatch: `risk_word`
- Revision operation: `REPLACE_RISK_VERB`

### SAMPLER_SIDE_COUNTERFACTUALS.P6.S3

Text: At warmup 4, changing from the compact {} reference to the forward {} lock moves the mean $p_1$ from 0.494077 to 0.450792 and raises the maximum worst fixed-position count from 556 to 719.

- Dominant function: `BG`
- Expected top-venue role: `QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- Previous relation: `jumps`
- Claim type/strength: `descriptive` / `low`
- Evidence anchor: `None`
- Risk words: `None`
- Punctuation: `hyphen_count=1; comma_count=1`
- Mismatch: `none`
- Revision operation: `KEEP`
