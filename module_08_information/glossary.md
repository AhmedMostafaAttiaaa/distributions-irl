# Module 08 glossary

| Term | Definition | Lesson |
|---|---|---|
| Surprise (self-information) | The information of an outcome, -ln p(x) in nats or -log2 p(x) in bits: zero for a certain event and large for a rare one. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Entropy | The average surprise of a distribution, H(p) = -sum p ln p; between 0 (point mass) and ln K (uniform), and the minimum average code length in bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Cross-entropy | The average surprise of data from p under a model q, H(p,q) = -sum p ln q = H(p) + KL(p\|\|q); the standard classification loss. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Perplexity | The exponential of the entropy or cross-entropy: the effective number of equally likely outcomes; the standard language-model metric. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Log loss | The average negative log probability that a model gave to the true class; cross-entropy between the labels and the predictions, and a proper scoring rule. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Differential entropy | The entropy of a continuous density, h = -integral f ln f; it can be negative, and the normal maximises it for a given variance. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Huffman code | A prefix code built from symbol probabilities whose average length lies between H and H + 1 bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
