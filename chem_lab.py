# importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# X axis: water activities
water_activity = np.array([0.996, 0.974, 0.985, 0.951, 0.964, 0.926, 0.989, 0.99, 0.973, 0.934, 0.973, 0.977,
                           0.971, 0.972])

# Y axis: T1 as first freezing temperature
#         T2 as second freezing temperature
T1 = np.array([235.68, 234.11, 233.05, 225.27, 230.6, 222.55, 232.95, 225.17, 229.17, 220.88, 228.96, 228.24,
               225.22, 224.79])
deltachempot1 = ([-711.1917932, -725.1227138, -738.810355, -839.578627, -778.41529, -752.2548698, -839.578627,
                  -791.131662, -894.7268809, -791.131662, -803.6058431, -839.578627, -839.578627])
actwat1 = np.exp(deltachempot1/(8.31*T1))

T2 = np.array([235.68, 237.45, 233.05, 225.27, 235.15, 228.63, 232.96, 225.17, 234.69, 236.17, 228.96, 228.24,
               231.1, 231.15])
#deltachempot2 = -711.1917932,

# find line of best fit
a, b = np.polyfit(water_activity, T1, 1)
c, d = np.polyfit(water_activity, T2, 1)
cluster = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

fig, ax = plt.subplots()

ax.scatter(water_activity[cluster == 1], T1[cluster == 1], marker='$H_2O$', color='r')
ax.scatter(water_activity[cluster == 2], T1[cluster == 2], marker='$OA$', color='c')
ax.scatter(water_activity[cluster == 3], T1[cluster == 3], marker='o', color='c')
ax.scatter(water_activity[cluster == 4], T1[cluster == 4], marker='s', color='c')
ax.scatter(water_activity[cluster == 5], T1[cluster == 5], marker='P', color='c')
ax.scatter(water_activity[cluster == 6], T1[cluster == 6], marker='*', color='c')
ax.scatter(water_activity[cluster == 7], T1[cluster == 7], marker='X', color='c')
ax.scatter(water_activity[cluster == 8], T1[cluster == 8], marker='D', color='c')
ax.scatter(water_activity[cluster == 9], T1[cluster == 9], marker='p', color='c')
ax.scatter(water_activity[cluster == 10], T1[cluster == 10], marker=2, color='c')
ax.scatter(water_activity[cluster == 11], T1[cluster == 11], marker='d', color='c')
ax.scatter(water_activity[cluster == 12], T1[cluster == 12], marker=5, color='c')
ax.scatter(water_activity[cluster == 13], T1[cluster == 13], marker='.', color='c')
ax.scatter(water_activity[cluster == 14], T1[cluster == 14], marker='^', color='c')
ax.scatter(water_activity[cluster == 1], T1[cluster == 1], marker='o', color='c')

ax.scatter(water_activity[cluster == 1], T2[cluster == 1], marker='$H_2O$', color='r')
ax.scatter(water_activity[cluster == 2], T2[cluster == 2], marker='$OA$', color='m')
ax.scatter(water_activity[cluster == 3], T2[cluster == 3], marker='o', color='m')
ax.scatter(water_activity[cluster == 4], T2[cluster == 4], marker='s', color='m')
ax.scatter(water_activity[cluster == 5], T2[cluster == 5], marker='P', color='m')
ax.scatter(water_activity[cluster == 6], T2[cluster == 6], marker='*', color='m')
ax.scatter(water_activity[cluster == 7], T2[cluster == 7], marker='X', color='m')
ax.scatter(water_activity[cluster == 8], T2[cluster == 8], marker='D', color='m')
ax.scatter(water_activity[cluster == 9], T2[cluster == 9], marker='p', color='m')
ax.scatter(water_activity[cluster == 10], T2[cluster == 10], marker=2, color='m')
ax.scatter(water_activity[cluster == 11], T2[cluster == 11], marker='d', color='m')
ax.scatter(water_activity[cluster == 12], T2[cluster == 12], marker=5, color='m')
ax.scatter(water_activity[cluster == 13], T2[cluster == 13], marker='.', color='m')
ax.scatter(water_activity[cluster == 14], T2[cluster == 14], marker='^', color='m')

# add points to plot
# plt.scatter(water_activity, T1)
# add line of best fit to plot
plt.plot(water_activity, a * water_activity + b, color='c')
plt.plot(water_activity, c * water_activity + d, color='m')
# plt.plot(water_activity, T1, 'ro')


plt.show()
