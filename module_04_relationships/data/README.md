# Module 04 data

This module uses **no external data**. Every number comes from simulation with a fixed seed (`np.random.default_rng(42)`), so the notebooks reproduce exactly.

| Lesson | What is simulated |
|---|---|
| 04_01 | draws from each family to verify the 18 continuous and 9 discrete relationships; a call-center timeline (12 calls per hour, 25 % spam); a quality lot (N = 2000, K = 40, n = 60); a statistics chain |
| 04_02 | website clicks (Binomial(2000, 0.003)), exam passes (Binomial(200, 0.6)), a 40-customer service total (Gamma), and small-sample t intervals |

All scenarios are illustrative, not measured.
