# plots to analyze the data aquired
# this will help us visualize the types of delays and how the year/month/day trends
import pandas as pd
import matplotlib.pyplot as plt

# load merged data csv
df = pd.read_csv("data/cleaned/merged_data.csv")

# visual 1: average delay times (in minutes) by month
df.groupby("MONTH")["ARR_DELAY"].mean().plot(kind="bar")
#titles
plt.title("Average Delay by Month")
plt.xlabel("Month")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks(ticks=range(12), labels=[
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
])

plt.savefig("data/outputs/plots/delay_by_month.png")
plt.close()

# visual 2: average delay times (in minutes) by departure hour
df_filtered = df[df["ARR_DELAY"] < 200] # filtering out outliers that would skew the data
df_filtered.groupby("DEP_HOUR")["ARR_DELAY"].mean().plot()
#titles
plt.title("Average Delay by Departure Hour")
plt.xlabel("Departure Hour (24-hour clock)")
plt.ylabel("Average Arrival Delay (minutes)")

plt.axhline(0) # refrence to 0 delay line
plt.savefig("data/outputs/plots/delay_by_departure_hour.png")
plt.close()

# creating categories
df_filtered["RAIN"] = (df_filtered["precipitation"] > 0).astype(int)
df_filtered["HIGH_WIND"] = (df_filtered["avg_wind_speed"] > 10).astype(int)

df_filtered["TEMP_CATEGORY"] = pd.cut(
    df_filtered["avg_temp"],
    bins=[-100, 50, 70, 200],
    labels=["Cold", "Moderate", "Hot"]
)

# visual 3: rain vs no rain delays
plt.figure()
df_filtered.groupby("RAIN")["ARR_DELAY"].mean().plot(kind="bar")
plt.title("Average Delay: Rain vs No Rain")
plt.xlabel("Weather Condition")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks([0, 1], ["No Rain", "Rain"], rotation=0)
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_rain_vs_no_rain.png")
plt.close()

# visual 4: high wind vs low wind delays
plt.figure()
df_filtered.groupby("HIGH_WIND")["ARR_DELAY"].mean().plot(kind="bar")
plt.title("Average Delay: High Wind vs Low Wind")
plt.xlabel("Wind Condition")
plt.ylabel("Average Arrival Delay (minutes)")
plt.xticks([0, 1], ["Low Wind", "High Wind"], rotation=0)
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_high_wind_vs_low_wind.png")
plt.close()

# visual 5: delay by temperature category
plt.figure()
df_filtered.groupby("TEMP_CATEGORY")["ARR_DELAY"].mean().plot(kind="bar")
plt.title("Average Delay by Temperature Category")
plt.xlabel("Temperature Category")
plt.ylabel("Average Arrival Delay (minutes)")
plt.tight_layout()
plt.savefig("data/outputs/plots/delay_by_temperature_category.png")
plt.close()
