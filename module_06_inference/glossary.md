# Module 06 glossary

| Term | Definition | Lesson |
|---|---|---|
| Estimator | A rule that turns a sample into a guess for a parameter; as a function of random data it has a sampling distribution. | [06_01](html/06_01_estimation_mle_mom.html) |
| Bias | The expected value of an estimator minus the true parameter; an estimator is unbiased if the bias is 0. | [06_01](html/06_01_estimation_mle_mom.html) |
| Mean squared error (MSE) | E[(estimate - truth)^2] = variance + bias^2; the standard measure of the accuracy of an estimator. | [06_01](html/06_01_estimation_mle_mom.html) |
| Consistency | An estimator is consistent if it converges in probability to the true parameter as the sample grows. | [06_01](html/06_01_estimation_mle_mom.html) |
| Method of moments | Estimating parameters by equating the theoretical moments of the model with the sample moments and solving. | [06_01](html/06_01_estimation_mle_mom.html) |
| Likelihood | The probability (density) of the observed data viewed as a function of the parameter; the product of the densities for independent data. | [06_01](html/06_01_estimation_mle_mom.html) |
| Maximum likelihood estimator (MLE) | The parameter value that maximises the likelihood (equivalently the log-likelihood); found where the score is zero. | [06_01](html/06_01_estimation_mle_mom.html) |
| Score and Fisher information | The score is the derivative of the log-likelihood; the Fisher information is its variance, or minus the expected second derivative, and measures how sharply the data pin down the parameter. | [06_01](html/06_01_estimation_mle_mom.html) |
| Cramer-Rao bound | Lower bound 1 / (n I) on the variance of any unbiased estimator; the MLE attains it asymptotically. | [06_01](html/06_01_estimation_mle_mom.html) |
| Invariance of the MLE | If theta-hat is the MLE of theta, then g(theta-hat) is the MLE of g(theta). | [06_01](html/06_01_estimation_mle_mom.html) |
| Sufficient statistic | A function of the data (such as the sum for the Exponential) that contains all the information about the parameter. | [06_01](html/06_01_estimation_mle_mom.html) |
| Confidence interval | A range (L, U) computed from the data by a procedure that contains the true parameter in at least 95 % (or the chosen level) of repeated samples. | [06_02](html/06_02_confidence_intervals.html) |
| Coverage probability | The long-run share of samples whose confidence interval contains the true parameter; the actual coverage can differ from the nominal level. | [06_02](html/06_02_confidence_intervals.html) |
| Pivotal quantity | A function of the data and the parameter whose distribution does not depend on the parameter, such as (x-bar - mu) / (s / sqrt n), which has a t distribution. | [06_02](html/06_02_confidence_intervals.html) |
| Margin of error | The half-width of a confidence interval, z x standard error; the sample size for a margin m is n = (z sigma / m)^2. | [06_02](html/06_02_confidence_intervals.html) |
| t interval | x-bar plus or minus t(n-1) s / sqrt n; the interval for a Normal mean when the standard deviation is estimated. | [06_02](html/06_02_confidence_intervals.html) |
| Wald interval | Estimate plus or minus z standard errors with the standard error computed at the estimate; poor for small samples and rare events. | [06_02](html/06_02_confidence_intervals.html) |
| Wilson interval | Interval for a proportion obtained by inverting the score test; stays inside 0 to 1 and has near-nominal coverage. | [06_02](html/06_02_confidence_intervals.html) |
| Clopper-Pearson (exact) interval | Interval for a proportion from the exact Binomial tails (Beta quantiles); guaranteed to cover at least the nominal level, hence conservative. | [06_02](html/06_02_confidence_intervals.html) |
| Prediction interval | A range for a single future observation, much wider than the confidence interval for the mean. | [06_02](html/06_02_confidence_intervals.html) |
| Null hypothesis | The default 'no effect' claim H0 that is kept unless the data provide strong evidence against it. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Alternative hypothesis | The claim H1 that the test looks for, one-sided (greater or less) or two-sided (not equal). | [06_03](html/06_03_hypothesis_testing_core.html) |
| Test statistic | A number computed from the data, such as z or t, whose distribution under H0 is known. | [06_03](html/06_03_hypothesis_testing_core.html) |
| p-value | The probability, if H0 is true, of a test statistic at least as extreme as the one observed; not the probability that H0 is true. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Significance level | The Type I error rate alpha chosen in advance (often 5 %); H0 is rejected when the p-value is at most alpha. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Type I error | Rejecting a true null hypothesis (a false positive); its probability is alpha. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Type II error | Failing to reject a false null hypothesis (a false negative); its probability is beta. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Power | The probability 1 - beta of rejecting H0 when a specified alternative is true; grows with the effect size and the sample size. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Effect size | The size of the true difference, often standardised as d = (mu - mu0) / sigma; the quantity power depends on. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Rejection region | The set of test-statistic values for which H0 is rejected; its probability under H0 equals alpha. | [06_03](html/06_03_hypothesis_testing_core.html) |
| Neyman-Pearson lemma | For two simple hypotheses the most powerful test of a given level rejects when the likelihood ratio is large. | [06_03](html/06_03_hypothesis_testing_core.html) |
