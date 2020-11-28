import math
from matplotlib import pyplot as plt

# This code was typed by SRIVATHSAN.S
# This can be used to solve the engineering XR chart problems
x = int(input("Enter num of sample: "))
sol = 0
sol1 = 0
sample = []
for z in range(0, x):
    sample.insert(z, z + 1)
print(sample)

smalln = int(input("Enter the Sample size: "))

c = []
# for z in range(0, x):
#     print("Enter value: ")
#     c.insert(z, int(input()))
print(c)
c = [2, 1, 1, 2, 3, 5, 5, 1, 2, 3]
np = sum(c) / x
print("np' = ", np)
p = np / smalln
print("p' = ", p)
pp = []
for z in range(0, x):
    pp.insert(z, c[z] / smalln)
print("np CHART")
CL = np
LCL = np - (3 * (math.sqrt(np * (1 - p))))
UCL = np + (3 * (math.sqrt(np * (1 - p))))
if LCL <= 0:
    print("Since LCL is less than 0 (", LCL, ") LCL is taken as 0")
    LCL = 0
print("CL = ", CL, " UCL = ", UCL, " LCL = ", LCL)
LCLg = []
for z in range(0, x):
    LCLg.insert(z, LCL)
UCLg = []
for z in range(0, x):
    UCLg.insert(z, UCL)
CLg = []
for z in range(0, x):
    CLg.insert(z, CL)
plt.plot(sample, c)
plt.title('np Chart')
plt.ylabel('np')
plt.xlabel('sample')
plt.plot(sample, UCLg)
plt.plot(sample, LCLg)
plt.plot(sample, CLg)
plt.show()
outz = []
for i in range(0, x):
    if c[i] < LCL or c[i] > UCL:
        outz.insert(i, c[i])
if outz:
    print("Since ", outz, " lie out of the control limits, the statistical process is out of control")
else:
    sol = 1
    print("Since all the point lie inside the control limits, the statistical process is under control")

print("p CHART")
pCL = p
pLCL = p - 3 * (math.sqrt((p * (1 - p)) / smalln))
pUCL = p + 3 * (math.sqrt((p * (1 - p)) / smalln))
if pLCL <= 0:
    print("Since LCL is less than 0 (", pLCL, ") LCL is taken as 0")
    pLCL = 0
print("CL = ", pCL, " UCL = ", pUCL, " LCL = ", pLCL)
RLCLg = []
for z in range(0, x):
    RLCLg.insert(z, pLCL)
RUCLg = []
for z in range(0, x):
    RUCLg.insert(z, pUCL)
RCLg = []
for z in range(0, x):
    RCLg.insert(z, pCL)
plt.plot(sample, pp)
plt.title('p Chart')
plt.ylabel('p')
plt.xlabel('sample')
plt.plot(sample, RUCLg)
plt.plot(sample, RLCLg)
plt.plot(sample, RCLg)
plt.show()
out = []
for i in range(0, x):
    if pp[i] < pLCL or pp[i] > pUCL:
        out.insert(i, pp[i])
if out:
    print("Since ", out, " lie out of the control limits, the statistical process is out of control")
else:
    sol1 = 1
    print("Since all the point lie inside the control limits, the statistical process is under control")
print("STATE OF CONTROL:")
if sol == 1 and sol1 == 1:
    print("Since the process is under control according to both the charts, the process is under control")
else:
    print("Since the process is out of control according to one of the charts, the process is out of control")
