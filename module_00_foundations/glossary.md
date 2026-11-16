# Module 00 glossary

| Term | Definition | Lesson |
|---|---|---|
| Random variable | A number produced by a random experiment. | [00_01](html/00_01_random_variables.html) |
| Discrete / continuous | Takes separate values / any value in an interval. | [00_01](html/00_01_random_variables.html) |
| PMF | Probability mass function p(x) = P(X = x) of a discrete variable. | [00_01](html/00_01_random_variables.html) |
| PDF | Probability density function; probabilities are areas under it. | [00_01](html/00_01_random_variables.html) |
| CDF | Cumulative distribution function F(x) = P(X <= x). | [00_01](html/00_01_random_variables.html) |
| Survival function | S(x) = P(X > x) = 1 - F(x). | [00_01](html/00_01_random_variables.html) |
| Quantile (PPF) | Inverse CDF: the value that leaves a given probability below it. | [00_01](html/00_01_random_variables.html) |
| Inverse transform sampling | Generating X = F^-1(U) from a Uniform(0,1) variable U. | [00_01](html/00_01_random_variables.html) |
| Expected value (mean) | Probability-weighted average of the values: E[X]. | [00_02](html/00_02_expectation_moments.html) |
| Variance | E[(X - mu)^2] = E[X^2] - mu^2; spread around the mean. | [00_02](html/00_02_expectation_moments.html) |
| Standard deviation | Square root of the variance, in the original units. | [00_02](html/00_02_expectation_moments.html) |
| Moment | E[X^k]; central moments use X minus the mean. | [00_02](html/00_02_expectation_moments.html) |
| Skewness | Standardized third central moment; asymmetry. | [00_02](html/00_02_expectation_moments.html) |
| Kurtosis | Standardized fourth central moment; tail weight (excess = kurtosis - 3). | [00_02](html/00_02_expectation_moments.html) |
| Moment generating function (MGF) | M(t) = E[exp(tX)]; its k-th derivative at 0 is E[X^k]. | [00_02](html/00_02_expectation_moments.html) |
| Linearity of expectation | E[aX + bY] = aE[X] + bE[Y], with or without independence. | [00_02](html/00_02_expectation_moments.html) |
| Law of Large Numbers | The sample mean converges to E[X]. | [00_02](html/00_02_expectation_moments.html) |
