# Module 03 glossary

| Term | Definition | Lesson |
|---|---|---|
| Multivariate Normal | Joint distribution of a vector with mean vector mu and covariance matrix Sigma; density exp(-d^2/2) / ((2 pi)^(d/2) sqrt(det Sigma)). | [03_01](html/03_01_multivariate_normal.html) |
| Covariance matrix | Symmetric positive semi-definite matrix of variances and covariances. | [03_01](html/03_01_multivariate_normal.html) |
| Mahalanobis distance | Distance from the mean measured in standard deviations that account for correlation; d^2 is chi-square(d). | [03_01](html/03_01_multivariate_normal.html) |
| Eigendecomposition | Sigma = Q Lambda Q^T: principal axes (eigenvectors) and variances (eigenvalues). | [03_01](html/03_01_multivariate_normal.html) |
| Cholesky factor | Lower-triangular L with Sigma = L L^T; used to sample X = mu + L Z. | [03_01](html/03_01_multivariate_normal.html) |
| Whitening | Transforming to uncorrelated unit-variance variables. | [03_01](html/03_01_multivariate_normal.html) |
| Schur complement | Conditional covariance S_aa - S_ab S_bb^-1 S_ba of a Normal. | [03_01](html/03_01_multivariate_normal.html) |
| Diversification | Portfolio variance below the weighted average variance when correlation is below 1. | [03_01](html/03_01_multivariate_normal.html) |
| Dirichlet distribution | Distribution over probability vectors on the simplex; multi-category generalization of the Beta. | [03_02](html/03_02_dirichlet_multinomial.html) |
| Simplex | Set of probability vectors with non-negative entries summing to 1 (a triangle for 3 categories). | [03_02](html/03_02_dirichlet_multinomial.html) |
| Concentration (alpha_0) | Sum of the Dirichlet parameters; larger means draws cluster tightly around the mean. | [03_02](html/03_02_dirichlet_multinomial.html) |
| Dirichlet-Multinomial | Counts from a Multinomial whose probabilities are drawn from a Dirichlet; overdispersed. | [03_02](html/03_02_dirichlet_multinomial.html) |
| Pseudo-counts | Dirichlet parameters read as prior observations of each category. | [03_02](html/03_02_dirichlet_multinomial.html) |
| Laplace smoothing | Adding one pseudo-count to each category (Dirichlet(1,...,1) prior). | [03_02](html/03_02_dirichlet_multinomial.html) |
| Topic model (LDA) | Documents are mixtures of topics with Dirichlet-distributed proportions. | [03_02](html/03_02_dirichlet_multinomial.html) |
| Overdispersion factor | (n + alpha_0) / (1 + alpha_0): Dirichlet-Multinomial variance relative to Multinomial. | [03_02](html/03_02_dirichlet_multinomial.html) |
