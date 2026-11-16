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
| Joint distribution | Distribution of two or more variables together. | [00_03](html/00_03_joint_conditional.html) |
| Marginal distribution | Distribution of one variable obtained by summing or integrating out the others. | [00_03](html/00_03_joint_conditional.html) |
| Conditional distribution | Distribution of one variable given a value of another: joint divided by marginal. | [00_03](html/00_03_joint_conditional.html) |
| Independence | Joint equals the product of the marginals; knowing one variable tells nothing about the other. | [00_03](html/00_03_joint_conditional.html) |
| Covariance | E[XY] - E[X]E[Y]; linear co-movement. | [00_03](html/00_03_joint_conditional.html) |
| Correlation | Covariance divided by the product of SDs, between -1 and 1. | [00_03](html/00_03_joint_conditional.html) |
| Bivariate Normal | Joint Normal with elliptical contours; conditionals are Normal with linear mean. | [00_03](html/00_03_joint_conditional.html) |
| Regression to the mean | Predictions are fewer SDs from the mean than the predictor, when correlation is below 1. | [00_03](html/00_03_joint_conditional.html) |
| Transformation | A new random variable Y = g(X) computed from X. | [00_04](html/00_04_transformations.html) |
| Change of variables | f_Y(y) = f_X(g^-1(y)) |d g^-1 / dy| for monotone g. | [00_04](html/00_04_transformations.html) |
| Jacobian factor | The stretching factor |dx/dy| that keeps the total area 1. | [00_04](html/00_04_transformations.html) |
| z-score | (X - mu) / sigma: mean 0, variance 1, unit free. | [00_04](html/00_04_transformations.html) |
| Probability integral transform | F(X) is Uniform(0,1) for a continuous CDF F. | [00_04](html/00_04_transformations.html) |
| Jensen inequality | E[g(X)] >= g(E[X]) for convex g. | [00_04](html/00_04_transformations.html) |
