# plan.md — Progress Tracker & Module Specs

This is the shared to-do list for all devices. Follow the session protocol in `CLAUDE.md` §2: **pull, claim, commit and push the claim, then work**. Tick checkboxes and commit after every lesson.

**Status legend:** ⬜ not started · 🟨 in progress · ✅ done · 🔁 needs review/fix

---

## Progress overview

| # | Module | Status | Device | Started | Finished |
|---|--------|--------|--------|---------|----------|
| P0 | Repo scaffold | ✅ | LAPTOP-1 | 2026-11-16 | 2026-11-16 |
| 00 | Foundations | ⬜ | | | |
| 01 | Discrete distributions | 🟨 | LAPTOP-1 | 2026-11-16 | |
| 02 | Continuous distributions | ⬜ | | | |
| 03 | Multivariate distributions | ⬜ | | | |
| 04 | Relationships between distributions | ⬜ | | | |
| 05 | Sampling & limit theorems | ⬜ | | | |
| 06 | Statistical inference | ⬜ | | | |
| 07 | Bayesian thinking | ⬜ | | | |
| 08 | Information theory | ⬜ | | | |
| 09 | Distributions inside ML & AI | ⬜ | | | |
| 10 | Model evaluation & confusion matrix | ⬜ | | | |
| 11 | Data science in practice | ⬜ | | | |
| 12 | Sampling algorithms | ⬜ | | | |
| 13 | Capstone projects | ⬜ | | | |
| FB | Final: HTML book (index + glossary) | ⬜ | | | |

Per-lesson checkbox key used below: **NB** notebook done & executes clean · **EX** worked example done, asserts pass · **3D** 3D plots done · **HTML** interactive page done, no console errors · **GIT** committed & pushed

---

## Phase 0 — Repo scaffold (do once, before any module)

- [x] Git identity set locally (`CLAUDE.md` §11 Authorship); `.claude/settings.json` present with attribution off
- [x] Folder structure per `CLAUDE.md` §3
- [x] `README.md`: project overview, how to set up the env, how to open notebooks and HTML pages
- [x] `requirements.txt` (base deps) and `.gitignore` (.venv, checkpoints, `__pycache__`, large data)
- [x] `common/style.py`: colorblind-safe palette + rcParams
- [x] `templates/lesson_template.ipynb` with all §4 section headers as markdown cells
- [x] `templates/lesson_template.html`: layout, CSS (light/dark), nav bar, slider component, vanilla-JS SVG bar/line chart helpers, histogram helper, KaTeX include, optional Plotly gl3d loader
- [x] `index.html` skeleton: book title, list of modules (unbuilt ones greyed out), same styling as the template
- [x] Commit `scaffold: repo structure and templates` and push

---

## Module 00 — Foundations `(draft)`

**Goal:** the vocabulary every later module uses. **Data:** synthetic only.

- [ ] 00_01 random_variables — discrete vs continuous, PMF/PDF/CDF, quantiles/PPF, survival function. *Example:* dice and waiting-time measurements. NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐
- [ ] 00_02 expectation_moments — expectation, variance, moments, skewness, kurtosis, MGF. *Example:* expected profit of a raffle / insurance policy. NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐
- [ ] 00_03 joint_conditional — joint, marginal, conditional, independence, covariance, correlation; 3D joint surfaces. *Example:* height vs weight. NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐
- [ ] 00_04 transformations — functions of random variables, change of variables, linear transforms, z-scores. NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐
- [ ] 00_05 bayes_theorem — conditional probability, Bayes, total probability. *Example:* medical test with 1% prevalence (sets up the confusion matrix in Module 10). NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐

---

## Module 01 — Discrete distributions

**Goal:** master every common discrete distribution: how it's generated, its full math, how to compute with it, and where it shows up in stats / DS / ML.
**3D theme:** PMF as 3D bars or a surface over (k, parameter) for every lesson.
**Data:** mostly synthetic with realistic numbers. Real data in 01_03 (football goals) and 01_06 (word frequencies from a book).

### 01_01 bernoulli_binomial
- Content: Bernoulli trial → sum of n independent trials = Binomial. Full derivation of PMF (counting argument), mean np, variance np(1−p), PGF/MGF. Shape vs n and p. Normal approximation preview (with continuity correction).
- 3D: Binomial PMF over (k, p) for fixed n; second plot over (k, n) for fixed p.
- **Worked example:** an online store has **1,000 visitors/day** and a **3.2 % conversion rate**. Questions: expected orders and SD; P(≥ 45 orders); P(25 ≤ X ≤ 40); how many orders to plan inventory for so that a stock-out happens on only 5 % of days (use the PPF). Shade the regions; simulate 10,000 days.
- Second example: QC with a 2 % defect rate in boxes of 50, P(box has ≥ 3 defects).
- Used in: A/B testing (conversion counts), binary labels & logistic regression likelihood, dropout masks (Bernoulli), ensemble majority voting.
- HTML: sliders n, p; PMF + CDF; range calculator; sample button; editable store example.
- NB ☑ EX ☑ 3D ☑ HTML ☑ GIT ☑

