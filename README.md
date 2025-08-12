# ⚡ Energy Consumption Calculator (Python)

This is a simple Python program that calculates the daily, weekly, monthly, and yearly energy usage of appliances based on their power rating (in watts) and daily usage hours. It also gives tips on whether the appliance is energy-efficient or not.

## How It Works
The program asks you to enter details for 5 appliances. For each appliance, you provide:
- Appliance name
- Power rating in watts
- Daily usage hours

The program then calculates:
- **Daily energy usage** = (Power in Watts × Hours per day) ÷ 1000
- **Weekly energy usage** = Daily × 7
- **Monthly energy usage** = Daily × 30
- **Yearly energy usage** = Daily × 365

If the daily usage is above 5 kWh, the program suggests reducing usage or switching to energy-efficient models. If it is 5 kWh or below, it praises your efficiency.

## How to Run
1. Make sure you have **Python 3.x** installed on your computer.
2. Download this file and save it as `energy_calculator.py`.
3. Open a terminal or command prompt in the folder where the file is saved.
4. Run:
   ```bash
   python energy_calculator.py
