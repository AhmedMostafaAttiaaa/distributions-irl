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
