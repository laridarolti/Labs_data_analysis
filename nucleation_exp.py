import scipy.io
import numpy as np
import matplotlib.pyplot as plt

directory = {1: "C:/Users/kayfr/Downloads/nucleation_experiment_data_with_plots/nucleation_experiment_data"
                "/220411_group3_Sample1/",
             2: "C:/Users/kayfr/Downloads/nucleation_experiment_data_with_plots/nucleation_experiment_data"
                "/220411_group3_Sample2/",
             3: "C:/Users/kayfr/Downloads/nucleation_experiment_data_with_plots/nucleation_experiment_data"
                "/220411_group3_Sample3/",
             4: "C:/Users/kayfr/Downloads/nucleation_experiment_data_with_plots/nucleation_experiment_data"
                "/220411_group3_Sample4/"}

nfrz = {1: scipy.io.loadmat(directory[1] + 'nFrz_auto.mat', simplify_cells="False"),
        2: scipy.io.loadmat(directory[2] + 'nFrz_auto.mat', simplify_cells="False"),
        3: scipy.io.loadmat(directory[3] + 'nFrz_auto.mat', simplify_cells="False"),
        4: scipy.io.loadmat(directory[4] + 'nFrz_auto.mat', simplify_cells="False")}

T = {1: scipy.io.loadmat(directory[1] + "T_auto.mat", simplify_cells="False"),
     2: scipy.io.loadmat(directory[2] + "T_auto.mat", simplify_cells="False"),
     3: scipy.io.loadmat(directory[3] + "T_auto.mat", simplify_cells="False"),
     4: scipy.io.loadmat(directory[4] + "T_auto.mat", simplify_cells="False")}

# Dict with values for all samples (1-4) and the corresponding Values for Temperature,
# amount of frozen wells and the frozen fraction
T = {1: T[1]["T_auto"]+273.15, 2: T[2]["T_auto"]+273.15, 3: T[3]["T_auto"]+273.15, 4: T[4]["T_auto"]+273.15}
nfrz = {1: nfrz[1]["nFrz"], 2: nfrz[2]["nFrz"], 3: nfrz[3]["nFrz"], 4: nfrz[4]["nFrz"]}
FF = {1: nfrz[1] / 96, 2: nfrz[2] / 96, 3: nfrz[3] / 96, 4: nfrz[4] / 96}

# Error for the frozen fraction, volume of the aliquot and a time dict (different sample, different measurement lengths)
FF_err = 0.03
V = 50 * 10 ** (-6)
t = np.arange(0, len(T[1])*15, 15)
n_well = 96  # number of wells
dcf = V / 0.05

# Calculate the theoretical homogeneous freezing rate
A_hom = 1 - np.exp(-10 ** 6 * np.exp(-3.5 * (T[1] - 235) + 19) * V * t)

# Plotting the frozen fraction with error bars as a function of temperature
# Slicing arrays to make samples more distinguishable from each other
plt.figure(1)
for i in range(1, 5):
    plt.plot(T[i][50:], FF[i][50:], label="Sample_" + str(i))
    plt.fill_between(T[i][50:], FF[i][50:] - FF_err, FF[i][50:] + FF_err, alpha=0.3)
plt.plot(T[1][50:], A_hom[50:], label="Theor. homo. freezing")
plt.axhline(0.5, 0, 1, color="k", linestyle="--", linewidth=0.5)
plt.title("Frozen fraction vs. Temperature")
plt.xlabel("Temperature [K]")
plt.ylabel("Frozen fraction")
plt.legend()
plt.savefig("frozen_fraction_temp", dpi=500, bbox_inches="tight")
# plt.show()

# Calculation of INP concentration and error propagation
INP = {1: np.log(n_well/(n_well - nfrz[1]))/V, 2: np.log(n_well/(n_well - nfrz[2]))/V,
       3: np.log(n_well/(n_well - nfrz[3]))/V, 4: np.log(n_well/(n_well - nfrz[4]))/V}
INP_err = 200 #np.sqrt((3 / 96) ** 2)

# plot of the INP concentrations with error bars
plt.figure(2)
for i in range(1, 5):
    plt.plot(T[i][50:], INP[i][50:], label="Sample_" + str(i))
    plt.fill_between(T[i][50:], INP[i][50:] - INP_err, INP[i][50:] + INP_err, alpha=0.3)
# plt.axhline(0.5, 0, 1, color="k", linestyle="--", linewidth=0.5)
plt.title("INP vs. Temperature")
plt.xlabel("Temperature [K]")
plt.ylabel("INP [1/l]")
plt.legend()
plt.savefig("inp_temp", dpi=500, bbox_inches="tight")
# plt.show()

