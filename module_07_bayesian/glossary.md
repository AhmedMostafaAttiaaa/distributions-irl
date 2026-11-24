# Module 07 glossary

| Term | Definition | Lesson |
|---|---|---|
| Prior | A probability distribution for a parameter that expresses what is believed before seeing the data. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Likelihood | The probability (density) of the observed data viewed as a function of the parameter. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Posterior | The distribution of the parameter after seeing the data: proportional to likelihood times prior. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Evidence (marginal likelihood) | The probability of the data averaged over the prior, p(x) = integral of p(x \\\\| theta) p(theta); the normalising constant of the posterior and the basis of Bayes factors. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Conjugate prior | A prior family whose posterior is in the same family, so updating only changes the parameters (Beta-Binomial, Gamma-Poisson, Normal-Normal). | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Beta-Binomial model | Binomial data with a Beta(a, b) prior on the success probability; the posterior is Beta(a + successes, b + failures). | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Gamma-Poisson model | Poisson counts with a Gamma(alpha, beta) prior on the rate; the posterior is Gamma(alpha + events, beta + exposure). | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Normal-Normal model | Normal data with known variance and a Normal prior on the mean; precisions add and the posterior mean is the precision-weighted average. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Shrinkage | The pull of the posterior mean from the data estimate towards the prior mean; strong for small samples and weak for large ones. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| MAP estimate | The posterior mode: the parameter value maximising log-likelihood plus log-prior, equal to the MLE plus a penalty. | [07_01](html/07_01_bayesian_updating_conjugates.html) |
| Credible interval | An interval that contains the parameter with a stated posterior probability (for example 95 percent), given the prior and the data. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Highest-density interval (HDI) | The shortest credible interval of a given mass; every point inside has higher posterior density than every point outside. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Posterior predictive distribution | The distribution of new data given the observed data, obtained by averaging the data model over the posterior of the parameter. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Beta-Binomial distribution | The distribution of the number of successes in m trials when the success probability has a Beta prior or posterior; wider than a Binomial with the same mean. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Region of practical equivalence (ROPE) | A range of effect sizes too small to matter in practice; decisions use the posterior probability that the effect lies inside, below or above it. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Expected loss | The posterior average of the amount lost by a decision, for example E[max(theta_A - theta_B, 0)] when choosing B. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Probability of being best | The posterior probability that a given variant has the highest true rate among several, estimated by Monte Carlo from joint posterior draws. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Bayesian A/B test | An A/B analysis based on the posterior of each variant: probability of direction, expected loss, ROPE and probability of being best instead of a p-value. | [07_02](html/07_02_credible_intervals_predictive.html) |
| Markov chain Monte Carlo (MCMC) | A family of algorithms that draw dependent samples from a target distribution, known only up to a constant, using a Markov chain whose long-run distribution is the target. | [07_03](html/07_03_mcmc_metropolis.html) |
| Metropolis algorithm | Random-walk MCMC: propose a step, accept it with probability min(1, target ratio), otherwise stay; needs only the unnormalised density. | [07_03](html/07_03_mcmc_metropolis.html) |
| Detailed balance | The condition pi(a) P(a to b) = pi(b) P(b to a) for a Markov chain, which guarantees that pi is stationary. | [07_03](html/07_03_mcmc_metropolis.html) |
| Burn-in | The initial draws of a chain, discarded because the chain has not yet reached the target distribution. | [07_03](html/07_03_mcmc_metropolis.html) |
| Acceptance rate | The share of proposals accepted by a Metropolis sampler; about 0.2 to 0.4 indicates a well-tuned step size. | [07_03](html/07_03_mcmc_metropolis.html) |
| Effective sample size (ESS) | The number of independent draws with the same precision as the correlated chain: N / (1 + 2 times the sum of autocorrelations). | [07_03](html/07_03_mcmc_metropolis.html) |
| R-hat (Gelman-Rubin) | A convergence diagnostic comparing between-chain and within-chain variance of several chains; values above about 1.01 signal non-convergence. | [07_03](html/07_03_mcmc_metropolis.html) |
| Hamiltonian Monte Carlo | MCMC that uses the gradient of the log-density to make long, efficient proposals; the NUTS variant is the default in Stan and PyMC. | [07_03](html/07_03_mcmc_metropolis.html) |
| Multi-armed bandit | A sequential decision problem in which one of several options (arms) with unknown reward probabilities is chosen at each step, trading off exploration against exploitation. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Exploration-exploitation trade-off | The tension between trying uncertain options to learn about them and using the option that currently looks best to earn reward. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Regret | The cumulative reward lost relative to always choosing the best arm: the sum over steps of p_best minus the chosen arm's rate. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Thompson sampling | A bandit policy that draws a plausible rate for each arm from its posterior and plays the arm with the highest draw, so each arm is played with its posterior probability of being best. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Epsilon-greedy | A bandit policy that plays a random arm with probability epsilon and the empirically best arm otherwise. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Upper confidence bound (UCB) | A bandit policy that plays the arm with the highest optimistic estimate: observed mean plus an exploration bonus that shrinks with the number of pulls. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Lai-Robbins bound | The asymptotic lower bound on the regret of any consistent bandit policy: the sum over suboptimal arms of gap / KL divergence times ln T. | [07_04](html/07_04_thompson_sampling_bandits.html) |
| Contextual bandit | A bandit in which the best arm depends on observed features of the user or situation, as in personalised recommendation. | [07_04](html/07_04_thompson_sampling_bandits.html) |
