# 顶刊语料抽取质量报告

这个报告用于判断顶刊 corpus 是否干净。它统计抽取后删除了哪些非论文正文噪声，并给出人工抽查样例。

## 总览

- 原始抽取句子/功能单元：1377 条。
- 删除噪声：106 条。
- 保留进入 corpus：1271 条。

## 删除原因统计

- `affiliation_or_email`：64 条。
- `funding_or_correspondence`：16 条。
- `manuscript_metadata`：8 条。
- `numeric_or_punctuation_fragment`：8 条。
- `single_letter_or_axis_tokens`：4 条。
- `caption_or_caption_fragment`：3 条。
- `table_or_figure_fragment`：2 条。
- `ocr_fragment`：1 条。

## 保留记录按 section 统计

- `Abstract`：532 条。
- `Contribution`：61 条。
- `Introduction`：418 条。
- `Results`：260 条。

## 删除样例（最多 20 条）

- `manuscript_metadata` / `Introduction`：Aimed at solving non-convex optimization problems, Beyer and Ogier introduced tabu learning into the Hopfield neural network (HNN), which enables the state trajectory to Manuscript
- `funding_or_correspondence` / `Introduction`：This work was supported in part by the National Natural Science Foundation of China under Grant 62271197, and in part by the Guangdong Basic and Applied Basic Research Foundation u
- `funding_or_correspondence` / `Introduction`：Quanli Deng, Chunhua Wang, Zekun Deng, and Gang Yang are with the College of Information Science and Engineering, Hunan University, Changsha, 410082, China (Corresponding author: C
- `affiliation_or_email` / `Introduction`：Chunhua Wang is also with the Greater Bay Area Institute for Innovation, Hunan University, Guangzhou, 511300, China.
- `affiliation_or_email` / `Introduction`：Yichuang Sun is with the School of Engineering and Computer Science, University of Hertfordshire, Hatfield AL10 9AB, U.K. climb out of local minima thus performing an efficient sea
- `manuscript_metadata` / `Introduction`：(e-mail: C.Gu@qub.ac.uk) Manuscript received xx xx, xxxx; revised xx xx, xxxx.
- `numeric_or_punctuation_fragment` / `Introduction`：0 0 1 0 - 1 1 1 0 - 1 0 1 0 - 9 1 0 - 8 1 0 - 7 1 0 - 6 1 0 - 5 1 0 - 4 1 0 - 3 1 0 - 2 1 0 - 1 1 0 0 [ 3 2 ] T h i s w o r k C o n v e n t i o n a l A P U F [ 2 0 ] [ 2 4 ] [ 1 8 
- `numeric_or_punctuation_fragment` / `Results`：9 1 0 0 1 k 1 0 k 1 0 0 k 0 .
- `single_letter_or_axis_tokens` / `Results`：0 P r e d i c t i o n a c c u r a c y T r a i n i n g s e t s i z e A P U F D D Q - A P U F d = 3 D D Q - A P U F d = 0 3 X O R A P U F 3 P X O R D D Q - A P U F d = 3 3 P X O R D 
- `single_letter_or_axis_tokens` / `Results`：0 P r e d i c t i o n a c c u r a c y T r a i n i n g s e t s i z e A P U F D D Q - A P U F d = 3 D D Q - A P U F d = 0 3 X O R A P U F 3 P X O R D D Q - A P U F d = 3 3 P X O R D 
- `single_letter_or_axis_tokens` / `Results`：0 P r e d i c t i o n a c c u r a c y T r a i n i n g s e t s i z e A P U F D D Q - A P U F d = 3 D D Q - A P U F d = 0 3 X O R A P U F 3 P X O R D D Q - A P U F d = 3 3 P X O R D 
- `numeric_or_punctuation_fragment` / `Introduction`：1, a significant 56% reduction in macrolevel EDAP is achieved when transitioning from a small- to a large-size standard (Std.) subarray design.
- `funding_or_correspondence` / `Introduction`：This work was supported in part by the Research Project “Thermodynamics of Circuits for Computation” of the National Fund for Scientific Research (FNRS) of Belgium.
- `funding_or_correspondence` / `Introduction`：(Corresponding author: Léopold Van Brandt.) Léopold Van Brandt, Denis Flandre, and Jean-Charles Delvenne are with the Institute for Information and Communication Technologies, Elec
- `affiliation_or_email` / `Introduction`：Michele Bonnin is with the Department of Electronics and Telecommunications, Politecnico di Torino, 10129 Turin, Italy.
- `affiliation_or_email` / `Introduction`：Mauricio Banaszeski da Silva is with the Department of Electronics and Computing, Universidade Federal de Santa Maria, Santa Maria 97105-900, Brazil.
- `affiliation_or_email` / `Introduction`：In all these domains of application, randomly distributed data often require normalization or standardization to enhance the robustness of the 1School of Automation and Information
- `affiliation_or_email` / `Introduction`：E-mail address: yunm@xaut.edu.cn This paper was produced by the IEEE Publication Technology Group.
- `single_letter_or_axis_tokens` / `Results`：(20); and (c) PSADIC-2 in Eq.
- `affiliation_or_email` / `Introduction`：For this reason, in 2016[2], the National Institute of Standards and Technology (NIST) started a competition for Post-Quantum Cryptography (PQC) algorithms, which resist quantum an

## 保留样例（最多 20 条）

- `Abstract`：—Memristors, with their unique nonlinear characteristics, are highly suitable for construction novel neural models with rich dynamic behaviors.
- `Abstract`：In this paper, a memristor with piecewise nonlinear state function is introduced into the tabu learning neuron model, resulting in a novel memristive tabu learning neuron model cap
- `Abstract`：By modulating the state function of the memristor, we can effectively and easily alter the number of wings of the chaotic butterfly.
- `Abstract`：Equilibrium points analysis further elucidates the mechanism behind the generation of multiwing chaos.
- `Abstract`：Various numerical simulation techniques, including phase portraits, bifurcation diagrams, Lyapunov exponent spectra, and local attraction basins, are employed to illustrate the dyn
- `Abstract`：Moreover, the newly constructed neuron model is validated using FPGA hardware, with the results aligning with numerical simulations, thereby offering a dependable foundation for a 
- `Abstract`：Lastly, an image encryption application based on the multi-wing chaotic butterfly is developed to demonstrate the potential application of the model.
- `Introduction`：INVESTIGATING the dynamical behaviors of neural networks can guide us in exploring more appropriate control strategies to achieve neural dynamics in the artificial neural networks.
- `Introduction`：The recurrent neural network proposed by J.
- `Introduction`：Hopfield in 1984 [1], has received extensive attention not only because of its engineering applications in optimization problems [2] and content-address memory [3], but also becaus
- `Introduction`：Dynamical behaviors of tabu learning neurons (TLNs) have attracted attention, prompting a closer examination of the running trajectories of the neural network.
- `Introduction`：Li et al. took the memory decay rate as a bifurcation parameter and studied the dynamical behaviors of tabu learning neurons, proving that a single TLN can transition between stabl
- `Introduction`：Xiao and Cao studied the stability of a discrete-time tabu learning single neuron model, finding that Pitchfork, Flip, and Neimark-Sacker bifurcations occur when the bifurcation pa
- `Introduction`：Bao et al. studied the dynamical behaviors of a non-autonomous TLN by introducing an external input to the TLN, discovering complex neuron firing patterns in their non-autonomous T
- `Abstract`：—As a lightweight hardware security primitive, physical unclonable functions (PUFs) can provide reliable identity authentication for the Internet of Things (IoT) devices with limit
- `Abstract`：Arbiter PUF (APUF) is one of the most wellknown PUF circuits.
- `Abstract`：However, its hardware implementation has poor reliability on field programmable gate arrays (FPGAs).
- `Abstract`：This paper proposed a highly reliable APUF that uses a delay difference quantization strategy (DDQ-APUF).
- `Abstract`：By adding multiple configurable delay units to the two symmetrical paths of the conventional APUF, the delay difference between the two symmetrical paths of APUF can be obtained by
- `Abstract`：Compared to conventional APUFs, DDQ-APUF does not use the arbitration result of signal transmission in two symmetric paths as its response, but rather uses the quantified delay dif