### 01_02 geometric_negative_binomial
- Content: trials until the first success (Geometric; mention both the "trials" and "failures" conventions and which one scipy uses); memorylessness proof; trials until the r-th success (Negative Binomial); NB as an overdispersed alternative to Poisson (Gamma–Poisson mixture, intuition only, full treatment in 07).
- 3D: Geometric PMF over (k, p); Negative Binomial PMF over (k, r).
- **Worked example:** a sales rep closes **15 %** of calls. Expected calls to the first sale; P(first sale within 5 calls); calls needed to reach **5 sales** (mean, SD, 90th percentile) to set daily targets.
- Second example: insurance claim counts with variance > mean, fitting NB vs Poisson.
- Used in: churn/retention ("how many periods until a customer leaves"), retry/backoff modeling, overdispersed count regression, RNA-seq counts.
- HTML: toggle Geometric / NegBin; sliders p, r; memorylessness demo.
- NB ☑ EX ☑ 3D ☑ HTML ☑ GIT ☑

### 01_03 poisson
- Content: Poisson as the limit of Binomial (n → ∞, np = λ), derived step by step; mean = variance = λ; sum of Poissons; Poisson process link to Exponential (preview of 02); goodness of fit by eye and with a chi-square preview.
- 3D: PMF over (k, λ); Binomial → Poisson convergence surface.
- **Worked example:** a call center receives **12 calls/hour** on average. P(> 20 calls in an hour); P(0 calls in 10 minutes); the minimum capacity so that the hour is overloaded less than 5 % of the time.
- **Real data:** goals per match from a public football season CSV (e.g. football-data.co.uk, English Premier League). Fit λ, compare observed vs Poisson frequencies, plot both. Document the source in `data/README.md` and add `download_data.py`.
- Used in: web traffic & server load, defect counts, Poisson regression (GLM), event rates in A/B tests, the count likelihood in recommender models.
- HTML: λ slider; Binomial-vs-Poisson comparison toggle (n slider); call-center calculator.
- NB ☑ EX ☑ 3D ☑ HTML ☑ GIT ☑

### 01_04 hypergeometric
- Content: sampling without replacement; PMF derivation by counting; mean and variance with the finite-population correction; when Binomial is a good approximation (n ≪ N); link to Fisher's exact test.
- 3D: PMF over (k, K) for fixed N, n.
- **Worked example:** a lot of **500 items** contains **25 defectives**; an inspector samples **20**. P(no defectives found); P(≥ 2); the sample size needed so that P(detect ≥ 1) ≥ 95 %. Compare with the Binomial approximation.
- Second example: a card game, e.g. P(≥ 2 aces in a 5-card hand).
- Used in: audit sampling, Fisher's exact test, gene-set enrichment analysis, lottery odds.
- HTML: sliders N, K, n; Hypergeometric vs Binomial overlay.
- NB ☑ EX ☑ 3D ☑ HTML ☑ GIT ☑

### 01_05 uniform_categorical_multinomial
- Content: discrete uniform; categorical (one draw, k classes); multinomial (n draws); covariance between category counts (negative); marginals are Binomial; link to softmax outputs and one-hot labels; chi-square goodness-of-fit preview.
- 3D: multinomial with 3 categories, probabilities over (x₁, x₂) with x₃ = n − x₁ − x₂ as 3D bars over the simplex.
- **Worked example:** **1,200 customers** choose between 4 subscription plans with probabilities **(0.40, 0.30, 0.20, 0.10)**. Expected count per plan; P(plan D gets ≥ 150 customers); is an observed split (450, 380, 240, 130) consistent with these probabilities? Plot observed vs expected.
- Second example: is a die fair? (600 rolls).
- Used in: classifier outputs (softmax = categorical), cross-entropy loss, bag-of-words / Naive Bayes, LLM next-token sampling (preview), survey analysis.
- HTML: probability sliders that renormalize; draw n samples; 3-category simplex 3D view.
- NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐

### 01_06 zipf_power_laws
- Content: Zipf / zeta distribution; power laws and log-log plots; heavy tails in discrete data; why the mean/variance may not exist for small exponents; rank-frequency vs frequency-count views.
- 3D: PMF over (rank, exponent s).
- **Real data / worked example:** word frequencies in a public-domain book from Project Gutenberg (e.g. *Pride and Prejudice*). Tokenize, count, rank-frequency log-log plot, estimate s, and answer: what share of all words do the top 10 / top 100 words cover? Document the source in `data/README.md` and add `download_data.py`.
- Used in: NLP vocabulary & tokenization, long-tail recommendations, city sizes, popularity / cache design.
- HTML: s slider; linear vs log-log toggle; "top-N coverage" calculator; embed the precomputed book word counts (top ~500) as JSON.
- NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐

