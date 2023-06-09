# -*- coding: utf-8 -*-
"""Statistics9(KunalChauhan).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyuUZAu6RZ-FtTwMsuSCY_0FZI2JLMfg
"""

import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/Kuna1Chauhan/EDA/main/STUDENT%20SCORE%20-%20Sheet1.csv")
scores = data.iloc[:, 1:].values
from scipy.stats import f_oneway

# Perform one-way ANOVA
statistic, p_value = f_oneway(*scores)
significance_level = 0.05

if p_value < significance_level:
    print("The mean scores of the students are not the same.")
    # Find the student with the highest score
    highest_score_student = data.loc[data["Final Exam"].idxmax(), "Name"]
    print("The student with the highest score is:", highest_score_student)
else:
    print("The mean scores of the students are the same.")