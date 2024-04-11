# ENERGY USAGE ANALYSIS
import matplotlib.pyplot as plt

# Example Values
monthly_electricity_bill = 200  # USD
monthly_gas_bill = 100  # USD
monthly_fuel_bill = 150  # USD

# Conversion factors
electricity_conversion_factor = 0.0005
gas_conversion_factor = 0.0053
fuel_conversion_factor = 2.32

# Calculate Energy Usage
electricity_usage = monthly_electricity_bill * 12 * electricity_conversion_factor
gas_usage = monthly_gas_bill * 12 * gas_conversion_factor
fuel_usage = monthly_fuel_bill * 12 * fuel_conversion_factor

# Pie Chart
labels = ['Electricity', 'Gas', 'Fuel']
values = [electricity_usage, gas_usage, fuel_usage]
plt.figure(figsize=(8, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Energy Usage Breakdown')
plt.axis('equal')
plt.show()




# TRANSPORTATION USAGE ANALYSIS
import matplotlib.pyplot as plt

# Example Values
total_kilometers_traveled_per_year = 20000  # km
average_fuel_efficiency = 10  # L/100km

# Conversion factor
emissions_conversion_factor = 2.31

# Calculate Transportation Emissions
transport_emissions = total_kilometers_traveled_per_year * (1 / average_fuel_efficiency) * emissions_conversion_factor

# Bar Graph
plt.figure(figsize=(8, 6))
plt.bar('Transportation', transport_emissions, color='orange')
plt.xlabel('Component')
plt.ylabel('CO2e (kg)')
plt.title('Transportation Emissions')
plt.show()

# WASTE GENERATION ANALYSIS
import matplotlib.pyplot as plt

# Example Values
total_waste_generated_per_month = 40  # kg
recycling_percentage = 70  # %

# Conversion factor
waste_emissions_factor = 0.57

# Calculate Waste Emissions
waste_emissions = total_waste_generated_per_month * 12 * waste_emissions_factor * (1 - recycling_percentage / 100)

# Pie Chart
labels = ['Waste', 'Recycling']
values = [waste_emissions, total_waste_generated_per_month - waste_emissions]
plt.figure(figsize=(8, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'lightgreen'])
plt.title('Waste Generation and Recycling')
plt.axis('equal')
plt.show()




# OVERALL CARBON FOOTPRINT ANALYSIS
import matplotlib.pyplot as plt

# Example Values
total_waste_generated_per_month = 40  # kg
recycling_percentage = 70  # %

# Conversion factor
waste_emissions_factor = 0.57

# Calculate Waste Emissions
waste_emissions = total_waste_generated_per_month * 12 * waste_emissions_factor * (1 - recycling_percentage / 100)

# Pie Chart
labels = ['Waste', 'Recycling']
values = [waste_emissions, total_waste_generated_per_month - waste_emissions]
plt.figure(figsize=(8, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'lightgreen'])
plt.title('Waste Generation and Recycling')
plt.axis('equal')
plt.show()