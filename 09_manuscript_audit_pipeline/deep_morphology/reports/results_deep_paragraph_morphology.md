# Results Deep Paragraph Morphology

Target paragraph sequence: `QUESTION -> FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY`.

## PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1

- Paragraph role: `main result`
- Current sequence: `SETUP -> BG -> BG -> BG`

- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S1` SETUP | evidence `Table` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S2` BG | evidence `None` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S3` BG | evidence `None` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S4` BG | evidence `None` | operation `KEEP`

## PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2

- Paragraph role: `main result`
- Current sequence: `GAP -> SETUP -> NEED`

- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S1` GAP | evidence `None` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S2` SETUP | evidence `None` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S3` NEED | evidence `Experiment setup` | operation `KEEP`

## PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P3

- Paragraph role: `main result`
- Current sequence: `SETUP -> SETUP`

- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P3.S1` SETUP | evidence `Citation` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P3.S2` SETUP | evidence `Experiment setup` | operation `KEEP`

## PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4

- Paragraph role: `main result`
- Current sequence: `SETUP -> SETUP -> SETUP`

- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4.S1` SETUP | evidence `None` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4.S2` SETUP | evidence `Experiment setup` | operation `KEEP`
- `PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4.S3` SETUP | evidence `Experiment setup` | operation `KEEP`

## RESTART_AND_WARMUP_CHARACTERIZATION.P1

- Paragraph role: `main result`
- Current sequence: `BG`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P1.S1` BG | evidence `None` | operation `KEEP`

## RESTART_AND_WARMUP_CHARACTERIZATION.P2

- Paragraph role: `main result`
- Current sequence: `RESULT -> BG -> NEED`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P2.S1` RESULT | evidence `Table` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P2.S2` BG | evidence `Experiment setup` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P2.S3` NEED | evidence `Experiment setup` | operation `KEEP`

## RESTART_AND_WARMUP_CHARACTERIZATION.P3

- Paragraph role: `main result`
- Current sequence: `RESULT`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P3.S1` RESULT | evidence `Citation` | operation `KEEP`

## RESTART_AND_WARMUP_CHARACTERIZATION.P4

- Paragraph role: `main result`
- Current sequence: `RESULT -> SETUP -> RESULT`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P4.S1` RESULT | evidence `Table` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P4.S2` SETUP | evidence `None` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P4.S3` RESULT | evidence `None` | operation `REPLACE_RISK_VERB`

## RESTART_AND_WARMUP_CHARACTERIZATION.P5

- Paragraph role: `main result`
- Current sequence: `RESULT`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P5.S1` RESULT | evidence `Citation` | operation `KEEP`

## RESTART_AND_WARMUP_CHARACTERIZATION.P6

- Paragraph role: `main result`
- Current sequence: `GAP -> SETUP -> RESULT`

- `RESTART_AND_WARMUP_CHARACTERIZATION.P6.S1` GAP | evidence `None` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P6.S2` SETUP | evidence `Experiment setup` | operation `KEEP`
- `RESTART_AND_WARMUP_CHARACTERIZATION.P6.S3` RESULT | evidence `None` | operation `ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB`

## SAMPLER_SIDE_COUNTERFACTUALS.P1

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> BG -> SETUP -> SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P1.S1` RESULT | evidence `Table` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P1.S2` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P1.S3` BG | evidence `Experiment setup` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P1.S4` SETUP | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P1.S5` SETUP | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P2

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P2.S1` RESULT | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P2.S2` SETUP | evidence `Experiment setup` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P3

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> RESULT -> BG -> RESULT`

- `SAMPLER_SIDE_COUNTERFACTUALS.P3.S1` RESULT | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P3.S2` RESULT | evidence `Table;Experiment setup` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P3.S3` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P3.S4` RESULT | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P4

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BOUNDARY -> RESULT`

- `SAMPLER_SIDE_COUNTERFACTUALS.P4.S1` RESULT | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P4.S2` BOUNDARY | evidence `None` | operation `ADD_BOUNDARY`
- `SAMPLER_SIDE_COUNTERFACTUALS.P4.S3` RESULT | evidence `None` | operation `REPLACE_RISK_VERB`

