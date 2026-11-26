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
| Naive Bayes | A classifier that applies Bayes' rule with the assumption that the features are independent given the class, so the log-odds are the prior log-odds plus a sum of per-feature votes. | [09_03](html/09_03_naive_bayes.html) |
| Multinomial naive Bayes | Naive Bayes for count features (word counts), with class-conditional word probabilities estimated by smoothed counts. | [09_03](html/09_03_naive_bayes.html) |
| Bernoulli naive Bayes | Naive Bayes for presence/absence features, where absent words also contribute evidence. | [09_03](html/09_03_naive_bayes.html) |
| Gaussian naive Bayes | Naive Bayes for continuous features, each modelled as a normal distribution within each class. | [09_03](html/09_03_naive_bayes.html) |
| Laplace smoothing | Adding alpha pseudo-counts to every count, equivalent to the posterior mean under a symmetric Dirichlet prior; it prevents zero probabilities for unseen words. | [09_03](html/09_03_naive_bayes.html) |
| Generative and discriminative models | A generative model describes how the features arise within each class (naive Bayes); a discriminative model fits the probability of the class given the features directly (logistic regression). | [09_03](html/09_03_naive_bayes.html) |
| Log-odds score | The logarithm of P(class 1)/P(class 0) given the data; a sum of evidence terms whose sign gives the decision and whose size the confidence. | [09_03](html/09_03_naive_bayes.html) |
| Precision and recall | Precision is the share of flagged items that are truly positive; recall is the share of true positives that are flagged. | [09_03](html/09_03_naive_bayes.html) |
| ROC AUC | The area under the ROC curve; equal to the probability that a random positive example scores higher than a random negative one. | [09_03](html/09_03_naive_bayes.html) |
| Kernel density estimate (KDE) | A nonparametric density estimate that places a small bump (kernel) on every observation and averages them; the bump width is the bandwidth. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| Bandwidth | The width of the kernel in a KDE; small values follow the noise (high variance), large values blur real structure (high bias); the optimal value shrinks like n^(-1/5). | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| Gaussian mixture model (GMM) | A density that is a weighted sum of normal distributions, equivalent to picking a hidden segment first and then drawing from that segment's normal. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| EM algorithm | Expectation-maximisation: alternately compute the soft membership of each observation (E-step) and re-estimate the parameters from those weighted memberships (M-step); the likelihood never decreases. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| Responsibility | The probability that an observation belongs to a given mixture component, given the data and the current parameters. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| Soft clustering | Assigning each observation a probability of belonging to every cluster instead of a single label. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| K-means | A hard clustering that alternates assigning points to the nearest centre and recomputing centres; the zero-variance, equal-spherical limit of a Gaussian mixture. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| BIC and AIC | Information criteria that penalise the log-likelihood by the number of parameters (BIC: p ln n, AIC: 2p) to choose between models such as numbers of mixture components. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
| Label switching | The fact that the components of a mixture can be permuted without changing the likelihood, so component numbers are arbitrary. | [09_04](html/09_04_density_estimation_kde_gmm_em.html) |
