import numpy as np 
import matplotlib.pyplot as plt 

a = range(1,5)
b = range(5,9)
c = range(9,13)
arr = np.array([a,b,c])
print(arr[1]+arr[0]+arr[2])
plt.plot(arr[0],arr[1],arr[2])
plt.xlabel("waktu")
plt.ylabel("progres")
plt.savefig("gamm.png")
plt.grid(True)
plt.show()



print("arya ganteng!!!!!!!!")