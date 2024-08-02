import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

def update_cos(frame, line, x):
    line.set_ydata(np.cos(x+frame))
    return [line]





# plt.ion()
fig, ax = plt.subplots()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)

line, = ax.plot(x, y)

#
# for delay in np.arange(0, np.pi, 0.1):
#     y = np.cos(x+delay)
#     # plt.clf()
#     # plt.plot(x, y)
#     line.set_ydata(y)
#
#     plt.draw()
#     plt.gcf().canvas.flush_events()
#
#     time.sleep(0.02)

phasa = np.arange(0, 4*np.pi, 0.1)

animation = FuncAnimation(
    fig,
    func=update_cos,
    frames=phasa,
    fargs=(line, x),
    interval=30,
    blit=True,
    repeat=False)


# plt.ioff()
plt.show()