# Module 09: Probabilistic modelling

How the distributions of Modules 01-08 become working models: losses as likelihoods, generalised linear models, naive Bayes on real text, density estimation and mixtures, anomaly detection, the randomness of neural networks, LLM sampling, VAEs, diffusion, Gaussian processes, reinforcement-learning policies, priors as regularisers, the bias-variance trade-off and uncertainty with conformal prediction.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 09_01 Loss functions as likelihoods | [notebook](notebooks/09_01_losses_as_likelihoods.ipynb) | [page](html/09_01_losses_as_likelihoods.html) | done |
| 09_02 Generalised linear models | [notebook](notebooks/09_02_glms.ipynb) | [page](html/09_02_glms.html) | done |
| 09_03 Naive Bayes | [notebook](notebooks/09_03_naive_bayes.ipynb) | [page](html/09_03_naive_bayes.html) | done |
| 09_04 Density estimation: KDE, Gaussian mixtures and EM | [notebook](notebooks/09_04_density_estimation_kde_gmm_em.ipynb) | [page](html/09_04_density_estimation_kde_gmm_em.html) | done |
| 09_05 Anomaly detection | [notebook](notebooks/09_05_anomaly_detection.ipynb) | [page](html/09_05_anomaly_detection.html) | done |
| 09_06 The randomness inside neural networks | [notebook](notebooks/09_06_neural_net_randomness.ipynb) | [page](html/09_06_neural_net_randomness.html) | done |
| 09_07 How language models sample | [notebook](notebooks/09_07_llm_sampling.ipynb) | [page](html/09_07_llm_sampling.html) | done |
| 09_08 Variational autoencoders | [notebook](notebooks/09_08_vae.ipynb) | [page](html/09_08_vae.html) | done |
| 09_09 Diffusion models | [notebook](notebooks/09_09_diffusion_noise.ipynb) | [page](html/09_09_diffusion_noise.html) | done |
| 09_10 Gaussian processes | [notebook](notebooks/09_10_gaussian_processes.ipynb) | [page](html/09_10_gaussian_processes.html) | done |
| 09_11 Reinforcement learning policies | [notebook](notebooks/09_11_rl_policies.ipynb) | [page](html/09_11_rl_policies.html) | done |
| 09_12 Priors as regularisers | [notebook](notebooks/09_12_priors_as_regularisers.ipynb) | [page](html/09_12_priors_as_regularisers.html) | done |

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (calculators, simulators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Every model is written from scratch in NumPy (no scikit-learn or deep-learning framework needed), so each formula can be followed line by line and checked against the theory.
- Each lesson has several worked examples with numbers, many figures (2D and 3D), an "In plain words" cell after each derivation and an interactive page.
- Prerequisites: Modules 02 (continuous), 03 (multivariate), 06 (likelihood) and 08 (entropy, KL).
