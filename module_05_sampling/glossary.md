# Module 05 glossary

| Term | Definition | Lesson |
|---|---|---|
| Law of large numbers | The average of n iid observations converges to the true mean as n grows (weak: in probability; strong: with probability 1) | [05_01](html/05_01_law_of_large_numbers.html) |
| Convergence in probability | Y_n tends to c if P(\\\\|Y_n - c\\\\| > eps) tends to 0 for every eps | [05_01](html/05_01_law_of_large_numbers.html) |
| Almost-sure convergence | The whole path converges to the limit with probability 1 | [05_01](html/05_01_law_of_large_numbers.html) |
| Standard error | Standard deviation of a statistic over repeated samples; for the sample mean sigma / sqrt(n) (developed in 05_03) | [05_01](html/05_01_law_of_large_numbers.html) |
| Chebyshev inequality | P(\\\\|Y - E Y\\\\| >= t) <= Var(Y) / t^2 for any distribution with finite variance | [05_01](html/05_01_law_of_large_numbers.html) |
| Hoeffding inequality | For values in [a, b]: P(\\\\|average - mu\\\\| >= eps) <= 2 exp(-2 n eps^2 / (b-a)^2) | [05_01](html/05_01_law_of_large_numbers.html) |
| Gambler fallacy | The false belief that past outcomes make the opposite outcome due | [05_01](html/05_01_law_of_large_numbers.html) |
| Monte Carlo estimate | An expectation estimated by an average of simulated draws; error shrinks like 1 / sqrt(n) | [05_01](html/05_01_law_of_large_numbers.html) |
| Central limit theorem | Standardized sums or averages of iid variables with finite variance converge in distribution to N(0, 1) | [05_02](html/05_02_central_limit_theorem.html) |
| Standardization | Subtracting the mean and dividing by the standard deviation to get mean 0 and variance 1 | [05_02](html/05_02_central_limit_theorem.html) |
| Berry-Esseen theorem | Bounds the Kolmogorov distance to the Normal by 0.4748 rho / (sigma^3 sqrt n) | [05_02](html/05_02_central_limit_theorem.html) |
| Edgeworth expansion | Normal approximation plus correction terms; the first is -gamma (z^2 - 1) pdf(z) / (6 sqrt n) | [05_02](html/05_02_central_limit_theorem.html) |
| Stable law | Limit of scaled sums of iid variables with infinite variance (alpha-stable, not Normal) | [05_02](html/05_02_central_limit_theorem.html) |
| Delta method | If the average is approx Normal then g(average) is approx Normal with variance g prime squared times sigma^2 / n | [05_02](html/05_02_central_limit_theorem.html) |
| Control chart | Plot of subgroup means with limits mu +/- 3 sigma / sqrt n; alarm when outside | [05_02](html/05_02_central_limit_theorem.html) |
| Sampling distribution | Distribution of a statistic over repeated samples from the same population | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Statistic | A function of the sample, which is therefore a random variable | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Bessel correction | Dividing the sum of squares by n - 1 so the sample variance is unbiased | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Finite population correction | Factor sqrt((N - n) / (N - 1)) applied to the SE when sampling without replacement | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Confidence interval | Interval built so that a stated share of repeated samples gives an interval containing the true value | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Wilson interval | Confidence interval for a proportion that keeps good coverage for small counts | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Welch degrees of freedom | Approximate d.f. of the t distribution for a difference of means with unequal variances | [05_03](html/05_03_sampling_distributions_standard_error.html) |
| Bootstrap | Resampling the data with replacement to estimate the sampling distribution of a statistic | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Plug-in principle | Replacing the unknown distribution F by the empirical distribution of the sample | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Empirical distribution function | ECDF: puts mass 1/n on each observation | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Percentile interval | Confidence interval from the 2.5 % and 97.5 % quantiles of the bootstrap values | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| BCa interval | Bias-corrected and accelerated bootstrap interval | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Monte Carlo method | Estimating expectations or probabilities by simulating a model many times | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Monte Carlo error | Standard error of a simulation estimate: sqrt(p (1 - p) / B) for a probability | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Permutation test | Test that shuffles group labels to build the null distribution of a statistic | [05_04](html/05_04_bootstrap_monte_carlo.html) |
| Out-of-bag sample | Observations left out of a bootstrap resample (about 36.8 %) | [05_04](html/05_04_bootstrap_monte_carlo.html) |
