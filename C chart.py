import math
from matplotlib import pyplot as plt

# This code was typed by SRIVATHSAN.S
# This can be used to solve the engineering XR chart problems
x = int(input("Enter num of sample: "))

sample = []
for z in range(0, x):
    sample.insert(z, z + 1)
print(sample)

c = []
# for z in range(0, x):
#     print("Enter value: ")
#     c.insert(z, int(input()))
c = [19, 10, 8, 12, 15, 22, 7, 13, 18, 13, 16, 14, 8, 7, 6, 4, 5, 6, 8, 9]
print(c)
cbar = sum(c) / x
print("c' = ", cbar)

print("c CHART")
CL = cbar
LCL = cbar - (3 * (math.sqrt(cbar)))
UCL = cbar + (3 * (math.sqrt(cbar)))
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
out = []
for i in range(0, x):
    if c[i] < LCL or c[i] > UCL:
        out.insert(i, c[i])
print("STATE OF CONTROL:")
if out:
    print("Since ", out, " lie out of the control limits, the statistical process is out of control")
else:
    print("Since all the point lie inside the control limits, the statistical process is under control")
plt.plot(sample, c)
plt.title('c Chart')
plt.ylabel('c')
plt.xlabel('sample')
plt.plot(sample, UCLg)
plt.plot(sample, LCLg)
plt.plot(sample, CLg)
plt.show()
