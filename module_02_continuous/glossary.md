# Module 02 glossary

| Term | Definition | Lesson |
|---|---|---|
| Probability density function (PDF) | Function whose area over an interval is the probability; height is probability per unit of x. | [02_01](html/02_01_uniform_normal.html) |
| Density | Probability per unit of x; can exceed 1, only areas are probabilities. | [02_01](html/02_01_uniform_normal.html) |
| Uniform distribution | All values in [a, b] equally likely; mean (a+b)/2, variance (b-a)^2/12. | [02_01](html/02_01_uniform_normal.html) |
| Normal (Gaussian) distribution | Bell-shaped distribution with mean mu and standard deviation sigma. | [02_01](html/02_01_uniform_normal.html) |
| z-score | (x - mu) / sigma: the number of standard deviations from the mean. | [02_01](html/02_01_uniform_normal.html) |
| 68-95-99.7 rule | Share of a Normal within 1, 2 and 3 standard deviations of the mean. | [02_01](html/02_01_uniform_normal.html) |
| Standard normal | Normal with mean 0 and SD 1; its CDF is Phi. | [02_01](html/02_01_uniform_normal.html) |
| Q-Q plot | Plot of ordered data against theoretical quantiles; a straight line means a good fit. | [02_01](html/02_01_uniform_normal.html) |
| Central Limit Theorem | Averages of many independent values are approximately Normal. | [02_01](html/02_01_uniform_normal.html) |
| Process capability (Cp, Cpk) | Ratio of the specification width to the process spread (6 SD), and its off-center version. | [02_01](html/02_01_uniform_normal.html) |
| Lognormal distribution | A positive variable whose natural logarithm is Normal(mu, sigma^2). | [02_02](html/02_02_lognormal.html) |
| Multiplicative process | A quantity built by multiplying many random positive factors; its log is a sum. | [02_02](html/02_02_lognormal.html) |
| Geometric mean | exp(mean of the logs); equals the Lognormal median. | [02_02](html/02_02_lognormal.html) |
| Median vs mean (skew) | For a Lognormal mode < median < mean, due to the long right tail. | [02_02](html/02_02_lognormal.html) |
| Percentile / SLO | A value exceeded by a given share of cases; service-level objectives are set on p95 and p99. | [02_02](html/02_02_lognormal.html) |
| AIC | Akaike information criterion 2k - 2 log-likelihood; lower is better. | [02_02](html/02_02_lognormal.html) |
| Exponential distribution | Waiting time between events of a Poisson process; f(x) = lambda exp(-lambda x), mean = SD = 1/lambda. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Rate vs scale | Rate lambda is events per unit time; scale 1/lambda is the mean wait (what scipy uses). | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Memorylessness | P(X > s+t | X > s) = P(X > t): the past does not change the future wait. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Poisson process | Events at a constant rate with independent increments; counts are Poisson, gaps Exponential. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Erlang distribution | Time until the k-th event of a Poisson process; Gamma with integer shape. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Gamma distribution | Flexible positive skewed family with shape k and scale theta; mean k theta. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Gamma function | Extension of the factorial: Gamma(n) = (n-1)!. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Hazard rate | Instantaneous failure rate; constant for the Exponential. | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Survival function | S(x) = P(X > x) = 1 - F(x). | [02_03](html/02_03_exponential_gamma_erlang.html) |
| Beta distribution | Distribution on [0, 1] with shape parameters alpha and beta; used for unknown probabilities. | [02_04](html/02_04_beta.html) |
| Conjugate prior | A prior whose posterior is in the same family: Beta prior + Binomial data gives a Beta posterior. | [02_04](html/02_04_beta.html) |
| Posterior | Belief about a parameter after seeing data: prior times likelihood, renormalized. | [02_04](html/02_04_beta.html) |
| Credible interval | Interval containing the parameter with a stated posterior probability. | [02_04](html/02_04_beta.html) |
| Shrinkage | Pulling an extreme observed rate toward the prior mean, strongest with little data. | [02_04](html/02_04_beta.html) |
| Pseudo-count | Prior parameters read as already-seen successes (alpha - 1) and failures (beta - 1). | [02_04](html/02_04_beta.html) |
| Order statistic | The k-th smallest of n values; for Uniform(0,1) it is Beta(k, n-k+1). | [02_04](html/02_04_beta.html) |
| Beta function | B(a, b) = Gamma(a) Gamma(b) / Gamma(a+b), the normalizing constant of the Beta. | [02_04](html/02_04_beta.html) |
