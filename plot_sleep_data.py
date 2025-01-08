import garth
import matplotlib.pyplot as plt

garth.resume(".garth")
sleep_datas = garth.SleepData.get(
    "2025-01-04",  # it seems like this is always GMT
    buffer_minutes=60  # controls start and stop margins beyond the window where garmin truly thinks you're sleeping
)
sleep_movements = sleep_datas.sleep_movement

# Prepare data for plotting
start_times = [data.start_gmt for data in sleep_movements]
activity_levels = [data.activity_level for data in sleep_movements]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(start_times, activity_levels, marker='o', label="Activity Level")
plt.title("Sleep Movement Activity Levels Over Time")
plt.xlabel("Time (GMT)")
plt.ylabel("Activity Level")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

breakpoint()
