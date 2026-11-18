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
| Mixture model | Density that is a weighted sum of component densities; data come from a hidden group chosen at random. | [03_03](html/03_03_gaussian_mixtures.html) |
| Mixing weights | Probabilities pi_k of each component; non-negative and summing to 1. | [03_03](html/03_03_gaussian_mixtures.html) |
| Responsibility | P(group k \| x): the posterior probability that a point came from component k. | [03_03](html/03_03_gaussian_mixtures.html) |
| EM algorithm | Expectation-Maximization: alternate computing responsibilities (E) and weighted parameter updates (M); likelihood never decreases. | [03_03](html/03_03_gaussian_mixtures.html) |
| Soft vs hard clustering | Probabilities of membership versus assigning each point to its most likely group. | [03_03](html/03_03_gaussian_mixtures.html) |
| BIC | Bayesian information criterion p ln n - 2 log-likelihood; lower is better; used to choose the number of components. | [03_03](html/03_03_gaussian_mixtures.html) |
| Law of total variance | Variance = average within-group variance + variance of the group means. | [03_03](html/03_03_gaussian_mixtures.html) |
| Label switching | Components have no natural order, so fitted groups can be permuted between runs. | [03_03](html/03_03_gaussian_mixtures.html) |
| Copula | A joint distribution on the unit square with Uniform marginals that carries only the dependence. | [03_04](html/03_04_copulas.html) |
| Sklar theorem | Any joint CDF is H(x, y) = C(F(x), G(y)) for marginals F, G and a copula C. | [03_04](html/03_04_copulas.html) |
| Gaussian copula | Copula of the multivariate Normal: Phi_rho(Phi^-1(u), Phi^-1(v)); no tail dependence. | [03_04](html/03_04_copulas.html) |
| Student-t copula | Copula with positive tail dependence: extremes cluster. | [03_04](html/03_04_copulas.html) |
| Clayton copula | Archimedean copula with lower-tail dependence 2^(-1/theta). | [03_04](html/03_04_copulas.html) |
| Kendall tau | Rank correlation based on concordant and discordant pairs; invariant to monotone transforms. | [03_04](html/03_04_copulas.html) |
| Spearman correlation | Pearson correlation of the ranks. | [03_04](html/03_04_copulas.html) |
| Tail dependence | Probability that one variable is extreme given the other is: lim P(V < q \| U < q). | [03_04](html/03_04_copulas.html) |
| Pseudo-observations | Ranks divided by n + 1, used to fit a copula. | [03_04](html/03_04_copulas.html) |
