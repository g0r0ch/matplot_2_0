import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()

# y = np.random.normal(0, 2, 500)
# ax.hist(y, 50)

# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(1, 5, len(x))
# ax.bar(x, y)

# y = np.random.normal(0, 2, 500)
# x = np.linspace(np.min(y), np.max(y), 10)
# bars = [len(y[np.bitwise_and(y >= x[i], y < x[i+1])]) for i in range(len(x)-1)]

# ax.bar(range(len(x)-1), bars)
# ax.barh(range(len(x)-1), bars)
#
# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(-20, 20, len(x))
#
# ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)

# x = np.arange(10)
# y1 = np.random.randint(3, 20, len(x))
# y2 = np.random.randint(3, 20, len(x))
# w = 0.3
# ax.bar(x - w/2, y1, width=w)
# ax.bar(x + w/2, y2, width=w)

##########################################pie

# vals = [10, 40, 23, 30, 7]
# labels = ['toy', 'hoi', 'moi', 'roi', 'oi']
# ax.pie(vals, labels=labels)

vals = [10, 40, 23, 30, 7]
labels = ['toy', 'hoi', 'moi', 'roi', 'oi']
exp = (0.1, 0.2, 0, 0, 0)
# ax.pie(vals, labels=labels, autopct='%.2f', explode=exp, shadow=True)
ax.pie(vals, labels=labels, autopct='%.2f', wedgeprops=dict(width=0.5), shadow=True)

ax.grid()

plt.show()