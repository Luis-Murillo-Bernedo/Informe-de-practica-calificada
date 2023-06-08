import matplotlib.pyplot as plt
import numpy as np
x=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
y1=[0,0,0,0,0.001,0,0.001,0.003,0.002,0.003,0.004,0.004,0.008,0.013,0.019,0.024,0.03,0.035,0.041,0.045,0.051]

plt.plot(x,y1,color='y', label='C++')

y2=[0,0.005,0.005,0.012,0.029,0.065,0.038,0.04,0.044,0.052,0.107,0.069,0.079,0.308,0.412,0.599,0.937,0.882,1.101,1.124,2.007]

plt.plot(x,y2,color='b', label='Python')

plt.xlabel('Número de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de HeapSort en C++ y Python')
plt.legend(loc='upper left')
#plt.yticks([200,400,600,800,1000])
plt.xticks(np.linspace(100, 100000, 21),x,rotation=45)

plt.show()