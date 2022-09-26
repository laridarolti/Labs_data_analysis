# importing numpy, matplotlib, pandas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors as mcolors

df1 = pd.read_excel(r'C:\Users\larid\Documents\MASTER\SEM2\LABS\Chem Lab\atmostrajectory.xls')
print(df1)

df2 = pd.read_excel(r'C:\Users\larid\Documents\MASTER\SEM2\LABS\Chem Lab\calculated_values.xlsx')
print(df2)

graph, (plot1) = plt.subplots(1)

# PLOT OF ATMOSPHERIC TRAJECTORY
plot1.plot(df1.RH_new/100, df1.T_new, color='burlywood')

#plot1.plot(df1.aiw, df1.Temp, color='c')
#plot1.plot(df1.aw_nuc, df1.Temp, color='m')
plot1.plot(df1.aiw_corrected, df1.Temp, color='pink')
plot1.plot(df1.aw_nuc_corrected, df1.Temp, color='orange')

cluster = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

#g, ax = plt.subplots()

#plot1.scatter(df2.calculated_aw[cluster == 1], df2.Tf1[cluster == 1], marker='$H_2O$', color='r', label='Pure water')
#plot1.scatter(df2.calculated_aw[cluster == 2], df2.Tf1[cluster == 2], marker='$OA$', color='r',
              #label='5%wt oxalic acid')
#plot1.scatter(df2.calculated_aw[cluster == 3], df2.Tf1[cluster == 3], marker='o', color='r',
              #label='10%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 4], df2.Tf1[cluster == 4], marker='s', color='r',
              #label='30%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 5], df2.Tf1[cluster == 5], marker='P', color='r',
              #label='5%wt oxalic acid + 10%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 6], df2.Tf1[cluster == 6], marker='*', color='r',
              #label='5%wt oxalic acid + 30%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 7], df2.Tf1[cluster == 7], marker='X', color='r',
              #label='10%wt glutaric acid')
#plot1.scatter(df2.calculated_aw[cluster == 8], df2.Tf1[cluster == 8], marker='D', color='r',
              #label='30%wt glutaric acid')
#plot1.scatter(df2.calculated_aw[cluster == 9], df2.Tf1[cluster == 9], marker='p', color='r',
              #label='5%wt oxalic acid + 10%wt glutaric acid')
#plot1.scatter(df2.calculated_aw[cluster == 10], df2.Tf1[cluster == 10], marker=2, color='r',
              #label='5%wt oxalic acid + 30%wt glutaric acid')
#plot1.scatter(df2.calculated_aw[cluster == 11], df2.Tf1[cluster == 11], marker='d', color='r',
              #label='20%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 12], df2.Tf1[cluster == 12], marker=5, color='r',
              #label='20%wt glutaric acid')
#plot1.scatter(df2.calculated_aw[cluster == 13], df2.Tf1[cluster == 13], marker='.', color='r',
              #label='5%wt oxalic acid + 20%wt citric acid')
#plot1.scatter(df2.calculated_aw[cluster == 14], df2.Tf1[cluster == 14], marker='^', color='r',
              #label='5%wt oxalic acid + 20%wt glutaric acid')


#plot1.scatter(df2.calculated_aw[cluster == 1], df2.Tfk[cluster == 1], marker='$H_2O$', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 2], df2.Tfk[cluster == 2], marker='$OA$', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 3], df2.Tfk[cluster == 3], marker='o', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 4], df2.Tfk[cluster == 4], marker='s', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 5], df2.Tfk[cluster == 5], marker='P', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 6], df2.Tfk[cluster == 6], marker='*', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 7], df2.Tfk[cluster == 7], marker='X', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 8], df2.Tfk[cluster == 8], marker='D', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 9], df2.Tfk[cluster == 9], marker='p', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 10], df2.Tfk[cluster == 10], marker=2, color='g')
#plot1.scatter(df2.calculated_aw[cluster == 11], df2.Tfk[cluster == 11], marker='d', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 12], df2.Tfk[cluster == 12], marker=5, color='g')
#plot1.scatter(df2.calculated_aw[cluster == 13], df2.Tfk[cluster == 13], marker='.', color='g')
#plot1.scatter(df2.calculated_aw[cluster == 14], df2.Tfk[cluster == 14], marker='^', color='g')