### 01_07 discrete_summary_chooser
- Content: comparison table of all Module 01 distributions; a "which discrete distribution?" decision flowchart; relationships map (Bernoulli → Binomial → Poisson; Geometric → NegBin; Hypergeometric → Binomial); mixed practice problems with solutions.
- 3D: optional side-by-side PMF surfaces.
- **Worked example:** 5 short real scenarios. For each, identify the distribution, justify it, and compute one probability.
- HTML: an interactive chooser (answer yes/no questions → recommended distribution with a live mini plot) plus the relationship map.
- NB ☐ EX ☐ 3D ☐ HTML ☐ GIT ☐

### Module 01 wrap-up
- [ ] `module_01_discrete/README.md` and `glossary.md` complete
- [ ] Root `index.html` links to all 7 lesson pages; prev/next links verified
- [ ] Status ✅ in the overview table; committed and pushed

---

## Module 02 — Continuous distributions `(draft)`

**3D theme:** PDF over (x, parameter). **Data:** synthetic plus small real sets (e.g. seaborn `tips`, latency/income samples). Decide per lesson.

- [ ] 02_01 uniform_normal — z-scores, 68-95-99.7 rule. *Example:* exam scores / manufacturing tolerances.
- [ ] 02_02 lognormal — *Example:* house prices or response latencies.
- [ ] 02_03 exponential_gamma_erlang — waiting times, the Poisson-process link. *Example:* time between customer arrivals.
- [ ] 02_04 beta — probabilities of probabilities. *Example:* uncertainty about a conversion rate.
- [ ] 02_05 weibull — reliability. *Example:* time to failure of hard drives.
- [ ] 02_06 heavy_tails_pareto_cauchy — *Example:* wealth distribution; why the sample mean of a Cauchy never settles.
- [ ] 02_07 laplace_logistic_gumbel — *Example:* L1 errors; the sigmoid's origin; maximum yearly rainfall.
- [ ] 02_08 t_chisquare_f — sampling distributions. *Example:* small-sample quality test.
- [ ] 02_09 von_mises — circular data. *Example:* wind direction / hour-of-day activity.
- [ ] 02_10 continuous_summary_chooser

---

## Module 03 — Multivariate distributions `(draft)`

**3D theme:** the showcase module (surfaces, contour ellipses, the simplex).

- [ ] 03_01 multivariate_normal — covariance ellipses, conditional/marginal, Mahalanobis. *Example:* height–weight data.
- [ ] 03_02 dirichlet_multinomial — the simplex in 3D, LDA intuition. *Example:* topic mixtures.
- [ ] 03_03 gaussian_mixtures — *Real data:* Old Faithful eruptions (bimodal).
- [ ] 03_04 copulas — dependence separate from marginals. *Example:* two correlated asset returns.

---

## Module 04 — Relationships between distributions `(draft)`

- [ ] 04_01 relationship_map — **interactive graph HTML** of all distributions in 01–03 with edges (limit, special case, sum, transform, conjugate); click an edge to see a demo.
- [ ] 04_02 limits_and_approximations — Binomial→Poisson→Normal, Gamma→Normal, t→Normal with error plots.

---

## Module 05 — Sampling & limit theorems `(draft)`

- [ ] 05_01 law_of_large_numbers — animated convergence.
- [ ] 05_02 central_limit_theorem — sample means from any distribution → Normal; interactive "pick a parent distribution".
- [ ] 05_03 sampling_distributions_standard_error
- [ ] 05_04 bootstrap_monte_carlo — *Example:* CI for a median delivery time.

---

## Module 06 — Statistical inference `(draft)`

- [ ] 06_01 estimation_mle_mom — 3D likelihood surfaces.
- [ ] 06_02 confidence_intervals — coverage simulation.
- [ ] 06_03 hypothesis_testing_core — null distribution, p-value, α, β, power, Type I/II errors (link to Module 10).
- [ ] 06_04 common_tests — t-tests, chi-square, ANOVA/F.
- [ ] 06_05 nonparametric_tests — Mann–Whitney, KS, permutation tests.
- [ ] 06_06 multiple_testing — Bonferroni, Benjamini–Hochberg.
- [ ] 06_07 ab_testing — *Real data:* a public A/B test dataset (e.g. Kaggle "A/B testing" landing-page data). Sample size, power, decision.

---

## Module 07 — Bayesian thinking `(draft)`

