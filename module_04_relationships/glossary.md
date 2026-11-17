# Module 04 glossary

| Term | Definition | Lesson |
|---|---|---|
| Sum of independent variables | Mechanism that adds independent copies; generating functions multiply (Bernoulli to Binomial, Exponential to Gamma). | [04_01](html/04_01_relationship_map.html) |
| Transformation | Applying a function to a variable (exp of a Normal is Lognormal; -ln U is Exponential). | [04_01](html/04_01_relationship_map.html) |
| Limit (convergence in distribution) | A sequence of distributions approaching another as a parameter grows (Binomial to Poisson to Normal). | [04_01](html/04_01_relationship_map.html) |
| Special case | A family with a fixed parameter equals a smaller family (Exponential = Gamma(1)). | [04_01](html/04_01_relationship_map.html) |
| Mixture | Distribution obtained by letting a parameter be random (Gamma-Poisson = Negative Binomial). | [04_01](html/04_01_relationship_map.html) |
| Conditioning | The law of a variable given an event or another variable (Poisson given the sum is Binomial). | [04_01](html/04_01_relationship_map.html) |
| Thinning | Keeping each event of a Poisson process independently with probability q gives another Poisson process. | [04_01](html/04_01_relationship_map.html) |
| Overdispersion | Variance larger than the mean, produced by mixing Poisson rates. | [04_01](html/04_01_relationship_map.html) |
| Total variation distance | Half the sum of absolute differences between two PMFs; 0 means identical and it bounds the error of any event probability. | [04_01](html/04_01_relationship_map.html) |
| Kolmogorov-Smirnov test | Test comparing a sample with a distribution through the largest CDF gap. | [04_01](html/04_01_relationship_map.html) |
| Le Cam bound | Total variation distance between Binomial(n,p) and Poisson(np) is at most n p^2 | [04_02](html/04_02_limits_and_approximations.html) |
| Berry-Esseen bound | Kolmogorov distance of a standardized sum from the Normal is at most C rho / (sigma^3 sqrt(n)), C <= 0.4748 | [04_02](html/04_02_limits_and_approximations.html) |
| Kolmogorov distance | Largest gap between two CDFs | [04_02](html/04_02_limits_and_approximations.html) |
| Continuity correction | Adding 0.5 when approximating a discrete count by a Normal | [04_02](html/04_02_limits_and_approximations.html) |
| Wilson-Hilferty | Cube-root Normal approximation for chi-square and Gamma | [04_02](html/04_02_limits_and_approximations.html) |
| Finite-population correction | Variance factor (N-n)/(N-1) separating Hypergeometric from Binomial | [04_02](html/04_02_limits_and_approximations.html) |
| Skewness | Third standardized moment; the main driver of the error of Normal approximations | [04_02](html/04_02_limits_and_approximations.html) |
| Sampling fraction | n / N, the share of the population in the sample; small values make Hypergeometric close to Binomial | [04_02](html/04_02_limits_and_approximations.html) |
| Inverse-CDF method | If U is uniform on (0,1) then F^-1(U) has CDF F; the basis of the transformation recipes | [04_01](html/04_01_relationship_map.html) |