#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 1], df2.Tf1[cluster == 1], marker='$H_2O$', color='r', label='Pure water')
plot1.scatter(df2.aw_corrected[cluster == 2], df2.Tf1[cluster == 2], marker='$OA$', color='r',
              label='5%wt oxalic acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 3], df2.Tf1[cluster == 3], marker='o', color='r',
              #label='10%wt citric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 4], df2.Tf1[cluster == 4], marker='s', color='r',
              #label='30%wt citric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 5], df2.Tf1[cluster == 5], marker='P', color='r',
              #label='5%wt oxalic acid + 10%wt citric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 6], df2.Tf1[cluster == 6], marker='*', color='r',
              #label='5%wt oxalic acid + 30%wt citric acid')
plot1.scatter(df2.aw_corrected[cluster == 7], df2.Tf1[cluster == 7], marker='X', color='r',
              label='10%wt glutaric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 8], df2.Tf1[cluster == 8], marker='D', color='r',
              #label='30%wt glutaric acid')
plot1.scatter(df2.aw_corrected[cluster == 9], df2.Tf1[cluster == 9], marker='p', color='r',
              label='5%wt oxalic acid + 10%wt glutaric acid')
plot1.scatter(df2.aw_corrected[cluster == 10], df2.Tf1[cluster == 10], marker=2, color='r',
              label='5%wt oxalic acid + 30%wt glutaric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 11], df2.Tf1[cluster == 11], marker='d', color='r',
              #label='20%wt citric acid')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 12], df2.Tf1[cluster == 12], marker=5, color='r',
              #label='20%wt glutaric acid')
plot1.scatter(df2.aw_corrected[cluster == 13], df2.Tf1[cluster == 13], marker='.', color='r',
              label='5%wt oxalic acid + 20%wt citric acid')
plot1.scatter(df2.aw_corrected[cluster == 14], df2.Tf1[cluster == 14], marker='^', color='r',
              label='5%wt oxalic acid + 20%wt glutaric acid')

#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 1], df2.Tfk[cluster == 1], marker='$H_2O$', color='g')
plot1.scatter(df2.aw_corrected[cluster == 2], df2.Tfk[cluster == 2], marker='$OA$', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 3], df2.Tfk[cluster == 3], marker='o', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 4], df2.Tfk[cluster == 4], marker='s', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 5], df2.Tfk[cluster == 5], marker='P', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 6], df2.Tfk[cluster == 6], marker='*', color='g')
plot1.scatter(df2.aw_corrected[cluster == 7], df2.Tfk[cluster == 7], marker='X', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 8], df2.Tfk[cluster == 8], marker='D', color='g')
plot1.scatter(df2.aw_corrected[cluster == 9], df2.Tfk[cluster == 9], marker='p', color='g')
plot1.scatter(df2.aw_corrected[cluster == 10], df2.Tfk[cluster == 10], marker=2, color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 11], df2.Tfk[cluster == 11], marker='d', color='g')
#NOT INP #plot1.scatter(df2.aw_corrected[cluster == 12], df2.Tfk[cluster == 12], marker=5, color='g')
plot1.scatter(df2.aw_corrected[cluster == 13], df2.Tfk[cluster == 13], marker='.', color='g')
plot1.scatter(df2.aw_corrected[cluster == 14], df2.Tfk[cluster == 14], marker='^', color='g')


plot1.legend()
plot1.invert_xaxis()
plt.xlabel("Water activity", fontweight='bold')
plt.ylabel("Temperature [K]", fontweight='bold')

# Shrink current axis's height by 10% on the bottom
box = plot1.get_position()
plot1.set_position([box.x0, box.y0 + box.height * 0.2, box.width, box.height * 0.8])

# Put a legend below current axis
plot1.legend(loc='upper center', bbox_to_anchor=(0.45, -0.4, 0.1, 0.3), fancybox=True, shadow=True, ncol=3)

plt.show()