## SAMPLER_SIDE_COUNTERFACTUALS.P5

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> RESULT -> RESULT -> GAP -> BG`

- `SAMPLER_SIDE_COUNTERFACTUALS.P5.S1` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P5.S2` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P5.S3` RESULT | evidence `Table` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P5.S4` GAP | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P5.S5` BG | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P6

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BOUNDARY -> BG -> BG -> BG -> BG -> BG`

- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S1` RESULT | evidence `Table` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S2` BOUNDARY | evidence `None` | operation `ADD_BOUNDARY`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S3` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S4` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S5` BG | evidence `None` | operation `ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S6` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P6.S7` BG | evidence `Experiment setup` | operation `WEAKEN_CLAIM;REPLACE_RISK_VERB`

## SAMPLER_SIDE_COUNTERFACTUALS.P7

- Paragraph role: `counterfactual`
- Current sequence: `BG -> NEED -> RESULT -> NEED`

- `SAMPLER_SIDE_COUNTERFACTUALS.P7.S1` BG | evidence `Experiment setup` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P7.S2` NEED | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P7.S3` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P7.S4` NEED | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P8

- Paragraph role: `counterfactual`
- Current sequence: `BG -> BG -> RESULT`

- `SAMPLER_SIDE_COUNTERFACTUALS.P8.S1` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P8.S2` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P8.S3` RESULT | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P9

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> SETUP -> BG -> SETUP -> RESULT`

- `SAMPLER_SIDE_COUNTERFACTUALS.P9.S1` RESULT | evidence `Table;Experiment setup` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P9.S2` SETUP | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P9.S3` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P9.S4` SETUP | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P9.S5` RESULT | evidence `None` | operation `REPLACE_RISK_VERB`

## SAMPLER_SIDE_COUNTERFACTUALS.P10

- Paragraph role: `counterfactual`
- Current sequence: `SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P10.S1` SETUP | evidence `Citation;Experiment setup` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P11

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> BG -> BG -> RESULT -> SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S1` RESULT | evidence `Table` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S2` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S3` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S4` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S5` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P11.S6` SETUP | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P12

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P12.S1` RESULT | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P12.S2` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P12.S3` SETUP | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P13

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> SETUP -> BG -> RESULT -> GAP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S1` RESULT | evidence `Figure` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S2` BG | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S3` SETUP | evidence `Table` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S4` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S5` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P13.S6` GAP | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P14

- Paragraph role: `counterfactual`
- Current sequence: `BG -> RESULT -> BG -> SETUP -> BG`

- `SAMPLER_SIDE_COUNTERFACTUALS.P14.S1` BG | evidence `None` | operation `REPLACE_RISK_VERB`
- `SAMPLER_SIDE_COUNTERFACTUALS.P14.S2` RESULT | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P14.S3` BG | evidence `None` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P14.S4` SETUP | evidence `Experiment setup` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P14.S5` BG | evidence `None` | operation `KEEP`

## SAMPLER_SIDE_COUNTERFACTUALS.P15

- Paragraph role: `counterfactual`
- Current sequence: `SETUP -> SETUP`

- `SAMPLER_SIDE_COUNTERFACTUALS.P15.S1` SETUP | evidence `Citation` | operation `KEEP`
- `SAMPLER_SIDE_COUNTERFACTUALS.P15.S2` SETUP | evidence `None` | operation `KEEP`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1

- Paragraph role: `mechanism diagnosis`
- Current sequence: `BG -> RESULT -> BOUNDARY -> BOUNDARY -> BG -> BG -> BG`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S1` BG | evidence `None` | operation `ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S2` RESULT | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S3` BOUNDARY | evidence `Experiment setup` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S4` BOUNDARY | evidence `None` | operation `ADD_BOUNDARY`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S5` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S6` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P1.S7` BG | evidence `None` | operation `REPLACE_RISK_VERB`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P2

- Paragraph role: `mechanism diagnosis`
- Current sequence: `RESULT -> SETUP -> RESULT -> BG`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P2.S1` RESULT | evidence `Table` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P2.S2` SETUP | evidence `Experiment setup` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P2.S3` RESULT | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P2.S4` BG | evidence `None` | operation `KEEP`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P3

- Paragraph role: `mechanism diagnosis`
- Current sequence: `RESULT -> SETUP`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P3.S1` RESULT | evidence `Citation` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P3.S2` SETUP | evidence `Table` | operation `KEEP`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4

