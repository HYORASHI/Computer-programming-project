import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class CarbonFootprint:
    def __init__(self, monthly_electricity_bill, monthly_gas_bill, monthly_fuel_bill, total_waste_generated_per_month, recycling_percentage, total_kilometers_traveled_per_year, average_fuel_efficiency):
        self.monthly_electricity_bill = monthly_electricity_bill
        self.monthly_gas_bill = monthly_gas_bill
        self.monthly_fuel_bill = monthly_fuel_bill
        self.total_waste_generated_per_month = total_waste_generated_per_month
        self.recycling_percentage = recycling_percentage
        self.total_kilometers_traveled_per_year = total_kilometers_traveled_per_year
        self.average_fuel_efficiency = average_fuel_efficiency

    def calculate_energy_usage(self):
        return (self.monthly_electricity_bill * 12 * 0.0005) + (self.monthly_gas_bill * 12 * 0.0053) + (self.monthly_fuel_bill * 12 * 2.32)

    def calculate_gas_consumption(self):
        return self.monthly_gas_bill * 12 * 0.0053

    def calculate_transportation_emissions(self):
        return self.total_kilometers_traveled_per_year * (1 / self.average_fuel_efficiency) * 2.31

    def calculate_carbon_footprint(self):
        return self.calculate_energy_usage() + self.calculate_waste() + self.calculate_transportation_emissions()

    def calculate_waste(self):
        return self.total_waste_generated_per_month * 12 * (0.57 - (self.recycling_percentage / 100))

    def generate_suggestions(self):
        suggestions = []

        # Calculate the optimal energy usage based on certain criteria
        optimal_energy_usage = self.calculate_optimal_energy_usage()

        if self.calculate_energy_usage() > optimal_energy_usage:
            suggestions.append(f"Consider reducing energy usage to {optimal_energy_usage} kgCO2e to optimize carbon footprint.")
        elif self.calculate_energy_usage() < optimal_energy_usage:
            suggestions.append(f"Consider increasing energy usage to {optimal_energy_usage} kgCO2e to optimize carbon footprint.")

        # Other suggestions for reducing carbon footprint
        if self.calculate_gas_consumption() > 50:
            suggestions.append("Improve home insulation and consider upgrading to a more efficient heating system.")
        if self.calculate_transportation_emissions() > 2.5:
            suggestions.append("Use public transportation, carpool, or consider electric/hybrid vehicles for transportation.")
        if self.recycling_percentage < 70:
            suggestions.append("Increase recycling efforts and reduce waste generation.")
        if self.total_waste_generated_per_month > 20:
            suggestions.append("Compost organic waste and reduce single-use items to decrease landfill waste.")

        return suggestions

    def calculate_optimal_energy_usage(self):
        # Calculate the optimal energy usage based on certain criteria
        # Example: Reduce energy usage by 20% for optimization
        return self.calculate_energy_usage() * 0.8

    def generate_graphs(self):
        labels = ['Energy Usage', 'Waste', 'Business Travel']
        values = [self.calculate_energy_usage(), self.calculate_waste(), self.calculate_transportation_emissions()]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'green', 'orange'])
        plt.xlabel('Carbon Footprint Component')
        plt.ylabel('CO2e (kg)')
        plt.title('Carbon Footprint Breakdown')
        plt.show()

    def generate_report(self):
        report = SimpleDocTemplate("carbon_footprint_report.pdf", pagesize=letter)
        data = [['Component', 'CO2e (kg)'],
                ['Energy Usage', self.calculate_energy_usage()],
                ['Waste', self.calculate_waste()],
                ['Business Travel', self.calculate_transportation_emissions()],
                ['Total', self.calculate_carbon_footprint()]]

        table = Table(data)
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
        report.build([table])

def main():
    try:
        monthly_electricity_bill = float(input("Enter monthly electricity bill: "))
        monthly_gas_bill = float(input("Enter monthly gas bill: "))
        monthly_fuel_bill = float(input("Enter monthly fuel bill: "))
        total_waste_generated_per_month = float(input("Enter total waste generated per month (in kg): "))
        recycling_percentage = float(input("Enter recycling/composting percentage (%): "))
        total_kilometers_traveled_per_year = float(input("Enter total kilometers traveled per year for business purposes: "))
        average_fuel_efficiency = float(input("Enter average fuel efficiency (in L/100km): "))

        carbon_footprint = CarbonFootprint(monthly_electricity_bill, monthly_gas_bill, monthly_fuel_bill, total_waste_generated_per_month, recycling_percentage, total_kilometers_traveled_per_year, average_fuel_efficiency)

        total_carbon_footprint = carbon_footprint.calculate_carbon_footprint()

        print("\nCarbon Footprint Breakdown:")
        print(f"Energy Usage: {carbon_footprint.calculate_energy_usage()} kgCO2e")
        print(f"Waste: {carbon_footprint.calculate_waste()} kgCO2e")
        print(f"Business Travel: {carbon_footprint.calculate_transportation_emissions()} kgCO2e")
        print("-------------------------")
        print(f"Total Carbon Footprint: {total_carbon_footprint} kgCO2e")

        print("\nSuggestions for reducing carbon footprint:")
        for suggestion in carbon_footprint.generate_suggestions():
            print("-", suggestion)

        # Generate graphs
        carbon_footprint.generate_graphs()

        # Generate report
        carbon_footprint.generate_report()

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
