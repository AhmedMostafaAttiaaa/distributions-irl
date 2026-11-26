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
| Anomaly (outlier) | An observation that the usual process would almost never produce; defined relative to a model of normal behaviour. | [09_05](html/09_05_anomaly_detection.html) |
| z-score | The number of standard deviations an observation lies from the mean, (x - mean) / sd; a 3-sigma rule flags 0.27 % of normal data. | [09_05](html/09_05_anomaly_detection.html) |
| Robust z-score (MAD) | A z-score built on the median and the median absolute deviation, scaled by 0.6745 so that it matches the ordinary z for normal data; one outlier cannot ruin it. | [09_05](html/09_05_anomaly_detection.html) |
| Mahalanobis distance | The distance of a point from the centre of a cloud measured in units of the cloud's own covariance; its square is chi-square distributed for Gaussian data. | [09_05](html/09_05_anomaly_detection.html) |
| Masking | The effect by which outliers inflate the estimated spread of the data so that they no longer look unusual. | [09_05](html/09_05_anomaly_detection.html) |
| Minimum covariance determinant (MCD) | A robust estimate of centre and covariance from the subset of h points whose covariance matrix has the smallest determinant. | [09_05](html/09_05_anomaly_detection.html) |
| Breakdown point | The largest share of contaminated observations an estimator can tolerate before it can be moved arbitrarily far (0 for the mean, 50 % for the median). | [09_05](html/09_05_anomaly_detection.html) |
| False-alarm rate | The share of normal observations that a detector flags; the threshold is chosen to meet a false-alarm budget. | [09_05](html/09_05_anomaly_detection.html) |
| Base-rate effect on precision | When anomalies are rare, even a detector with a small false-alarm rate produces mostly false alerts: precision = recall x prevalence / (recall x prevalence + false-alarm rate x (1 - prevalence)). | [09_05](html/09_05_anomaly_detection.html) |
| Weight initialisation | The distribution from which a network's weights are drawn before training; its variance must keep the signal's variance roughly constant across layers. | [09_06](html/09_06_neural_net_randomness.html) |
| Xavier (Glorot) initialisation | Weights with variance 2 / (fan_in + fan_out) (or 1 / fan_in), designed to keep forward and backward signals stable for tanh and sigmoid units. | [09_06](html/09_06_neural_net_randomness.html) |
| He initialisation | Weights with variance 2 / fan_in, the correction of Xavier for ReLU units, which discard half the signal. | [09_06](html/09_06_neural_net_randomness.html) |
| Vanishing and exploding signals | The geometric shrinking or growth of activations and gradients with depth when the weight scale is not matched to the layer width. | [09_06](html/09_06_neural_net_randomness.html) |
| Dropout | Randomly setting units to zero during training with probability p and rescaling the rest by 1/(1-p), a Bernoulli multiplicative noise that regularises the network. | [09_06](html/09_06_neural_net_randomness.html) |
| Monte-Carlo dropout | Keeping dropout on at prediction time and averaging many stochastic passes; the spread of the passes is an approximate uncertainty. | [09_06](html/09_06_neural_net_randomness.html) |
| Deep ensemble | The average and spread of the predictions of several networks trained from different random seeds; a strong practical uncertainty estimate. | [09_06](html/09_06_neural_net_randomness.html) |
| Label smoothing | Replacing the 0/1 target by (1 - epsilon) times the one-hot vector plus epsilon / K, which gives a finite optimal logit gap and reduces over-confidence. | [09_06](html/09_06_neural_net_randomness.html) |
| Minibatch gradient noise | The sampling noise of a gradient computed on B examples, with standard deviation proportional to 1 / sqrt(B). | [09_06](html/09_06_neural_net_randomness.html) |
| Softmax temperature | A divisor T applied to the logits before the softmax: T < 1 sharpens the distribution towards the argmax, T > 1 flattens it towards uniform. | [09_07](html/09_07_llm_sampling.html) |
| Greedy decoding | Always choosing the most likely next token; deterministic and prone to repetition. | [09_07](html/09_07_llm_sampling.html) |
| Top-k sampling | Sampling only from the k most likely tokens after renormalising their probabilities. | [09_07](html/09_07_llm_sampling.html) |
| Top-p (nucleus) sampling | Sampling from the smallest set of most likely tokens whose total probability reaches p, so the number of candidates adapts to the model's confidence. | [09_07](html/09_07_llm_sampling.html) |
| Min-p sampling | Keeping only tokens whose probability is at least a fraction of the most likely token's probability. | [09_07](html/09_07_llm_sampling.html) |
| Truncation cost | Renormalising a distribution after keeping a set of probability mass m changes it by KL divergence -ln m. | [09_07](html/09_07_llm_sampling.html) |
| Gumbel-max trick | The identity that argmax(logit + Gumbel noise) is an exact sample from the softmax of the logits. | [09_07](html/09_07_llm_sampling.html) |
| Gumbel-softmax | A differentiable relaxation of categorical sampling that replaces the argmax by a softmax with temperature tau, trading bias against gradient variance. | [09_07](html/09_07_llm_sampling.html) |
| Perplexity | The exponential of the average negative log-probability per token; the effective number of equally likely next tokens. | [09_07](html/09_07_llm_sampling.html) |
| Distinct-n | The share of distinct n-grams among all n-grams of generated text, a simple measure of diversity. | [09_07](html/09_07_llm_sampling.html) |
| Variational autoencoder (VAE) | A generative model with an encoder that maps data to a distribution over a latent code and a decoder that maps codes back to data, trained by maximising the ELBO. | [09_08](html/09_08_vae.html) |
| Evidence lower bound (ELBO) | The expected log-likelihood of the data under the encoder minus the KL divergence of the encoder from the prior; a lower bound on the log-evidence whose gap is the KL to the true posterior. | [09_08](html/09_08_vae.html) |
| Latent variable | A hidden variable that is never observed but generates the data, such as the code of a VAE or the segment of a mixture model. | [09_08](html/09_08_vae.html) |
| Reparameterisation trick | Writing a sample as z = mu + sigma epsilon with parameter-free noise epsilon, so that gradients can flow through the sampling and have low variance. | [09_08](html/09_08_vae.html) |
| Score-function (REINFORCE) estimator | A gradient estimator of an expectation that multiplies the function value by the gradient of the log-density; unbiased but of high variance. | [09_08](html/09_08_vae.html) |
| Beta-VAE | A VAE whose KL term is weighted by beta, trading reconstruction quality against the information carried by the latent code. | [09_08](html/09_08_vae.html) |
| Posterior collapse | A latent dimension whose encoder distribution equals the prior for every input, carrying no information; its KL cost is zero. | [09_08](html/09_08_vae.html) |
| Active latent dimension | A latent dimension of a VAE whose average KL to the prior is above a small threshold (for example 0.05 nats). | [09_08](html/09_08_vae.html) |
| Amortised inference | Using one neural network (the encoder) to approximate the posterior of every data point instead of optimising each posterior separately. | [09_08](html/09_08_vae.html) |
