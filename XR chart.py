from matplotlib import pyplot as plt

# This code was typed by SRIVATHSAN.S
# This can be used to solve the engineering XR chart problems
from matplotlib.pyplot import subplot, plot, title, ylabel, xlabel, show
from numpy import linspace, sin
from scipy import rand

x = int(input("Enter num of sample: "))
sol = 0
sol1 = 0
sample = []
for z in range(0, x):
    sample.insert(z, z + 1)
print(sample)

c = []
print("Enter mean values: ")

# for z in range(0, x):
    #c.insert(z, int(input()))
c = [43, 49, 37, 44, 45, 37, 51, 46, 43, 47]

print(c)
mean = sum(c) / x
print("X' = ", mean)

cr = []
print("Enter range values: ")
# for zr in range(0, x):
#     cr.insert(zr, int(input()))
cr = [5, 6, 5, 7, 7, 4, 8, 6, 4, 6]

print(cr)
rangeR = sum(cr) / x

print("R' = ", rangeR)

smalln = int(input("Enter the Sample size: "))
if smalln == 2:
    a2 = 1.880
    d3 = 0
    d4 = 3.267
    d2 = 1.128
elif smalln == 3:
    a2 = 1.023
    d3 = 0
    d4 = 2.574
    d2 = 1.693
elif smalln == 4:
    a2 = 0.729
    d3 = 0
    d4 = 2.282
    d2 = 2.059
elif smalln == 5:
    a2 = 0.577
    d3 = 0
    d4 = 2.114
    d2 = 2.326
elif smalln == 6:
    a2 = 0.483
    d3 = 0
    d4 = 2.004
    d2 = 2.534
elif smalln == 7:
    a2 = 0.419
    d3 = 0.076
    d4 = 1.924
    d2 = 2.704
elif smalln == 8:
    a2 = 0.373
    d3 = 0.136
    d4 = 1.864
    d2 = 2.847
elif smalln == 9:
    a2 = 0.337
    d3 = 0.184
    d4 = 1.816
    d2 = 2.970
elif smalln == 10:
    a2 = 0.308
    d3 = 0.223
    d4 = 1.777
    d2 = 3.078
elif smalln == 11:
    a2 = 0.285
    d3 = 0.256
    d4 = 1.744
    d2 = 3.173
elif smalln == 12:
    a2 = 0.266
    d3 = 0.283
    d4 = 1.717
    d2 = 3.258
elif smalln == 13:
    a2 = 0.249
    d3 = 0.307
    d4 = 1.693
    d2 = 3.336
elif smalln == 14:
    a2 = 0.235
    d3 = 0.328
    d4 = 1.672
    d2 = 3.407
elif smalln == 15:
    a2 = 0.223
    d3 = 0.347
    d4 = 1.653
    d2 = 3.472
elif smalln == 16:
    a2 = 0.212
    d3 = 0.363
    d4 = 1.637
    d2 = 3.532
elif smalln == 17:
    a2 = 0.203
    d3 = 0.378
    d4 = 1.622
    d2 = 3.588
elif smalln == 18:
    a2 = 0.194
    d3 = 0.391
    d4 = 1.608
    d2 = 3.640
elif smalln == 19:
    a2 = 0.187
    d3 = 0.403
    d4 = 1.597
    d2 = 3.689
elif smalln == 20:
    a2 = 0.180
    d3 = 0.415
    d4 = 1.585
    d2 = 3.735
elif smalln == 21:
    a2 = 0.173
    d3 = 0.425
    d4 = 1.575
    d2 = 3.778
elif smalln == 22:
    a2 = 0.167
    d3 = 0.434
    d4 = 1.566
    d2 = 3.819
elif smalln == 23:
    a2 = 0.162
    d3 = 0.443
    d4 = 1.557
    d2 = 3.858
elif smalln == 24:
    a2 = 0.157
    d3 = 0.451
    d4 = 1.548
    d2 = 3.895
elif smalln == 25:
    a2 = 0.153
    d3 = 0.459
    d4 = 1.541
    d2 = 3.931
else:
    print("Out of limit")

print("A2 = ", a2, " D3 = ", d3, " D4 = ", d4)
print("X CHART")
CL = mean
ar = a2 * rangeR
LCL = mean - ar
UCL = mean + ar

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

outz = []
for i in range(0, x):
    if c[i] < LCL or c[i] > UCL:
        outz.insert(i, c[i])
if outz:
    print("Since ", outz, " lie out of the control limits, according to X' chart the process is out of control")
else:
    sol = 1
    print("Since all the point lie inside the control limits, according to X' chart the process is under control")

print("R CHART")
RCL = rangeR
RLCL = d3 * rangeR
RUCL = d4 * rangeR

print("CL = ", RCL, " UCL = ", RUCL, " LCL = ", RLCL)
RLCLg = []
for z in range(0, x):
    RLCLg.insert(z, RLCL)
RUCLg = []
for z in range(0, x):
    RUCLg.insert(z, RUCL)
RCLg = []
for z in range(0, x):
    RCLg.insert(z, RCL)
out = []
for i in range(0, x):
    if cr[i] < RLCL or cr[i] > RUCL:
        out.insert(i, cr[i])
if out:
    print("Since ", out, " lie out of the control limits, according to R chart the process is out of control")
else:
    sol1 = 1
    print("Since all the point lie inside the control limits, according to R chart the process is under control")

print("STATE OF CONTROL:")
if sol == 1 and sol1 == 1:
    print("Since the process is under control according to both the charts, the process is under control")
else:
    print("Since the process is out of control according to one of the charts, the process is out of control")

subplot(2, 1, 1)
plot(sample, c)
title('X Chart')
ylabel('mean')
xlabel('sample')
plot(sample, UCLg)
plot(sample, LCLg)
plot(sample, CLg)

subplot(2, 1, 2)
plot(sample, cr)
title('R Chart')
ylabel('range')
xlabel('sample')
plot(sample, RUCLg)
plot(sample, RLCLg)
plot(sample, RCLg)
show()