- [ ] 07_01 bayesian_updating_conjugates — Beta–Binomial, Gamma–Poisson, Normal–Normal; animated updating.
- [ ] 07_02 credible_intervals_posterior_predictive
- [ ] 07_03 mcmc_metropolis — a sampler walking a 3D surface.
- [ ] 07_04 thompson_sampling_bandits — *Example:* choosing between 3 ad creatives.

---

## Module 08 — Information theory `(draft)`

- [ ] 08_01 entropy_cross_entropy — *Example:* why cross-entropy is the classification loss.
- [ ] 08_02 kl_js_divergence — two-Gaussian interactive, asymmetry demo.
- [ ] 08_03 wasserstein_distance — GAN motivation.
- [ ] 08_04 mutual_information — feature selection example.

---

## Module 09 — Distributions inside ML & AI `(draft)`

**Data:** sklearn datasets, SMS Spam Collection (UCI), MNIST if needed (extra deps in `module_09/requirements.txt`).

- [ ] 09_01 losses_as_likelihoods — MSE↔Gaussian, MAE↔Laplace, CE↔Bernoulli/Categorical, Poisson loss.
- [ ] 09_02 glms — logistic and Poisson regression, link functions.
- [ ] 09_03 naive_bayes — Gaussian / Multinomial / Bernoulli NB. *Real data:* SMS spam.
- [ ] 09_04 density_estimation_kde_gmm_em
- [ ] 09_05 anomaly_detection — z-score, Mahalanobis, multivariate Gaussian.
- [ ] 09_06 neural_net_randomness — Xavier/He init, dropout, label smoothing, MC-dropout uncertainty.
- [ ] 09_07 llm_sampling — softmax temperature, top-k, top-p, Gumbel-max / Gumbel-softmax.
- [ ] 09_08 vae — reparameterization, Gaussian KL, 2D/3D latent space.
- [ ] 09_09 diffusion_noise — forward Gaussian noising schedule visualized.
- [ ] 09_10 gaussian_processes — distributions over functions, prior/posterior.
- [ ] 09_11 rl_policies — stochastic policies, exploration.

---

## Module 10 — Model evaluation & the confusion matrix `(draft)`

**Signature visual:** two overlapping score distributions (positives vs negatives) with a draggable threshold → live confusion matrix, metrics, ROC point.

- [ ] 10_01 confusion_matrix_from_distributions
- [ ] 10_02 classification_metrics — precision, recall, specificity, F1, MCC, Cohen's kappa.
- [ ] 10_03 roc_auc_pr_curves — built from the distributions; AUC as a probability.
- [ ] 10_04 thresholds_and_costs — cost-sensitive threshold choice.
- [ ] 10_05 base_rate_fallacy — medical test (links to 00_05).
- [ ] 10_06 calibration — reliability diagrams, Brier score, log loss.
- [ ] 10_07 multiclass_confusion_matrix
- [ ] 10_08 regression_residual_diagnostics — residual distributions, Q-Q plots, prediction intervals.
- *Real data:* sklearn breast cancer; optionally Kaggle credit-card fraud (large → gitignored + download script).

---

## Module 11 — Data science in practice `(draft)`

- [ ] 11_01 eda_distributions — histograms, KDE, ECDF, box/violin, Q-Q.
- [ ] 11_02 fitting_distributions — `scipy.stats.fit`, AIC/BIC, KS goodness of fit.
- [ ] 11_03 transformations — log, Box–Cox, Yeo–Johnson.
- [ ] 11_04 outliers_heavy_tails
- [ ] 11_05 data_drift — KS test, PSI.
- [ ] 11_06 class_imbalance
- [ ] 11_07 survival_analysis — Kaplan–Meier, Weibull. *Real data:* Telco customer churn.
- [ ] 11_08 queueing — Poisson arrivals, M/M/1 & M/M/c.
- [ ] 11_09 synthetic_data_generation

---

## Module 12 — Sampling algorithms `(draft)`

- [ ] 12_01 inverse_transform_box_muller
- [ ] 12_02 rejection_importance_sampling
- [ ] 12_03 monte_carlo_integration — estimating π, high-dimensional integrals.

---

## Module 13 — Capstone projects `(draft)`

- [ ] 13_01 ab_test_end_to_end
- [ ] 13_02 spam_classifier_naive_bayes
- [ ] 13_03 fraud_anomaly_detector
- [ ] 13_04 bayesian_bandit_simulator
- [ ] 13_05 vae_latent_explorer

---

## Final — HTML book `(draft)`

- [ ] `index.html`: full table of contents (modules → lessons), search box (client-side), progress badges
- [ ] `glossary.html`: merge all `module_XX/glossary.md` into one alphabetical, searchable glossary with links to lessons
- [ ] Consistent nav on every page (index · prev · next · glossary)
- [ ] Link check across all pages
- [ ] Optional: export the book as a single zip / PDF
