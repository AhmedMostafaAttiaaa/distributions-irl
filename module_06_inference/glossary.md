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
| Welch t-test | Two-sample t-test that does not assume equal variances: t = (difference of means) / sqrt(s1^2/n1 + s2^2/n2) with Satterthwaite degrees of freedom; the recommended default. | [06_04](html/06_04_common_tests.html) |
| Pooled t-test | Two-sample t-test that assumes equal variances and uses the pooled standard deviation; inflated Type I error when the variances and sample sizes differ. | [06_04](html/06_04_common_tests.html) |
| Paired t-test | One-sample t-test on the within-unit differences; removes between-unit variation and is more sensitive when the pairs are correlated. | [06_04](html/06_04_common_tests.html) |
| Chi-square goodness-of-fit test | Compares observed counts with the counts expected under a model: chi-square = sum of (O - E)^2 / E with K - 1 degrees of freedom. | [06_04](html/06_04_common_tests.html) |
| Chi-square test of independence | Tests whether two categorical variables are related in a contingency table; expected counts are row total times column total divided by n, df = (r - 1)(c - 1). | [06_04](html/06_04_common_tests.html) |
| Cramer's V | Strength of association in a contingency table, sqrt(chi-square / (n min(r - 1, c - 1))), between 0 and 1. | [06_04](html/06_04_common_tests.html) |
| One-way ANOVA | Test that several group means are equal, comparing the variation between groups with the variation within groups. | [06_04](html/06_04_common_tests.html) |
| F statistic | Ratio of two independent variance estimates (mean squares), F = MSB / MSW in ANOVA; follows an F distribution with (k - 1, N - k) degrees of freedom under H0. | [06_04](html/06_04_common_tests.html) |
| Cohen's d | Standardised difference of two means, (mean1 - mean2) / pooled SD; about 0.2 small, 0.5 medium, 0.8 large. | [06_04](html/06_04_common_tests.html) |
| Eta squared | Share of the total variation explained by the groups in ANOVA, SSB / SST. | [06_04](html/06_04_common_tests.html) |
| Nonparametric test | A test whose null distribution does not depend on the shape of the data distribution, often based on ranks or on relabelling the data. | [06_05](html/06_05_nonparametric_tests.html) |
| Rank | The position of an observation in the sorted pooled sample (1 = smallest); ties receive the average rank. | [06_05](html/06_05_nonparametric_tests.html) |
| Mann-Whitney U test | Rank-based test (equivalent to the Wilcoxon rank-sum test) that two independent samples come from the same distribution; U / (n1 n2) estimates P(X1 > X2). | [06_05](html/06_05_nonparametric_tests.html) |
| Probability of superiority | P(X1 > X2) for a random observation from each group, estimated by U / (n1 n2); equals the AUC when the values are scores. | [06_05](html/06_05_nonparametric_tests.html) |
| Wilcoxon signed-rank test | Rank test for paired data that the differences are symmetric about zero. | [06_05](html/06_05_nonparametric_tests.html) |
| Sign test | Test that the median difference is zero using only the signs of the differences; the number of positives is Binomial(n, 1/2) under H0. | [06_05](html/06_05_nonparametric_tests.html) |
| Permutation test | Test that obtains the null distribution of any statistic by recomputing it over all (or many random) relabellings of the data; exact when the labels are exchangeable. | [06_05](html/06_05_nonparametric_tests.html) |
| Kolmogorov-Smirnov test | Test based on D, the largest vertical gap between an empirical CDF and a hypothesised CDF (one sample) or another empirical CDF (two samples). | [06_05](html/06_05_nonparametric_tests.html) |
| Lilliefors correction | Correction for the KS test when the distribution's parameters are estimated from the same data; the critical value is smaller than the usual one. | [06_05](html/06_05_nonparametric_tests.html) |
| Kruskal-Wallis test | Rank-based analogue of one-way ANOVA for three or more groups. | [06_05](html/06_05_nonparametric_tests.html) |
| Asymptotic relative efficiency | Limiting ratio of the sample sizes two tests need for the same power; 0.955 for Wilcoxon against the t-test with Normal data, above 1 for heavy tails. | [06_05](html/06_05_nonparametric_tests.html) |
| Multiple testing problem | Running many tests makes false positives likely: m independent true nulls tested at level alpha give at least one false positive with probability 1 - (1 - alpha)^m. | [06_06](html/06_06_multiple_testing.html) |
| Family-wise error rate (FWER) | The probability of at least one false rejection among all the tests performed. | [06_06](html/06_06_multiple_testing.html) |
| False discovery rate (FDR) | The expected proportion of false rejections among all rejections, E[V / max(R, 1)]; a more lenient and more powerful goal than FWER control. | [06_06](html/06_06_multiple_testing.html) |
| Bonferroni correction | Reject a hypothesis if its p-value is at most alpha / m; controls the FWER under any dependence by the union bound, but loses power as m grows. | [06_06](html/06_06_multiple_testing.html) |
| Holm procedure | Step-down version of Bonferroni that tests the sorted p-values at alpha / (m - k + 1) and stops at the first failure; controls the FWER and is never less powerful than Bonferroni. | [06_06](html/06_06_multiple_testing.html) |
| Benjamini-Hochberg procedure | Step-up rule that rejects all hypotheses up to the largest k with p(k) <= k alpha / m; controls the FDR at (m0 / m) alpha for independent or positively dependent tests. | [06_06](html/06_06_multiple_testing.html) |
| Adjusted p-value (q-value) | The smallest error-control level at which a hypothesis would still be rejected; for BH, the minimum over j >= i of m p(j) / j. | [06_06](html/06_06_multiple_testing.html) |
| Tukey HSD | Post-hoc test for all pairwise differences of k group means using the studentised range distribution, with simultaneous error control. | [06_06](html/06_06_multiple_testing.html) |
| Winner's curse | The upward bias of the best result chosen among many noisy candidates, such as the highest validation score of many models. | [06_06](html/06_06_multiple_testing.html) |
| A/B test | A randomised experiment that compares a control version with a treatment version on a pre-chosen metric to estimate the causal effect of the change. | [06_07](html/06_07_ab_testing.html) |
| Primary metric | The single pre-registered metric on which the ship or don't-ship decision depends; secondary and guardrail metrics are judged with a multiple-testing correction. | [06_07](html/06_07_ab_testing.html) |
| Guardrail metric | A metric that must not get worse (for example latency or rounds played) even if the primary metric improves. | [06_07](html/06_07_ab_testing.html) |
| Minimum detectable effect (MDE) | The smallest true difference an experiment is designed to detect with the chosen power; the sample size grows with 1 / MDE squared. | [06_07](html/06_07_ab_testing.html) |
| Sample ratio mismatch (SRM) | A significant departure of the observed group sizes from the planned split (chi-square test on the counts); it signals broken randomisation or logging. | [06_07](html/06_07_ab_testing.html) |
| A/A test | An experiment with two identical versions, used to validate the pipeline: it should give p < 0.05 in 5 percent of runs and uniform p-values. | [06_07](html/06_07_ab_testing.html) |
| Relative lift | The effect expressed as a share of the control rate, (p_B - p_A) / p_A. | [06_07](html/06_07_ab_testing.html) |
| Peeking | Checking a running test repeatedly and stopping at the first significant result; it inflates the false-positive rate well above the nominal level. | [06_07](html/06_07_ab_testing.html) |
| Sequential testing | Designs such as alpha spending (O'Brien-Fleming boundaries) or always-valid p-values that allow repeated looks while keeping the overall error rate. | [06_07](html/06_07_ab_testing.html) |
| Risk | The probability of an event in a group, estimated by events divided by group size. | [06_08](html/06_08_risk_odds_ratio.html) |
| Relative risk (RR) | The ratio of the risk in the exposed group to the risk in the unexposed group, p1 / p0; its confidence interval is built on the log scale. | [06_08](html/06_08_risk_odds_ratio.html) |
| Odds ratio (OR) | The ratio of the odds p / (1 - p) in two groups, equal to ad / bc in a 2x2 table; it approximates the relative risk only for rare outcomes. | [06_08](html/06_08_risk_odds_ratio.html) |
| Number needed to treat (NNT) | The number of units that must be exposed for one extra (or one fewer) event: 1 / \\\|risk difference\\\|. | [06_08](html/06_08_risk_odds_ratio.html) |
| Fisher's exact test | Exact test for a 2x2 table that conditions on the margins; the count in one cell is Hypergeometric under the null hypothesis. | [06_08](html/06_08_risk_odds_ratio.html) |
| CUPED | Controlled-experiment Using Pre-Experiment Data: the metric is adjusted as Y - theta (X - mean X) with a pre-experiment covariate X, which cuts the variance by 1 - rho^2 without biasing the treatment effect. | [06_09](html/06_09_cuped_variance_reduction.html) |
| Variance reduction | Techniques that lower the variance of an experiment's estimate (covariate adjustment, stratification, control variates) so that fewer users are needed for the same power. | [06_09](html/06_09_cuped_variance_reduction.html) |
| Control variate | A variable with known mean that is correlated with the quantity of interest and is subtracted (with an optimal coefficient) to reduce the variance of an estimate. | [06_09](html/06_09_cuped_variance_reduction.html) |
| Pre-experiment covariate | A variable measured before the treatment is assigned, hence balanced across groups by randomisation and safe to adjust for. | [06_09](html/06_09_cuped_variance_reduction.html) |
| Wald test | Test based on the distance of the MLE from the null value in units of its estimated standard error: W = (theta_hat - theta_0)^2 I(theta_hat); simple but unreliable for small samples. | [06_10](html/06_10_likelihood_ratio_tests.html) |
| Score test | Test based on the slope (score) of the log-likelihood at the null value, S = U(theta_0)^2 / I(theta_0); needs only the null model and the Wilson interval is its inversion. | [06_10](html/06_10_likelihood_ratio_tests.html) |
| Likelihood-ratio test (LRT) | Test using twice the gap between the maximised log-likelihood and its value at the null, 2 (l(theta_hat) - l(theta_0)); approximately chi-square under the null and invariant to reparameterisation. | [06_10](html/06_10_likelihood_ratio_tests.html) |
| Nested models | Two models where the smaller is a special case of the larger (for example Exponential inside Gamma); the LRT compares them with a chi-square test whose degrees of freedom equal the number of extra parameters. | [06_10](html/06_10_likelihood_ratio_tests.html) |
| Profile likelihood interval | The set of parameter values whose likelihood-ratio statistic is below the chi-square critical value (3.84 for 95 percent with one parameter). | [06_10](html/06_10_likelihood_ratio_tests.html) |
