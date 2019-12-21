
import numpy as np
import scipy as sc

import matplotlib.pyplot as plt

func = lambda th : np.sin (1/2 * th[0] **2 - 1/4* th[1]**2 +3)* np.cos(2*th[0] +1 - np.e**th[1])

res=100
_x= np.linspace(-2,2,res)
_y= np.linspace(-2,2,res)

_z= np.zeros((res,res))

for ix, x in enumerate(_x):
	for iy, y in enumerate(_x):
		_z[iy,ix] = func([x,y])


plt.contourf(_x,_y,_z,100)
plt.colorbar()


theta = np.random.rand(2) *4 -2

_T= np.copy(theta)

h=0.001
lr= 0.001

plt.plot(theta[0], theta[1],"o",c = "white")

grad = np.zeros(2)

for _ in range (10000):

	for it, th in enumerate(theta):

		_T = np.copy(theta)
		_T[it] = _T[it] + h

		deriv = (func(_T) -func(theta)) / h

		grad [it] = deriv

	theta = theta - lr *grad

	func(theta)

	

	if (_ %10 ==0):

		plt.plot(theta[0], theta[1], ".", c= "red")




plt.plot(theta[0], theta[1],"o",c = "green")


plt.show()





