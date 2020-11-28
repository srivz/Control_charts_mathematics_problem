from matplotlib import pyplot as plt

# This code was typed by SRIVATHSAN. S
# This can be used to solve the engineering XR chart problems
from matplotlib.pyplot import subplot, plot, title, ylabel, xlabel, show

x = int(input("Enter num of sample: "))
d2 = 0
a2 = 0
position = []
d3 = 0
d4 = 0
sol = 0
sol1 = 0
sample = []
smalln = int(input("Enter the Sample size: "))
print("Enter the specification limit: (num1)+-(num2)")
qsl1 = float(input("num1 = "))
qsl2 = float(input("num2 = "))
qtl1 = qsl1 + qsl2
qtl2 = qsl1 - qsl2
print("(", qsl1, "+-", qsl2, ")")
for z in range(0, x):
    sample.insert(z, z + 1)
print(sample)

c = []

for z in range(0, x):
    print("Enter value: ")
    c.insert(z, int(input()))

# c = [16.1, 15.2, 14.2, 13.9, 15.4, 15.7, 15.2, 15.0, 16.5, 14.9, 15.3, 17.8, 15.9, 14.6, 15.2]
print(c)
mean = sum(c) / x
print("X' = ", mean)

cr = []
for zr in range(0, x):
    print("Enter value: ")
    cr.insert(zr, int(input()))

# cr = [3.0, 2.1, 5.6, 2.4, 4.1, 2.7, 2.3, 3.8, 5.0, 2.9, 13.8, 14.2, 4.8, 5.0, 2.2]
print(cr)
rangeR = sum(cr) / x
print("R' = ", rangeR)

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
LCLg = []
for z in range(0, x):
    LCLg.insert(z, LCL)
UCLg = []
for z in range(0, x):
    UCLg.insert(z, UCL)
CLg = []
for z in range(0, x):
    CLg.insert(z, CL)


print("CL = ", CL, " UCL = ", UCL, " LCL = ", LCL)
position1 = []
outz = []

for i in range(0, x):
    if c[i] < LCL or c[i] > UCL:
        outz.insert(i, c[i])
for cv in range(0, x):
    if c[cv] in outz:
        position1.insert(cv, c.index(c[cv], cv, x) + 1)
if outz:
    print("Looking at all the mean values , the mean values of samples ", position1, " don’t lie between the UCL = ",
          UCL, " and LCL = ", LCL, ".Therefore the process is NOT under control with respect to Mean chart.")
else:
    sol = 1
    print(" Looking at all the mean values they lie between the UCL=", UCL, "and LCL =", LCL,
          ".Therefore the process is under control with respect to Mean chart.")
print(" ")
print(" ")
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


position2 = []
out = []
for i in range(0, x):
    if cr[i] < RLCL or cr[i] > RUCL:
        out.insert(i, cr[i])

if out:
    for cv in range(0, x):
        if cr[cv] in out:
            position2.insert(cv, cr.index(cr[cv], cv, x) + 1)
    print("Looking at all the range values , the range values of samples ", position2, " don’t lie between the UCL = ",
          RUCL, " and LCL = ", RLCL, ".Therefore the process is NOT under control with respect to Range chart.")
else:
    sol1 = 1
    print(" Looking at all the range values they lie between the UCL = ", RUCL, "and LCL = ", RLCL,
          ". Therefore the process is under control with respect to Range chart.")
print(" ")
print(" ")
print("STATE OF CONTROL:")
if sol == 1 and sol1 == 1:
    print("Since the process is under control according to both the charts, the process is under control\n\n")
else:
    print("Since the process is out of control according to one of the charts, the process is out of control\n\n")




sol1 = 0
sol = 0
print("Now we remove those samples whose values were outside UCL and LCL and form a new table without those samples.")

position.extend(position1)
position.extend(position2)
pos = list(dict.fromkeys(position))
newx = x - len(pos)
newc = []
newcr = []
newsample = []
newc.extend(c)
newcr.extend(cr)
newsample.extend(sample)
for f in range(1, len(pos) + 1):
    newc.pop(pos[f - 1] - f)
    newcr.pop(pos[f - 1] - f)
    newsample.pop()

