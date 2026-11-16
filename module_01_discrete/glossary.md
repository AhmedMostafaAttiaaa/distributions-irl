# Module 01 glossary

| Term | Definition | Lesson |
|---|---|---|
| Bernoulli trial | One experiment with two outcomes, success (1) with probability p and failure (0). | [01_01](html/01_01_bernoulli_binomial.html) |
| Binomial distribution | Number of successes in n independent Bernoulli(p) trials. | [01_01](html/01_01_bernoulli_binomial.html) |
| Continuity correction | Adding or subtracting 0.5 when approximating a discrete variable by a Normal. | [01_01](html/01_01_bernoulli_binomial.html) |
| PMF | Probability mass function: P(X = k) for a discrete variable. | [01_01](html/01_01_bernoulli_binomial.html) |
| CDF | Cumulative distribution function: P(X <= k). | [01_01](html/01_01_bernoulli_binomial.html) |
| PGF | Probability generating function G(s) = E[s^X]; multiplies for independent sums. | [01_01](html/01_01_bernoulli_binomial.html) |
| Survival function (sf) | P(X > k) = 1 - CDF. | [01_01](html/01_01_bernoulli_binomial.html) |
| Quantile (ppf) | The smallest k with CDF(k) at least a given probability. | [01_01](html/01_01_bernoulli_binomial.html) |
| Geometric distribution | Number of trials until the first success; memoryless. | [01_02](html/01_02_geometric_negative_binomial.html) |
| Memorylessness | P(X > m+n | X > m) = P(X > n): the past does not change the future wait. | [01_02](html/01_02_geometric_negative_binomial.html) |
| Negative Binomial distribution | Number of trials (or failures) until the r-th success; sum of r Geometrics. | [01_02](html/01_02_geometric_negative_binomial.html) |
| Overdispersion | Variance larger than the mean, which Poisson cannot represent. | [01_02](html/01_02_geometric_negative_binomial.html) |
| Gamma-Poisson mixture | Poisson counts with a Gamma-distributed rate; gives a Negative Binomial. | [01_02](html/01_02_geometric_negative_binomial.html) |
| Poisson distribution | Count of independent events at a constant rate in a fixed window; mean = variance = lambda. | [01_03](html/01_03_poisson.html) |
| Rate (lambda) | Average number of events per window; scales with window length. | [01_03](html/01_03_poisson.html) |
| Poisson process | Events at a constant rate with independent increments; gaps are Exponential. | [01_03](html/01_03_poisson.html) |
| Thinning | Keeping each Poisson event with probability q gives Poisson(q lambda). | [01_03](html/01_03_poisson.html) |
| Chi-square goodness of fit | Test comparing observed counts with expected counts from a fitted model. | [01_03](html/01_03_poisson.html) |
| Dispersion | Variance relative to the mean; Poisson has ratio 1. | [01_03](html/01_03_poisson.html) |
| Hypergeometric distribution | Number of special items in a sample drawn without replacement from a finite population. | [01_04](html/01_04_hypergeometric.html) |
| Sampling without replacement | Drawn items are not returned, so draws are dependent. | [01_04](html/01_04_hypergeometric.html) |
| Finite-population correction | Factor (N-n)/(N-1) that shrinks the variance when sampling without replacement. | [01_04](html/01_04_hypergeometric.html) |
| Fisher exact test | Exact test for a 2x2 table based on the Hypergeometric distribution. | [01_04](html/01_04_hypergeometric.html) |
| Acceptance sampling | Inspecting a sample to decide whether to accept a lot. | [01_04](html/01_04_hypergeometric.html) |
| Discrete uniform | All outcomes in a finite set equally likely. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Categorical distribution | One draw from k classes with probabilities p_1..p_k. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Multinomial distribution | Counts of each of k classes in n independent categorical draws. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Softmax | Maps scores to probabilities: p_j = exp(z_j) / sum exp(z_i). | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| One-hot encoding | Vector with a single 1 marking the class. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Cross-entropy loss | Negative log-probability the model assigns to the true class. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Chi-square statistic | Sum of (observed - expected)^2 / expected over categories. | [01_05](html/01_05_uniform_categorical_multinomial.html) |
| Zipf distribution | P(X=k) proportional to k^(-s); frequency falls as a power of rank. | [01_06](html/01_06_zipf_power_laws.html) |
| Zeta distribution | Infinite-support Zipf with s > 1, normalized by the Riemann zeta function. | [01_06](html/01_06_zipf_power_laws.html) |
| Power law | Relationship y = C x^(-s); a straight line of slope -s on log-log axes. | [01_06](html/01_06_zipf_power_laws.html) |
| Heavy tail | Tail that decays more slowly than any exponential, so extreme values are common. | [01_06](html/01_06_zipf_power_laws.html) |
| Rank-frequency plot | Counts plotted against rank, usually on log-log axes. | [01_06](html/01_06_zipf_power_laws.html) |
| Hapax legomenon | A word that occurs exactly once in a text. | [01_06](html/01_06_zipf_power_laws.html) |
| Harmonic number | H_N = 1 + 1/2 + ... + 1/N. | [01_06](html/01_06_zipf_power_laws.html) |
