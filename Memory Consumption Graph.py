import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4


keylength_acafp = (12, 16, 20, 22)
keylength_rsa = (13, 16, 21 , 23)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, keylength_acafp, bar_width,
alpha=opacity,
color='r',
label='ACAFP (Proposed Algo)')

rects2 = plt.bar(index + bar_width, keylength_rsa, bar_width,
alpha=opacity,
color='b',
label='RSA')

plt.xlabel('Key length in bits')
plt.ylabel('Encrypted Data in bits')
plt.title('Memory Consumption')
plt.xticks(index + bar_width, ('13', '17', '22', '25'))
plt.legend()

plt.tight_layout()
plt.show()