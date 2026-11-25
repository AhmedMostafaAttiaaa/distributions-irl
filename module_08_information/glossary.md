# Module 08 glossary

| Term | Definition | Lesson |
|---|---|---|
| Surprise (self-information) | The information of an outcome, -ln p(x) in nats or -log2 p(x) in bits: zero for a certain event and large for a rare one. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Entropy | The average surprise of a distribution, H(p) = -sum p ln p; between 0 (point mass) and ln K (uniform), and the minimum average code length in bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Cross-entropy | The average surprise of data from p under a model q, H(p,q) = -sum p ln q = H(p) + KL(p\\\\|\\\\|q); the standard classification loss. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Perplexity | The exponential of the entropy or cross-entropy: the effective number of equally likely outcomes; the standard language-model metric. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Log loss | The average negative log probability that a model gave to the true class; cross-entropy between the labels and the predictions, and a proper scoring rule. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Differential entropy | The entropy of a continuous density, h = -integral f ln f; it can be negative, and the normal maximises it for a given variance. | [08_01](html/08_01_entropy_cross_entropy.html) |
| Huffman code | A prefix code built from symbol probabilities whose average length lies between H and H + 1 bits. | [08_01](html/08_01_entropy_cross_entropy.html) |
| KL divergence | The expected extra surprise of using q when the data follow p, KL(p\\\|\\\|q) = sum p ln(p/q) = H(p,q) - H(p); non-negative, zero only if q = p, and not symmetric. | [08_02](html/08_02_kl_js_divergence.html) |
| Jensen-Shannon divergence | A symmetric, always finite version of KL: the average of KL(p\\\|\\\|m) and KL(q\\\|\\\|m) with m the mixture of p and q; bounded by ln 2, and its square root is a metric. | [08_02](html/08_02_kl_js_divergence.html) |
| Population stability index (PSI) | The symmetrised KL divergence sum (q - p) ln(q / p) between a training and a live distribution over bins; used to monitor data drift. | [08_02](html/08_02_kl_js_divergence.html) |
| Forward and reverse KL | KL(p\\\|\\\|q) (forward) makes q cover all of p's mass, as in maximum likelihood; KL(q\\\|\\\|p) (reverse) lets q lock onto one mode, as in variational inference. | [08_02](html/08_02_kl_js_divergence.html) |
| G-test | The likelihood-ratio goodness-of-fit test for counts: G = 2n KL(p_hat\\\|\\\|p0), chi-square distributed with K - 1 degrees of freedom under the null. | [08_02](html/08_02_kl_js_divergence.html) |
| Pinsker's inequality | The bound TV(p,q) <= sqrt(KL(p\\\|\\\|q) / 2) between the total variation distance and the KL divergence. | [08_02](html/08_02_kl_js_divergence.html) |
| Total variation distance | Half the sum of absolute differences between two distributions, the largest difference in probability they assign to any event. | [08_02](html/08_02_kl_js_divergence.html) |
| Wasserstein distance | The least work needed to move the mass of one distribution onto another, W_p = (inf over couplings of E\\|X - Y\\|^p)^(1/p); a metric measured in the units of the variable. | [08_03](html/08_03_wasserstein_distance.html) |
| Earth mover's distance | Another name for the Wasserstein-1 distance: the minimum amount of earth times distance needed to reshape one pile into another. | [08_03](html/08_03_wasserstein_distance.html) |
| Optimal transport | The problem of moving one distribution onto another at minimum total cost; in one dimension the optimal plan matches sorted values, in general it is a linear program. | [08_03](html/08_03_wasserstein_distance.html) |
| Coupling | A joint distribution with two given marginals; the Wasserstein distance minimises the expected cost over all couplings. | [08_03](html/08_03_wasserstein_distance.html) |
| Kantorovich-Rubinstein duality | W1(p, q) equals the supremum of E_p f - E_q f over all 1-Lipschitz functions f; the basis of the Wasserstein GAN critic. | [08_03](html/08_03_wasserstein_distance.html) |
| Frechet distance (FID) | The Wasserstein-2 distance between two Gaussians, sqrt of the squared mean distance plus a covariance term; the FID score of image generators applies it to network features. | [08_03](html/08_03_wasserstein_distance.html) |
| Wasserstein GAN | A generative adversarial network trained with a 1-Lipschitz critic that estimates the Wasserstein-1 distance, giving useful gradients even when real and generated samples do not overlap. | [08_03](html/08_03_wasserstein_distance.html) |
| Mutual information | The KL divergence between a joint distribution and the product of its marginals, I(X;Y) = H(X) - H(X\|Y); zero iff X and Y are independent, and it detects any kind of dependence. | [08_04](html/08_04_mutual_information.html) |
| Conditional entropy | The average remaining uncertainty about X once Y is known, H(X\|Y) = H(X,Y) - H(Y). | [08_04](html/08_04_mutual_information.html) |
| Information gain | The reduction in the entropy of a label produced by a split or a feature, H(Y) - H(Y\|S) = I(Y;S); the criterion of decision-tree splits. | [08_04](html/08_04_mutual_information.html) |
| Normalised mutual information | Mutual information divided by sqrt(H(X) H(Y)) so that it lies between 0 and 1; used to compare variables and clusterings. | [08_04](html/08_04_mutual_information.html) |
| Data processing inequality | No processing of Y can increase the information it carries about X: I(X; f(Y)) <= I(X; Y). | [08_04](html/08_04_mutual_information.html) |
| KSG estimator | The Kraskov-Stoegbauer-Grassberger nearest-neighbour estimator of the mutual information of continuous variables, which avoids binning. | [08_04](html/08_04_mutual_information.html) |
| Mutual-information feature selection | A filter method that ranks features by the mutual information with the target, corrected for estimation bias and checked against a permutation baseline. | [08_04](html/08_04_mutual_information.html) |
