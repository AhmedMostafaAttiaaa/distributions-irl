# Module 09 glossary

| Term | Definition | Lesson |
|---|---|---|
| Negative log-likelihood (loss) | The sum of minus the log-probability of the data under a model; minimising it is maximum likelihood, and every standard loss is one for some noise distribution. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Mean squared error (MSE) | The average squared residual; the Gaussian negative log-likelihood with fixed variance, minimised by the mean. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Mean absolute error (MAE) | The average absolute residual; the Laplace negative log-likelihood, minimised by the median and robust to outliers. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Huber loss | Squared for small residuals and linear for large ones, so it behaves like the mean near the centre and like the median in the tails. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Pinball (quantile) loss | The asymmetric absolute loss max(tau r, (tau - 1) r) whose minimiser is the tau-quantile; the asymmetric Laplace negative log-likelihood. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Quantile regression | Regression that models a chosen conditional quantile (for example the 90th percentile) by minimising the pinball loss. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Poisson loss | The negative log-likelihood of count data, lambda - y ln lambda, usually with a log link so that predicted rates are positive. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Proper scoring rule | A loss for probability forecasts that is minimised in expectation only by the true probabilities, such as log loss and the Brier score. | [09_01](html/09_01_losses_as_likelihoods.html) |
| Generalised linear model (GLM) | A regression with an exponential-family outcome distribution, a linear predictor and a link function connecting the mean to the predictor. | [09_02](html/09_02_glms.html) |
| Link function | The function g with g(mean) = linear predictor, such as the logit for probabilities or the log for rates; its inverse keeps predictions in the allowed range. | [09_02](html/09_02_glms.html) |
| Logistic regression | A GLM for a yes/no outcome with the logit link; each coefficient is a log odds ratio. | [09_02](html/09_02_glms.html) |
| Odds ratio | The factor by which the odds of an outcome are multiplied per unit change of a predictor, exp(beta) in logistic regression. | [09_02](html/09_02_glms.html) |
| Poisson regression | A GLM for counts with the log link; exp(beta) is the rate ratio, and exposure enters as an offset. | [09_02](html/09_02_glms.html) |
| Offset (exposure) | A known term, such as the log of the observation time, added to the linear predictor with coefficient fixed at 1 so that the model describes rates. | [09_02](html/09_02_glms.html) |
| Iteratively reweighted least squares (IRLS) | Newton's method for GLMs: repeated weighted least-squares fits to a working response until the coefficients stop changing. | [09_02](html/09_02_glms.html) |
| Overdispersion | Variance larger than the model allows (for counts, larger than the mean); it makes Poisson standard errors too small and is handled by the negative binomial or quasi-likelihood. | [09_02](html/09_02_glms.html) |
| Deviance | Twice the gap between the log-likelihood of the saturated model and the fitted model; the GLM analogue of the residual sum of squares. | [09_02](html/09_02_glms.html) |
