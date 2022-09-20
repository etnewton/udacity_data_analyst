import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

data_set = pd.read_csv("processed_data.csv")

fig, ax = plt.subplots()

ax.plot(data_set["year"][24:], data_set["avg_temp_louisville_25y_avg"][24:], label="Louisville")
ax.plot(data_set["year"][24:], data_set["avg_temp_25y_avg"][24:], label="Global")

ax.set(xlabel="Year", ylabel="Temperature (°C)", title="25 Year Moving Average")

ax.legend(loc="right")

ax.grid()

plt.fill_between(data_set["year"][24:], data_set["avg_temp_louisville_25y_avg"][24:], data_set["avg_temp_25y_avg"][24:], color="grey", alpha=0.3)

fig.savefig("25yr_Avg.png")


fig, ax = plt.subplots()

ax.plot(data_set["year"][9:], data_set["avg_temp_louisville_10y_avg"][9:], label="Louisville")
ax.plot(data_set["year"][9:], data_set["avg_temp_10y_avg"][9:], label="Global")

ax.set(xlabel="Year", ylabel="Temperature (°C)", title="10 Year Moving Average")
ax.legend(loc="right")
ax.grid()

plt.fill_between(data_set["year"][9:], data_set["avg_temp_louisville_10y_avg"][9:], data_set["avg_temp_10y_avg"][9:], color="grey", alpha=0.3)

fig.savefig("10yr_Avg.png")

fig, ax = plt.subplots()

ax.plot(data_set["year"][99:], data_set["avg_temp_louisville_100y_avg"][99:], label="Louisville")
ax.plot(data_set["year"][99:], data_set["avg_temp_100y_avg"][99:], label="Global")

ax.set(xlabel="Year", ylabel="Temperature (°C)", title="100 Year Moving Average")
ax.legend(loc="right")
ax.grid()

plt.fill_between(data_set["year"][99:], data_set["avg_temp_louisville_100y_avg"][99:], data_set["avg_temp_100y_avg"][99:], color="grey", alpha=0.3)

fig.savefig("100yr_Avg.png")

fig, ax = plt.subplots()

ax.plot(data_set["year"][99:], data_set["avg_temp_louisville_100y_delta"][99:], label="Louisville")
ax.plot(data_set["year"][99:], data_set["avg_temp_100y_delta"][99:], label="Global")

ax.set(xlabel="Year", ylabel="Temperature (°C)", title="Change Over Year (100 Year Moving Average)")
ax.legend(loc="right")
ax.grid()

plt.fill_between(data_set["year"][99:], data_set["avg_temp_louisville_100y_delta"][99:], data_set["avg_temp_100y_delta"][99:], color="grey", alpha=0.3)

fig.savefig("100yr_Year_Delta.png")
