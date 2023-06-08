import matplotlib.pyplot as plt
import numpy as np
x=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
y1=[0,0,0,0,0.001,0,0,0.002,0.001,0.002,0.001,0.001,0.002,0.002,0.002,0.003,0.003,0.004,0.004,0.005,0.005]

plt.plot(x,y1,color='y', label='C++')

y2=[0.001,0.001,0.002,0.003,0.002,0.005,0.004,0.004,0.004,0.005,0.006,0.006,0.013,0.018,0.025,0.04,0.055,0.063,0.101,0.106,0.131]

plt.plot(x,y2,color='b', label='Python')

plt.xlabel('Número de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de CountingSort en C++ y Python')
plt.legend(loc='upper left')
#plt.yticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700])
plt.xticks(np.linspace(100, 100000, 21),x,rotation=45)

plt.show()