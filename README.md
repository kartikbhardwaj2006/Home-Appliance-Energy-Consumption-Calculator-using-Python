⚡ Energy Consumption Calculator (Python)
This is a simple Python program that calculates the daily, weekly, monthly, and yearly energy usage of appliances based on their power rating (in watts) and daily usage hours. It also gives tips on whether the appliance is energy-efficient or not.

📜 How It Works
The program asks you to enter details for 5 appliances. For each appliance, you provide:

Appliance name

Power rating in watts

Daily usage hours

It then calculates:

Daily energy usage = (Power in Watts × Hours per day) ÷ 1000

Weekly energy usage = Daily × 7

Monthly energy usage = Daily × 30

Yearly energy usage = Daily × 365

If the daily usage is above 5 kWh, the program suggests reducing usage or switching to energy-efficient models.
If it is 5 kWh or below, it praises your efficiency.

💻 Code
python
Copy
Edit
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
▶️ How to Run
Install Python 3.x on your computer.

Save the above code as energy_calculator.py.

Open a terminal in the folder where you saved the file.

Run:

bash
Copy
Edit
python energy_calculator.py
📌 Example Output
yaml
Copy
Edit
--- Appliance 1 ---
Enter the appliance name: Refrigerator
Enter the power rating (in watts): 150
Enter daily usage hours: 24

Energy Consumption for Refrigerator:
Daily: 3.60 kWh
Weekly: 25.20 kWh
Monthly: 108.00 kWh
Yearly: 1314.00 kWh
 Tip: Your appliance is energy-efficient. Keep it up!

--- Appliance 2 ---
Enter the appliance name: Air Conditioner
Enter the power rating (in watts): 1500
Enter daily usage hours: 8

Energy Consumption for Air Conditioner:
Daily: 12.00 kWh
Weekly: 84.00 kWh
Monthly: 360.00 kWh
Yearly: 4380.00 kWh
 Tip: Consider reducing usage or switching to energy-efficient models.
📄 License
MIT License

Copyright (c) 2025 Kartik Bhardwaj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
