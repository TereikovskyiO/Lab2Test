'''2 variant'''
import tkinter as tk
import math
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer

x = []
y = []
A = 0          # random
fi = 0         # random
w = 900
N = 256
n = 10
# step = w/n
t = 0
tau = 0

######### variant when fi and A are always random
# x
for t in range(N):
    sum = 0
    for i in range(n):
        fi = random.randint(1, 5)                                       # for random float use random.uniform( , )
        A  = random.randint(1, 5)
        sum = sum + A*(math.sin(w*t+fi))
    x.append(sum)
# y
for t in range(N):
    sum = 0
    for i in range(n):
        fi = random.randint(1, 5)  # for random float use random.uniform( , )
        A = random.randint(1, 5)
        sum = sum + A * (math.sin(w * t + fi))
    y.append(sum)

print("Number of x elements: ", len(x))
print("Number of y elements: ", len(y))

''''# print graph of x
tgr = []
for i in range(N):
    tgr.append(i)
plt.plot(tgr, x)
plt.show()'''
#######   Mx, Dx, Rxx and Rxy   ########





Mx = 0
Dx = 0
Mxy = 0
Dxy = 0
Rxx = 0
Rxy = 0
#start = timer()
#     Mxx
for t in range(N):
    Mx = Mx + x[t]
Mx = Mx/N
#print(Mx)

#      Dxx
for t in range(N):
    Dx = Dx + (x[t]-Mx)
Dx = Dx/(N-1)


#     Mxy
for t in range(N):
    Mx = Mx + y[t]
Mx = Mx/N
#print(Mx)

#      Dxy
for t in range(N):
    Dx = Dx + (y[t]-Mx)
Dx = Dx/(N-1)

#end =  timer()
#time = end - start                # time in seconds
'''
root = tk.Tk()
w1 = tk.Label(root, text="Mx: \t\t\t\t\t" + str(Mx))
w1.pack()
w2 = tk.Label(root, text = "Dx: \t\t\t\t\t" + str(Dx))
w2.pack()
w3 = tk.Label(root, text = "Time: \t\t\t\t\t" + str(time))
w3.pack()
root.mainloop()'''

#    Rxx                                         what to do with tau ??????
Rxx = []
Rxy = []
for tau in range(N//2):
    sum = 0
    for t in range(N//2):
        sum = sum + (x[t]-Mx)*(x[t+tau]-Mx)
    Rxx.append(sum/(N-1))

#     Rxy
#tau1 = N//2
for i in range(N):
    y.append(0)

for tau in range(N):
    sum = 0
    for t in range(N-tau):
        sum = sum + (x[t]-Mx)*(y[t+tau]-Mxy)
    Rxy.append(sum/(N-1))
print(len(Rxx))
print(len(Rxy))
print(Rxx[0])
print(Rxy[0])
sum = 0
RxxNum = 0
RxyNum = 0
for i in range(len(Rxx)):
    sum = sum + Rxx[i]
RxxNum = sum/n
print(RxxNum)
for i in range(len(Rxy)):
    sum = sum + Rxy[i]
RxyNum = sum/n
print(RxyNum)


tgr = []
for i in range(N):
    tgr.append(i)
plt.plot(tgr, Rxy)
plt.show()