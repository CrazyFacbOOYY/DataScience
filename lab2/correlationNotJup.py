# ШАГ 1 (ячейка 1) - по счету 
import pandas as pd
brainFrame = pd.read_csv('brainsize.txt', delimiter='\t')

# ШАГ 2 (ячейка 2)
print(brainFrame.head())
# ШАГ 2 (ячейка 3)
print(brainFrame.head(10))
# ШАГ 2 (ячейка 4)
print(brainFrame.tail(8))

# Часть 2 
# ШАГ 1 (ячейка 5)
print(brainFrame.describe())

# ШАГ 2 (ячейка 6)
import numpy as np
import matplotlib.pyplot as plt

# ШАГ 2 (ячейка 7)
menDf = brainFrame[brainFrame['Gender'] == 'Male']
womenDf = brainFrame[brainFrame['Gender'] == 'Female']

# ШАГ 2 (ячейка 8)
menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)

plt.scatter(menMeanSmarts, menDf["MRI_Count"])

plt.xlabel('PIQ, FSIQ, VIQ')
plt.ylabel('MRI Count')
plt.title('Размер мозга от интеллекта у мужчин')

plt.show()

# ШАГ 2 (ячейка 9)
womenMeanSmarts = womenDf[['PIQ', 'FSIQ', 'VIQ']].mean(axis=1)

plt.scatter(womenMeanSmarts, womenDf['MRI_Count'])

plt.xlabel('PIQ, FSIQ, VIQ')
plt.ylabel('MRI Count')
plt.title('Pазмер мозга от интеллекта у женщин')

plt.show()