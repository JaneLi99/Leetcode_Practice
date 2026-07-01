# Tax Obligation
# To know when a business needs to start paying taxes in a given region, we need to calculate the sales tax / VAT of the products they have sold in a period.
# Different product categories have different tax rates and are distinguished by a "product tax code".
# Write a function, calculate_sales_tax, that takes a set of tax rates and sales and calculates the amount of sales tax owed in each region.
#
# Input
# The parameters to the calculate_sales_tax function will be two lists of CSV-formatted strings.
# The first, tax_rates, contains entries in the format: start_date,region,product_tax_code,tax_rate
# The second, sales, contains entries in the format: date,region,product_tax_code,EXC/INC,price
#
# start_date and date are in the format YYYY-MM-DD
# tax_rate is a percentage expressed as a decimal number from 0.00 to 100.00
# EXC/INC indicates whether the price is tax-exclusive or tax-inclusive (see Part 2)
#
# Output
# The output should be a list of strings in the format:
# region1,total_tax_owed1
# region2,total_tax_owed2
# ...
# regionN,total_tax_owedN
#
# Format total_tax_owed to two decimal places
# Order results lexicographically by region
#
# Part 1 — Basic EXC Tax Calculation
# Calculate the amount of sales tax owed in each region. Assume all prices are tax-exclusive (EXC) — meaning tax is added on top of the price.
# Formula:
# tax = price × (tax_rate / 100)
# You may also assume in Part 1 that each (region, product_tax_code) pair has exactly one tax rate and that the start_date can be ignored.
# Example:
# pythontax_rates = [
#     "2024-01-01,US,general,10.00",
#     "2024-01-01,EU,general,20.00",
# ]
#
# sales = [
#     "2024-03-15,US,general,EXC,200.00",
#     "2024-03-15,EU,general,EXC,500.00",
# ]
#
# # Expected output:
# # EU,100.00
# # US,20.00
#
# Part 2 — INC (Tax-Inclusive) Support
# Extend your solution to handle both EXC and INC prices.
#
# EXC (tax-exclusive): tax is added on top of the listed price
# INC (tax-inclusive): tax is already embedded inside the listed price
#
# Formulas:
# EXC → tax = price × (tax_rate / 100)
# INC → tax = price × (tax_rate / (100 + tax_rate))
# Example:
# pythontax_rates = [
#     "2024-01-01,US,general,10.00",
#     "2024-01-01,US,food,5.00",
#     "2024-01-01,EU,general,20.00",
# ]
#
# sales = [
#     "2024-03-15,US,general,EXC,200.00",  # tax = 200 × 10/100       = 20.00
#     "2024-03-15,US,food,INC,105.00",     # tax = 105 × 5/105        =  5.00
#     "2024-03-15,EU,general,INC,120.00",  # tax = 120 × 20/120       = 20.00
#     "2024-03-15,EU,general,EXC,500.00",  # tax = 500 × 20/100       = 100.00
# ]
#
# # Expected output:
# # EU,120.00
# # US,25.00
#
# Part 3 — Tax Rates with Effective Dates
# Extend your solution to handle multiple tax rates for the same (region, product_tax_code) pair, each with a different start_date.
# For each sale, apply the tax rate whose start_date is the most recent date that is on or before the sale's date. If no tax rate is applicable (i.e. all rates start after the sale date), skip that sale.
# Example:
# pythontax_rates = [
#     "2024-01-01,US,general,10.00",   # applies Jan–May
#     "2024-06-01,US,general,12.00",   # applies Jun onwards
#     "2024-01-01,US,food,5.00",
#     "2024-01-01,EU,general,20.00",
# ]
#
# sales = [
#     "2024-03-15,US,general,EXC,200.00",  # uses 10% → tax = 20.00
#     "2024-07-01,US,general,EXC,100.00",  # uses 12% → tax = 12.00
#     "2024-03-15,US,food,INC,105.00",     # uses  5% → tax =  5.00
#     "2024-03-15,EU,general,EXC,500.00",  # uses 20% → tax = 100.00
#     "2024-03-15,EU,general,INC,120.00",  # uses 20% → tax = 20.00
# ]
#
# # Expected output:
# # EU,120.00
# # US,37.00
#
# Constraints
# 1 ≤ len(tax_rates) ≤ 1000
# 1 ≤ len(sales) ≤ 1000
# tax_rate is between 0.00 and 100.00 inclusive
# price is a positive decimal number
# region and product_tax_code are non-empty strings
# Dates are valid and in YYYY-MM-DD format
# EXC or INC are the only possible values for the tax type field
# In Part 1, each (region, product_tax_code) pair has exactly one tax rate

from collections import defaultdict
from datetime import date

def calculate_sales_tax(tax_rates, sales):
    rate_map = defaultdict(list)

    for entry in tax_rates:
        parts = entry.strip().split(",")
        start_date = date.fromisoformat(parts[0])
        region = parts[1]
        product_tax_code = parts[2]
        tax_rate = float(parts[3])

        rate_map[(region, product_tax_code)].append((start_date, tax_rate))

    # Sort each group by date so we can binary search / iterate
    for key in rate_map:
        rate_map[key].sort(key=lambda x: x[0])

    def get_tax_rate(region, product_tax_code, sale_date):
        entries = rate_map.get((region, product_tax_code), [])
        applicable_rate = None
        for start_date, rate in entries:
            if start_date <= sale_date:
                applicable_rate = rate  # keep updating → last one wins
            else:
                break  # list is sorted, no point continuing
        return applicable_rate

    region_tax = defaultdict(float)

    for entry in sales:
        parts = entry.strip().split(",")
        sale_date = date.fromisoformat(parts[0])
        region = parts[1]
        product_tax_code = parts[2]
        exc_or_inc = parts[3].strip().upper()
        price = float(parts[4])

        tax_rate = get_tax_rate(region, product_tax_code, sale_date)

        if tax_rate is None:
            continue

        if exc_or_inc == "EXC":
            tax = price * (tax_rate / 100)
        elif exc_or_inc == "INC":
            tax = price * (tax_rate / (100 + tax_rate))
        else:
            tax = 0.0

        region_tax[region] += tax


    result = []
    for region in sorted(region_tax.keys()):
        result.append(f"{region},{region_tax[region]:.2f}")

    return result


# ── Example Input ──────────────────────────────────────────────
def main():
    tax_rates = [
        "2024-01-01,US,general,10.00",
        "2024-01-01,US,food,5.00",
        "2024-01-01,EU,general,20.00",
        "2024-06-01,US,general,12.00",   # rate change mid-year
    ]

    sales = [
        "2024-03-15,US,general,EXC,200.00",  # rate=10% → tax=20.00
        "2024-03-15,US,food,INC,105.00",     # rate=5%  → tax=105*(5/105)=5.00
        "2024-07-01,US,general,EXC,100.00",  # rate=12% (after Jun 1) → tax=12.00
        "2024-03-15,EU,general,EXC,500.00",  # rate=20% → tax=100.00
        "2024-03-15,EU,general,INC,120.00",  # rate=20% → tax=120*(20/120)=20.00
    ]

    output = calculate_sales_tax(tax_rates, sales)
    print(output)

if __name__ == "__main__":
    main()

