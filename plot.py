import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np

def plot(data, path):

	x = np.linspace(1, 240, 240)
	y = np.array(data[-240:])
	plt.plot(x, y, 'r') 
	plt.title("The last year SSE_Composite_Index")
	plt.xlabel("Time")
	plt.ylabel("Index")
	plt.savefig(path)