# tax calculator program
# a program that calculates the net salary of an individual in the UK

import tkinter as tk


def calculate_net_salary(gross_salary):
    # Constants for tax bands and rates
    basic_rate_threshold = 50000
    higher_rate_threshold = 150000
    basic_rate = 0.20
    higher_rate = 0.40
    additional_rate = 0.45

    # Calculate Personal Allowance
    personal_allowance = 12500
    if gross_salary > 100000:
        reduction = (gross_salary - 100000) / 2
        personal_allowance = max(0, personal_allowance - reduction)

    # Calculate taxable income
    taxable_income = max(0, gross_salary - personal_allowance)

    # Calculate tax
    tax = 0
    if taxable_income > higher_rate_threshold:
        tax += (taxable_income - higher_rate_threshold) * additional_rate
        taxable_income = higher_rate_threshold
    if taxable_income > basic_rate_threshold:
        tax += (taxable_income - basic_rate_threshold) * higher_rate
        taxable_income = basic_rate_threshold
    tax += taxable_income * basic_rate

    # Calculate net salary
    net_salary = gross_salary - tax
    return net_salary


def calculate_and_display_net_salary():
    try:
        # Get the input and remove commas
        gross_salary_str = gross_salary_entry.get().replace(',', '')
        gross_salary = float(gross_salary_str)

        # Calculate and display the net salary
        net_salary = calculate_net_salary(gross_salary)
        net_salary_result_label.config(text=f"Net Salary: £{net_salary:.2f}")
    except ValueError:
        net_salary_result_label.config(text="Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("UK Tax Calculator")

# Create and place widgets
gross_salary_label = tk.Label(root, text="Gross Salary (£):")
gross_salary_label.pack()

gross_salary_entry = tk.Entry(root)
gross_salary_entry.pack()

calculate_button = tk.Button(
    root, text="Calculate", command=calculate_and_display_net_salary)
calculate_button.pack()

net_salary_result_label = tk.Label(root, text="Net Salary: £0.00")
net_salary_result_label.pack()

# Run the application
root.mainloop()

# gross = int(input("What is your gross income: "))
# print(f" your net salary = {calculate_net_salary(gross)}")
