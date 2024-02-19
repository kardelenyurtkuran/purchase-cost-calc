# purchase-cost-calc
PurchaseCostCalc is a Python program for automatically calculating costs based on Excel BOM (Bill of Materials) lists. This program retrieves prices from online sources using the links provided in the specified Excel file and adds them to the BOM list. As a result, it provides the user with the total cost.

## How It Works?

PurchaseCostCalc is developed in Python and follows the basic steps below:

1. The user uploads an Excel file and specifies the BOM list.
2. The program retrieves prices from online sources using the provided links for each product.
3. The obtained prices are added to the relevant cells in the Excel file.
4. The program sums up all prices and calculates the total cost.
5. It presents the total cost and detailed information to the user.

## How to Use?

1. Install Python (specified version in the requirements file).
2. Install the required libraries: pip install -r requirements.txt.
3. Run the program: python ExcelCostCalc.py.
4. Follow the instructions and upload your Excel file.

## Requirements
- Python 3.x
- Pandas
- openpyxl
- requests

## Data Sources

PurchaseCostCalc retrieves data from the following websites for cost calculation:

- [OZDISAN](https://ozdisan.com/): This site is used to fetch product prices.

These websites are used solely for the purpose of cost calculation and not for other purposes of the project.

## Sample BOM Lists

To provide sample BOM lists for usage in the project, there is a folder named "Sample_BOM_lists". This folder contains various example BOM lists to help understand and test the project's functionality.

## Contribution
See contribution guidelines for details on how to contribute to this project.

## License
This project is licensed under the MIT License. Refer to the LICENSE file for more information.
