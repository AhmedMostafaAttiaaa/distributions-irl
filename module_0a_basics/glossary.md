# Module 0A glossary

| Term | Definition | Lesson |
|---|---|---|
| Sample space | The set S of all possible outcomes of an experiment. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Outcome | One possible result of an experiment, such as rolling a 4. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Event | A set of outcomes (a subset of the sample space), such as 'the die is even'. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Union | A or B: the outcomes that are in A, in B, or in both. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Intersection | A and B: the outcomes that are in both A and B. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Complement | Not A: the outcomes of the sample space that are not in A; P(not A) = 1 - P(A). | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Mutually exclusive events | Events that cannot both happen (empty intersection), so P(A or B) = P(A) + P(B). | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Axioms of probability | P(A) >= 0, P(S) = 1, and P of a union of mutually exclusive events equals the sum of their probabilities. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Equally likely outcomes | Outcomes with the same probability, so P(A) = number of outcomes in A divided by the total number. | [0a_01](html/0a_01_sets_events_sample_space.html) |
| De Morgan's laws | not (A or B) = (not A) and (not B); not (A and B) = (not A) or (not B). | [0a_01](html/0a_01_sets_events_sample_space.html) |
| Multiplication rule | If a task has steps with m1, m2, ..., mk choices, it can be done in m1 x m2 x ... x mk ways. | [0a_02](html/0a_02_counting_basics.html) |
| Factorial | n! = n (n - 1) ... 2 1, the number of ways to arrange n distinct items; 0! = 1. | [0a_02](html/0a_02_counting_basics.html) |
| Permutation | An ordered selection of k items from n without repetition; there are n! / (n - k)! of them. | [0a_02](html/0a_02_counting_basics.html) |
| Combination | An unordered selection of k items from n; there are n! / (k! (n - k)!) of them. | [0a_02](html/0a_02_counting_basics.html) |
| Binomial coefficient | The number C(n, k) of ways to choose k items from n, read 'n choose k'; the entries of Pascal's triangle. | [0a_02](html/0a_02_counting_basics.html) |
| Pascal's triangle | Triangle of binomial coefficients in which each entry is the sum of the two entries above it. | [0a_02](html/0a_02_counting_basics.html) |
| Birthday problem | Probability that at least two of n people share a birthday: 1 - product of (365 - j) / 365; above 50 % for 23 people. | [0a_02](html/0a_02_counting_basics.html) |
| Addition rule | P(A or B) = P(A) + P(B) - P(A and B); the overlap is subtracted once because it was counted twice. | [0a_03](html/0a_03_probability_rules.html) |
| Inclusion-exclusion | For several events, add the singles, subtract the pairs, add the triples, and so on, to get P of the union. | [0a_03](html/0a_03_probability_rules.html) |
| Independent events | Events A and B with P(A and B) = P(A) P(B); knowing one happened does not change the chance of the other. | [0a_03](html/0a_03_probability_rules.html) |
| Multiplication rule for probabilities | For independent events P(A and B) = P(A) P(B); in general P(A and B) = P(A) P(B given A). | [0a_03](html/0a_03_probability_rules.html) |
| At least one | P(at least one of independent events) = 1 - product of (1 - p_i), the complement of 'none happens'. | [0a_03](html/0a_03_probability_rules.html) |
| Series system | A system that works only if all its components work; reliability is the product of the component reliabilities. | [0a_03](html/0a_03_probability_rules.html) |
| Parallel system | A system that works if at least one component works; reliability is 1 minus the product of the failure probabilities. | [0a_03](html/0a_03_probability_rules.html) |
| Union bound | P(A1 or ... or An) is at most the sum of the P(Ai), whatever the overlaps. | [0a_03](html/0a_03_probability_rules.html) |
| Conditional probability | P(A given B) = P(A and B) / P(B): the probability of A in the smaller world where B is known to have happened. | [0a_04](html/0a_04_conditional_independence.html) |
| General multiplication rule | P(A and B) = P(B) P(A given B) = P(A) P(B given A); extends to chains of events. | [0a_04](html/0a_04_conditional_independence.html) |
| Independence (conditional form) | A and B are independent when P(A given B) = P(A): learning B does not change the chance of A. | [0a_04](html/0a_04_conditional_independence.html) |
| Sampling without replacement | Drawing items that are not returned, so each draw changes the probabilities of the next. | [0a_04](html/0a_04_conditional_independence.html) |
| Contingency table | A table of counts of units classified by two categories at once; rows and columns give conditional probabilities. | [0a_04](html/0a_04_conditional_independence.html) |
| Chi-square test of independence | Test that compares observed counts in a contingency table with the counts expected under independence. | [0a_04](html/0a_04_conditional_independence.html) |
| Monty Hall problem | Three doors, one car: switching after the host reveals a goat wins with probability 2/3, staying wins 1/3. | [0a_04](html/0a_04_conditional_independence.html) |
| Prosecutor's fallacy | Confusing P(A given B) with P(B given A). | [0a_04](html/0a_04_conditional_independence.html) |
