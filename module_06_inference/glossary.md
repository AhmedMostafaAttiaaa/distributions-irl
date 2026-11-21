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
