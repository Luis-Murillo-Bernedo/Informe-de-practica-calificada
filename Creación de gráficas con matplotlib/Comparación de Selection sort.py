import matplotlib.pyplot as plt
import numpy as np
x=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
y1=[0,0.001,0.001,0.011,0.022,0.039,0.063,0.09,0.129,0.16,0.205,0.25,0.989,2.249,4.002,6.81,9.089,12.529,16.083,20.155,24.825]

plt.plot(x,y1,color='y', label='C++')

y2=[0,0.001,0.055,0.36,0.56,1.06,1.604,2.47,3.561,4.66,6.758,6.7,30.98,69.642,105.565,191.872,261.902,379.749,503.605,774.976,939.179]

plt.plot(x,y2,color='b', label='Python')

plt.xlabel('Número de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de SelectionSort en C++ y Python')
plt.legend(loc='upper left')
plt.yticks([200,400,600,800,1000])
plt.xticks(np.linspace(100, 100000, 21),x,rotation=45)

plt.show()