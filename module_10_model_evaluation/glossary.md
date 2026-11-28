# Module 10 glossary

| Term | Definition | Lesson |
|---|---|---|
| Confusion matrix | The 2 x 2 table of true positives, false positives, true negatives and false negatives that results from applying a threshold to a classifier's scores. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Decision threshold | The score above which a case is predicted positive; moving it trades false alarms against misses. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Sensitivity (recall, true positive rate) | The share of actual positives that are flagged, TP / (TP + FN) = P(S > t \| positive). | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Specificity | The share of actual negatives that are correctly passed, TN / (TN + FP) = 1 - false positive rate. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| False positive rate | The share of actual negatives that are flagged, FP / (FP + TN) = P(S > t \| negative). | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Precision (positive predictive value) | The share of flagged cases that are truly positive, TP / (TP + FP); it depends on the prevalence. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Prevalence (base rate) | The share of positive cases in the population being scored; it changes precision and accuracy but not recall or the false positive rate. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Separability d-prime | The distance between the mean scores of positives and negatives in units of their standard deviation; larger values mean less overlap. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Wilson interval | A confidence interval for a proportion that keeps good coverage near 0 and 1 and for small samples, preferred to the Wald interval. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
