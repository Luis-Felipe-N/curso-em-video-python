import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3000, 1, 100)
y = numpy.random.normal(15000, 40, 100) / x

plt.scatter(x, y)
plt.show()
