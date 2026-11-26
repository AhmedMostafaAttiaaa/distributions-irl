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
