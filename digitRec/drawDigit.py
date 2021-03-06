import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on points')
X = np.random.rand(8)
line, = ax.plot(X, 'o', picker=5)  # 5 points tolerance

def onpick(event):
	thisline = event.artist
	xdata = thisline.get_xdata()
	ydata = thisline.get_ydata()
	ind = event.ind
	points = tuple(zip(xdata[ind], ydata[ind]))
	X = np.random.rand(8)
	line, = ax.plot(X, 'o', picker=5)
	plt.draw()

fig.canvas.mpl_connect('pick_event', onpick)

plt.show()