print("\n\nSample   ", newsample)
print("mean     ", newc)
print("range    ", newcr)
newmean = sum(newc) / newx
print("X' = ", newmean)
newrange = sum(newcr) / newx
print("R' = ", newrange)

print("A2 = ", a2, " D3 = ", d3, " D4 = ", d4)
print("\n\nX CHART")
newCL = newmean
newar = a2 * newrange
newLCL = newmean - newar
newUCL = newmean + newar

print("CL = ", newCL, " UCL = ", newUCL, " LCL = ", newLCL)
newLCLg = []
for z in range(0, newx):
    newLCLg.insert(z, newLCL)
newUCLg = []
for z in range(0, newx):
    newUCLg.insert(z, newUCL)
newCLg = []
for z in range(0, newx):
    newCLg.insert(z, newCL)

noutz = []

for i in range(0, newx):
    if newc[i] < newLCL or newc[i] > newUCL:
        noutz.insert(i, newc[i])
if noutz:
    print("Looking at all the mean values , the mean values ", noutz, " don’t lie between the UCL = ", newUCL,
          " and LCL = ", newLCL, ".Therefore the process is NOT under control with respect to Mean chart.")
else:
    sol = 1
    print(" Looking at all the mean values they lie between the UCL = ", newUCL, " and LCL = ", newLCL,
          ".Therefore the process is under control with respect to Mean chart.")
print("\n\nR CHART")
newRCL = newrange
newRLCL = d3 * newrange
newRUCL = d4 * newrange

print("CL = ", newRCL, " UCL = ", newRUCL, " LCL = ", newRLCL)
newRLCLg = []
for z in range(0, newx):
    newRLCLg.insert(z, newRLCL)
newRUCLg = []
for z in range(0, newx):
    newRUCLg.insert(z, newRUCL)
newRCLg = []
for z in range(0, newx):
    newRCLg.insert(z, newRCL)

nout = []
for i in range(0, newx):
    if newcr[i] < newRLCL or newcr[i] > newRUCL:
        nout.insert(i, newcr[i])

if nout:
    print("Looking at all the range values , the range values of samples ", nout, " don’t lie between the UCL = ",
          newRUCL, "and LCL = ", newRLCL, ".Therefore the process is NOT under control with respect to Range chart.")
else:
    sol1 = 1
    print(" Looking at all the range values they lie between the UCL = ", newRUCL, " and LCL = ", newRLCL,
          ". Therefore the process is under control with respect to Range chart.")
print(" ")
print("STATE OF CONTROL:")
if sol == 1 and sol1 == 1:
    print("Since the process is under control according to both the charts, the process is under control")
else:
    print("Since the process is out of control according to one of the charts, the process is out of control")
print("Now the process is under control with respect to the ", newx,
      " samples considered since it is under control with respect to both MEAN and RANGE")
print(" ")
tl1 = newmean + ((3 * newrange) / d2)
tl2 = newmean - ((3 * newrange) / d2)
print("Tolerance limit= (", tl1, ",", tl2, ")")
print(" ")
print("RESULT")
if qtl1 > tl1 and qtl2 < tl2:
    print("Since the tolerance limits lie within the specification limits , the process meets the required "
          "specifications.")


subplot(2, 2, 1)
plot(sample, c)
title('X Chart')
ylabel('mean')
xlabel('sample')
plot(sample, UCLg)
plot(sample, LCLg)
plot(sample, CLg)

subplot(2, 2, 2)
plot(sample, cr)
title('R Chart')
ylabel('range')
xlabel('sample')
plot(sample, RUCLg)
plot(sample, RLCLg)
plot(sample, RCLg)

subplot(2, 2, 3)
plot(newsample, newc)
title('X Chart')
ylabel('mean')
xlabel('sample')
plot(newsample, newUCLg)
plot(newsample, newLCLg)
plot(newsample, newCLg)

subplot(2, 2, 4)
plot(newsample, newcr)
title('R Chart')
ylabel('range')
xlabel('sample')
plot(newsample, newRUCLg)
plot(newsample, newRLCLg)
plot(newsample, newRCLg)
show()
