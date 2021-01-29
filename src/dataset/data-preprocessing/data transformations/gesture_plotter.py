import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

# Simple program to plot the gesture co-ordinates for visual inspection

def plot(gesture):
	x = gesture[1::2] 
	y = gesture[2::2]
	plt.scatter(x, y)
	plt.show()


if __name__ == "__main__":	
	#sample csv line 
	gesture = ['palm_108_keypoints', 550.552, 2280.4, 621.377, 2209.57, 678.713, 2125.25, 722.557, 2013.96, 800.128, 1943.13, 638.241, 1990.35, 634.868, 1852.07, 614.632, 1761.01, 587.651, 1673.32, 564.042, 1986.98, 550.552, 1828.46, 543.806, 1720.54, 523.57, 1632.85, 499.962, 1986.98, 496.589, 1835.21, 489.844, 1747.52, 476.353, 1666.57, 439.254, 2003.84, 419.018, 1889.17, 419.018, 1828.46, 419.018, 1757.63]
	plot(gesture)