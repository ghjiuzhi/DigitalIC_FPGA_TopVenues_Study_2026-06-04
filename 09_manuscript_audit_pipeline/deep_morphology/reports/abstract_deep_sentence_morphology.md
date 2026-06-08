# Abstract Deep Sentence Morphology

Target sequence: `BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`.

Current sequence: `SETUP -> GAP -> SETUP -> RESULT -> BG -> BG -> RESULT -> GAP -> RESULT`.

## ABS.S1

Text: FPGA ring-oscillator true random number generators are commonly evaluated from oscillator-array structure and final output statistics.

- Function: `SETUP`
- Expected role: `BG`
- Claim: `method` / `low`
- Evidence: `None`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S2

Text: This paper reports a two-board Zynq-7020 {} case study showing that this boundary can be insufficient: sampler-side physical implementation can substantially reshape measured restart behavior.

- Function: `GAP`
- Expected role: `PROBLEM`
- Claim: `method` / `medium`
- Evidence: `None`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S3

Text: Continuous-stream placement measurements on the primary board expose a large implementation dependence, from a biased placement with $p_1=0.337316$ and bit min-entropy 0.593606 to a near-balanced placement with $p_1=0.499969$ and bit min-entropy 0.999909.

- Function: `SETUP`
- Expected role: `GAP`
- Claim: `method` / `low`
- Evidence: `Experiment setup`
- Risk words: `large`
- Operation: `REPLACE_RISK_VERB`

## ABS.S4

Text: Restart measurements then show that continuous-stream balance is not enough: warmup bytes 8 and 10 trigger fixed-position diagnostic flags, while warmup bytes 11, 12, and 16 do not.

- Function: `RESULT`
- Expected role: `METHOD`
- Claim: `measurement` / `medium`
- Evidence: `Experiment setup`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S5

Text: The central evidence is a bidirectional sampler-side counterfactual on the primary board, plus a repeated second-board check: imposing the restart-oriented sample-RO lock changes a compact sampler configuration toward biased restart behavior on both boards, with board-specific magnitudes.

- Function: `BG`
- Expected role: `SETUP`
- Claim: `causal/generalization` / `low`
- Evidence: `None`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S6

Text: On the second board, three-run forward warmup-4 and warmup-5 means are $p_1=0.450792$ and 0.445222, while the reverse compact-lock warmup-4 mean is 0.498300.

- Function: `BG`
- Expected role: `RESULT`
- Claim: `descriptive` / `low`
- Evidence: `None`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S7

Text: Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- Function: `RESULT`
- Expected role: `BOUNDARY`
- Claim: `measurement` / `medium`
- Evidence: `None`
- Risk words: `small`
- Operation: `REPLACE_RISK_VERB`

## ABS.S8

Text: Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show that final all64 output can hide biased internal sampler-vector directions: on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718 while internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- Function: `GAP`
- Expected role: `BOUNDARY`
- Claim: `causal/generalization` / `medium`
- Evidence: `None`
- Risk words: `None`
- Operation: `KEEP`

## ABS.S9

Text: These measurements support a diagnostic claim rather than a certification claim: sampler-side physical implementation is not passive readout in the evaluated implementations and should be included in the measured entropy-source boundary.

- Function: `RESULT`
- Expected role: `BOUNDARY`
- Claim: `method` / `medium`
- Evidence: `Experiment setup`
- Risk words: `None`
- Operation: `KEEP`

## Revised Function Plan Before Rewriting

`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`.
