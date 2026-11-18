# Module 05 data

Lessons use **simulated data** with fixed seeds (`np.random.default_rng(42)`), so the notebooks reproduce exactly. Any lesson that uses a real dataset will document its source, license and download date here.

| Lesson | What is simulated |
|---|---|
| 05_01 | coin, die, Exponential, Uniform, Lognormal, Cauchy and Pareto draws; roulette spins (18/38 on red); poll answers (Bernoulli 0.5); random points in the unit square for the Monte Carlo estimate of pi |

All scenarios are illustrative, not measured.
| 05_02 | draws from Uniform, Exponential, Bernoulli, Lognormal, a two-humped mixture and Pareto; daily sales totals (Lognormal orders, mean 85, SD 60); bottle fills (Uniform 495 to 505 ml); heavy-skew revenue per user (Lognormal s = 2) |
| 05_03 | a population of 20,000 delivery times (Gamma(4, scale 7.5), seed 2025); Normal samples (mean 50, SD 12); a defect sample (12 of 80); two checkout-time summaries |
