# Module 08 glossary

| Term | Definition | Lesson |
|---|---|---|
| Surprise (self-information) | The information of an outcome, -ln p(x) in nats or -log2 p(x) in bits: zero for a certain event and large for a rare one. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Entropy | The average surprise of a distribution, H(p) = -sum p ln p; between 0 (point mass) and ln K (uniform), and the minimum average code length in bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Cross-entropy | The average surprise of data from p under a model q, H(p,q) = -sum p ln q = H(p) + KL(p\\|\\|q); the standard classification loss. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Perplexity | The exponential of the entropy or cross-entropy: the effective number of equally likely outcomes; the standard language-model metric. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Log loss | The average negative log probability that a model gave to the true class; cross-entropy between the labels and the predictions, and a proper scoring rule. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Differential entropy | The entropy of a continuous density, h = -integral f ln f; it can be negative, and the normal maximises it for a given variance. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Huffman code | A prefix code built from symbol probabilities whose average length lies between H and H + 1 bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
| KL divergence | The expected extra surprise of using q when the data follow p, KL(p\|\|q) = sum p ln(p/q) = H(p,q) - H(p); non-negative, zero only if q = p, and not symmetric. | [08_02](html/08_02_kl_js_divergence.html) |
| Jensen-Shannon divergence | A symmetric, always finite version of KL: the average of KL(p\|\|m) and KL(q\|\|m) with m the mixture of p and q; bounded by ln 2, and its square root is a metric. | [08_02](html/08_02_kl_js_divergence.html) |
| Population stability index (PSI) | The symmetrised KL divergence sum (q - p) ln(q / p) between a training and a live distribution over bins; used to monitor data drift. | [08_02](html/08_02_kl_js_divergence.html) |
| Forward and reverse KL | KL(p\|\|q) (forward) makes q cover all of p's mass, as in maximum likelihood; KL(q\|\|p) (reverse) lets q lock onto one mode, as in variational inference. | [08_02](html/08_02_kl_js_divergence.html) |
| G-test | The likelihood-ratio goodness-of-fit test for counts: G = 2n KL(p_hat\|\|p0), chi-square distributed with K - 1 degrees of freedom under the null. | [08_02](html/08_02_kl_js_divergence.html) |
| Pinsker's inequality | The bound TV(p,q) <= sqrt(KL(p\|\|q) / 2) between the total variation distance and the KL divergence. | [08_02](html/08_02_kl_js_divergence.html) |
| Total variation distance | Half the sum of absolute differences between two distributions, the largest difference in probability they assign to any event. | [08_02](html/08_02_kl_js_divergence.html) |
