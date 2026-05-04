# plots to analyze the data aquired
# this will help us visualize the types of delays and how the year/month/day trends
import pandas as pd
import matplotlib.pyplot as plt

# load merged data csv
df = pd.read_csv("data/cleaned/merged_data.csv")

# visual 1: average delay times (in minutes) by month
df.groupby("MONTH")["ARR_DELAY"].mean().plot(kind="bar")
#titles of graph
plt.title("Average Delay by Month")
plt.xlabel("Month")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks(ticks=range(12), labels=[ # label by month
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"])

# where to save graphs
plt.savefig("data/outputs/plots/delay_by_month.png")
plt.close()

# visual 2: average delay times (in minutes) by departure hour
# filtering out outliers that would skew the data. (both extemely early or extremely delayed flights)
# we do this to be more realistic with calculations rather than use an exteme scenario to predict normal delays
df_filtered = df[(df["ARR_DELAY"] > -60) & (df["ARR_DELAY"] < 200)].copy()  
df_filtered.groupby("DEP_HOUR")["ARR_DELAY"].mean().plot()
#titles
plt.title("Average Delay by Departure Hour")
plt.xlabel("Departure Hour (24-hour clock)")
plt.ylabel("Average Arrival Delay (minutes)")

plt.axhline(0) # refrence to 0 delay line
plt.savefig("data/outputs/plots/delay_by_departure_hour.png")
plt.close()

# creating categories
df_filtered["RAIN"] = (df_filtered["precipitation"] >0).astype(int)
df_filtered["HIGH_WIND"] = (df_filtered["avg_wind_speed"] >10).astype(int)

df_filtered["TEMP_CATEGORY"] = pd.cut( # creating temp bins to make bar graph
    df_filtered["avg_temp"],
    bins= [-100, 45, 55, 65, 75, 200],
    labels=["<45°F", "45–55°F", "55–65°F", "65–75°F", ">75°F"])

# visual 3: rain vs no rain delays (bar graphs)
plt.figure()
df_filtered.groupby("RAIN")["ARR_DELAY"].mean().plot(kind="bar")
plt.title("Average Delay: Rain vs No Rain")
plt.xlabel("Weather Condition")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks([0, 1], ["No Rain","Rain"], rotation=0)
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_rain_vs_no_rain.png")
plt.close()

# visual 4: high wind vs low wind delays (bar graphs)
plt.figure()
df_filtered.groupby("HIGH_WIND")["ARR_DELAY"].mean().plot(kind="bar")
plt.title("Average Delay: High Wind vs Low Wind")
plt.xlabel("Wind Condition")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks([0, 1], ["Low Wind","High Wind"], rotation=0)
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_high_wind_vs_low_wind.png")
plt.close()

# visual 5: delay by temperature category (bar graphs with temp bins initialized earlier)
plt.figure()
df_filtered.groupby("TEMP_CATEGORY", observed=True)["ARR_DELAY"].mean().sort_index().plot(kind="bar")
plt.title("Average Delay by Temperature Category")
plt.xlabel("Temperature Category")
plt.ylabel("Average Arrival Delay (minutes)")
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_by_temperature_category.png")
plt.close()
