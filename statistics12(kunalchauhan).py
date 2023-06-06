# -*- coding: utf-8 -*-
"""Statistics12(KunalChauhan).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyuUZAu6RZ-FtTwMsuSCY_0FZI2JLMfg
"""

import scipy.stats as stats

mean_A = 2.5
mean_B = 2.2
s_A = 0.8
s_B = 0.6
n_A = n_B = 30

t_statistic, p_value = stats.ttest_ind_from_stats(mean_A, s_A, n_A, mean_B, s_B, n_B)
alpha = 0.05

if p_value < alpha:
    print("The null hypothesis should be rejected.")
    print("There is a significant difference in the mean improvement scores between Group A and Group B.")
else:
    print("The null hypothesis should not be rejected.")
    print("There is insufficient evidence to suggest a significant difference in the mean improvement scores between Group A and Group B.")