- Paragraph role: `mechanism diagnosis`
- Current sequence: `BG -> RESULT -> BG -> BOUNDARY -> BOUNDARY -> RESULT`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S1` BG | evidence `None` | operation `REPLACE_RISK_VERB`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S2` RESULT | evidence `Table` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S3` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S4` BOUNDARY | evidence `None` | operation `ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB;ADD_BOUNDARY`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S5` BOUNDARY | evidence `None` | operation `REPLACE_RISK_VERB;ADD_BOUNDARY`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P4.S6` RESULT | evidence `Experiment setup` | operation `KEEP`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5

- Paragraph role: `mechanism diagnosis`
- Current sequence: `BG -> BG -> RESULT -> RESULT`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5.S1` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5.S2` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5.S3` RESULT | evidence `Table` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5.S4` RESULT | evidence `None` | operation `REPLACE_RISK_VERB`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P6

- Paragraph role: `mechanism diagnosis`
- Current sequence: `RESULT -> BG -> RESULT`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P6.S1` RESULT | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P6.S2` BG | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P6.S3` RESULT | evidence `None` | operation `KEEP`

## TDC_ASSISTED_MECHANISM_DIAGNOSIS.P7

- Paragraph role: `mechanism diagnosis`
- Current sequence: `RESULT -> BG`

- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P7.S1` RESULT | evidence `None` | operation `KEEP`
- `TDC_ASSISTED_MECHANISM_DIAGNOSIS.P7.S2` BG | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P1

- Paragraph role: `counterfactual`
- Current sequence: `SETUP -> RESULT -> BG -> RESULT -> BG -> BG -> GAP`

- `REDUCED_XOR_COUNTERFACTUALS.P1.S1` SETUP | evidence `Citation;Experiment setup` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S2` RESULT | evidence `Figure` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S3` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S4` RESULT | evidence `Table` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S5` BG | evidence `None` | operation `REPLACE_RISK_VERB`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S6` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P1.S7` GAP | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P2

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> SETUP`

- `REDUCED_XOR_COUNTERFACTUALS.P2.S1` RESULT | evidence `Citation` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P2.S2` SETUP | evidence `Experiment setup` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P3

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> RESULT`

- `REDUCED_XOR_COUNTERFACTUALS.P3.S1` RESULT | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P3.S2` RESULT | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P4

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> RESULT`

- `REDUCED_XOR_COUNTERFACTUALS.P4.S1` RESULT | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P4.S2` RESULT | evidence `None` | operation `REPLACE_RISK_VERB`

## REDUCED_XOR_COUNTERFACTUALS.P5

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> RESULT`

- `REDUCED_XOR_COUNTERFACTUALS.P5.S1` RESULT | evidence `Citation` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P5.S2` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P5.S3` RESULT | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P6

- Paragraph role: `counterfactual`
- Current sequence: `RESULT -> BG -> RESULT -> GAP -> BG -> BG`

- `REDUCED_XOR_COUNTERFACTUALS.P6.S1` RESULT | evidence `Table` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P6.S2` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P6.S3` RESULT | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P6.S4` GAP | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P6.S5` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P6.S6` BG | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P7

- Paragraph role: `counterfactual`
- Current sequence: `BG -> BG -> GAP -> RESULT`

- `REDUCED_XOR_COUNTERFACTUALS.P7.S1` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P7.S2` BG | evidence `None` | operation `REPLACE_RISK_VERB`
- `REDUCED_XOR_COUNTERFACTUALS.P7.S3` GAP | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P7.S4` RESULT | evidence `None` | operation `KEEP`

## REDUCED_XOR_COUNTERFACTUALS.P8

- Paragraph role: `counterfactual`
- Current sequence: `SETUP -> BG -> BOUNDARY -> RESULT -> BG -> BG`

- `REDUCED_XOR_COUNTERFACTUALS.P8.S1` SETUP | evidence `Experiment setup` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P8.S2` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P8.S3` BOUNDARY | evidence `None` | operation `ADD_BOUNDARY`
- `REDUCED_XOR_COUNTERFACTUALS.P8.S4` RESULT | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P8.S5` BG | evidence `None` | operation `KEEP`
- `REDUCED_XOR_COUNTERFACTUALS.P8.S6` BG | evidence `None` | operation `KEEP`
