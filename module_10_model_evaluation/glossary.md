# Module 10 glossary

| Term | Definition | Lesson |
|---|---|---|
| Confusion matrix | The 2 x 2 table of true positives, false positives, true negatives and false negatives that results from applying a threshold to a classifier's scores. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Decision threshold | The score above which a case is predicted positive; moving it trades false alarms against misses. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Sensitivity (recall, true positive rate) | The share of actual positives that are flagged, TP / (TP + FN) = P(S > t \\| positive). | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Specificity | The share of actual negatives that are correctly passed, TN / (TN + FP) = 1 - false positive rate. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| False positive rate | The share of actual negatives that are flagged, FP / (FP + TN) = P(S > t \\| negative). | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Precision (positive predictive value) | The share of flagged cases that are truly positive, TP / (TP + FP); it depends on the prevalence. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Prevalence (base rate) | The share of positive cases in the population being scored; it changes precision and accuracy but not recall or the false positive rate. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Separability d-prime | The distance between the mean scores of positives and negatives in units of their standard deviation; larger values mean less overlap. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| Wilson interval | A confidence interval for a proportion that keeps good coverage near 0 and 1 and for small samples, preferred to the Wald interval. | [10_01](html/10_01_confusion_matrix_from_distributions.html) |
| F1 score | The harmonic mean of precision and recall, 2TP / (2TP + FP + FN); it ignores true negatives. | [10_02](html/10_02_classification_metrics.html) |
| F-beta score | A generalisation of F1 in which recall is weighted beta times as much as precision. | [10_02](html/10_02_classification_metrics.html) |
| Matthews correlation coefficient (MCC) | The correlation between predicted and true binary labels; it uses all four cells and is zero for any constant or random classifier. | [10_02](html/10_02_classification_metrics.html) |
| Cohen's kappa | Agreement between prediction and truth beyond what chance would give, (p_o - p_e) / (1 - p_e). | [10_02](html/10_02_classification_metrics.html) |
| Balanced accuracy | The average of recall and specificity; unaffected by the prevalence. | [10_02](html/10_02_classification_metrics.html) |
| Youden's J (informedness) | Recall plus specificity minus one, equal to TPR - FPR; zero for a random classifier. | [10_02](html/10_02_classification_metrics.html) |
| Markedness | Precision plus negative predictive value minus one; MCC is the geometric mean of markedness and Youden's J. | [10_02](html/10_02_classification_metrics.html) |
