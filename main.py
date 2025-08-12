def calculate_energy(power_watts, hours_per_day):
    daily_energy = (power_watts * hours_per_day) / 1000
    weekly_energy = daily_energy * 7
    monthly_energy = daily_energy * 30
    yearly_energy = daily_energy * 365
    return daily_energy, weekly_energy, monthly_energy, yearly_energy

for i in range(1, 6):
    print(f"\n--- Appliance {i} ---")
    appliance = input("Enter the appliance name: ")
    power_watts = float(input("Enter the power rating (in watts): "))
    hours_per_day = float(input("Enter daily usage hours: "))

    daily, weekly, monthly, yearly = calculate_energy(power_watts, hours_per_day)

    print(f"\nEnergy Consumption for {appliance}:")
    print(f"Daily: {daily:.2f} kWh")
    print(f"Weekly: {weekly:.2f} kWh")
    print(f"Monthly: {monthly:.2f} kWh")
    print(f"Yearly: {yearly:.2f} kWh")

    if daily > 5:
        print(" Tip: Consider reducing usage or switching to energy-efficient models.")
    else:
        print(" Tip: Your appliance is energy-efficient. Keep it up!")

    