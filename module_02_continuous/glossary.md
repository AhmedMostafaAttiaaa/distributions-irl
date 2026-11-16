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
| Weibull distribution | Lifetime distribution with shape k and scale lambda; survival exp(-(x/lambda)^k). | [02_05](html/02_05_weibull.html) |
| Hazard rate | Instantaneous failure risk at age t among units still working: h(t) = f(t)/S(t). | [02_05](html/02_05_weibull.html) |
| Infant mortality | Falling hazard (Weibull shape k < 1): survivors become safer. | [02_05](html/02_05_weibull.html) |
| Wear-out | Rising hazard (Weibull shape k > 1): risk grows with age. | [02_05](html/02_05_weibull.html) |
| Bathtub curve | Hazard that falls, stays flat, then rises over a product life. | [02_05](html/02_05_weibull.html) |
| Characteristic life | The Weibull scale lambda: 63.2 % of units fail by this age for any shape. | [02_05](html/02_05_weibull.html) |
| MTTF | Mean time to failure, lambda Gamma(1 + 1/k) for the Weibull. | [02_05](html/02_05_weibull.html) |
| Weibull plot | Plot of ln(-ln(1-F)) against ln(x); a straight line with slope k means Weibull. | [02_05](html/02_05_weibull.html) |
| Weakest link (series system) | A system that fails with its first part; the minimum of Weibulls is Weibull with scale lambda n^(-1/k). | [02_05](html/02_05_weibull.html) |
| Rayleigh distribution | Weibull with shape 2, used for wind speed and noise magnitude. | [02_05](html/02_05_weibull.html) |
| Censoring | Units that have not failed by the end of observation; they carry partial information. | [02_05](html/02_05_weibull.html) |
| Heavy tail | Tail that decays more slowly than any exponential, so extreme values remain common. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Pareto distribution | Power-law tail S(x) = (x_m/x)^alpha for x >= x_m. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Tail index (alpha) | Exponent of a power-law tail; smaller means heavier; moments of order >= alpha are infinite. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Cauchy distribution | Bell-shaped distribution with no mean or variance; ratio of two standard Normals. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| 80/20 rule (Pareto principle) | About 80 % of the total comes from 20 % of the population; alpha = 1.16 for a Pareto. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Gini coefficient | Inequality measure from 0 to 1; 1/(2 alpha - 1) for a Pareto. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Lorenz curve | Share of the total held by the bottom fraction of the population. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Scale invariance | P(X > cx | X > x) = c^(-alpha) for a Pareto, independent of x. | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Stable distribution | Distribution closed under sums up to scale and shift (Normal, Cauchy). | [02_06](html/02_06_heavy_tails_pareto_cauchy.html) |
| Laplace distribution | Double-exponential distribution f(x) = exp(-|x-mu|/b)/(2b); likelihood of absolute (L1) errors. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| L1 loss (MAE) | Sum of absolute errors; minimized by the median; the Laplace negative log-likelihood. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Robust estimator | Estimator little affected by outliers, such as the median. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Logistic distribution | Bell-like distribution whose CDF is the sigmoid; variance pi^2 s^2 / 3. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Sigmoid / logit | Sigmoid 1/(1+e^-z) maps log-odds to a probability; the logit is its inverse. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Latent-variable model | A hidden continuous variable plus noise crossing a threshold decides a binary outcome. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Gumbel distribution | Limit law of maxima of light-tailed variables; F(x) = exp(-exp(-(x-mu)/beta)). | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Return level / return period | Value exceeded with probability 1/T per year; T is the return period. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Gumbel-max trick | argmax(score + Gumbel noise) samples a Categorical with softmax probabilities. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Laplace mechanism | Adding Laplace noise to a query answer to achieve differential privacy. | [02_07](html/02_07_laplace_logistic_gumbel.html) |
| Sampling distribution | Distribution of a statistic (mean, variance, ratio) over repeated samples. | [02_08](html/02_08_t_chisquare_f.html) |
| Degrees of freedom | Number of independent pieces of information; n - 1 for the sample variance. | [02_08](html/02_08_t_chisquare_f.html) |
| Chi-square distribution | Sum of squares of independent standard normals; Gamma(nu/2, scale 2). | [02_08](html/02_08_t_chisquare_f.html) |
| Student t distribution | Standard normal divided by sqrt(chi-square/nu); heavier tails than the Normal. | [02_08](html/02_08_t_chisquare_f.html) |
| F distribution | Ratio of two independent chi-squares each divided by its degrees of freedom. | [02_08](html/02_08_t_chisquare_f.html) |
| Standard error | Estimated SD of a statistic, s / sqrt(n) for the mean. | [02_08](html/02_08_t_chisquare_f.html) |
| Critical value | Quantile that bounds the rejection region of a test. | [02_08](html/02_08_t_chisquare_f.html) |
| p-value | Probability, under the null hypothesis, of a statistic at least as extreme as observed. | [02_08](html/02_08_t_chisquare_f.html) |
| Confidence interval | Range computed from data that covers the true parameter in a stated share of repeated samples. | [02_08](html/02_08_t_chisquare_f.html) |
| Coverage | Actual share of intervals containing the true value. | [02_08](html/02_08_t_chisquare_f.html) |
