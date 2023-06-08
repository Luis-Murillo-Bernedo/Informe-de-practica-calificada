import matplotlib.pyplot as plt
import numpy as np
x=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
y1=[0,0,0.015,0.015,0.031,0.062,0.109,0.156,0.219,0.312,0.39,0.484,2.156,4.89,8.876,14.187,20.64,28.111,37.462,46.368,58.171]

plt.plot(x,y1,color='y', label='C++')

y2=[0,0.04,0.125,0.792,1.302,2.36,3.435,6.362,7.226,11.485,12.367,14.939,62.82,171.786,300.907,466.248,679.935,834.182,1035.996,1376.412,1694.432]

plt.plot(x,y2,color='b', label='Python')

plt.xlabel('Número de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de BubbleSort en C++ y Python')
plt.legend(loc='upper left')
plt.yticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700])
plt.xticks(np.linspace(100, 100000, 21),x,rotation=45)

plt.show()