# Python Bill Calculator

A simple beginner-friendly Python project that calculates tax and the final bill amount from a given subtotal and tax percentage.

## Features

- Takes the bill amount as user input
- Takes the tax percentage as user input
- Calculates the tax amount
- Calculates the final total
- Displays the bill summary with two decimal places

## How It Works

The program follows these steps:

1. The user enters the bill amount.
2. The user enters the tax percentage.
3. Tax is calculated using:

   `Tax = Subtotal × Tax Rate / 100`

4. The final bill is calculated using:

   `Total = Subtotal + Tax`

5. The result is displayed as a formatted bill summary.

## Example

### Input

```text
Enter the bill amount: ₹1000
Enter tax percentage: 18
```

### Output

```text
--- Bill Summary ---
Subtotal: ₹1000.00
Tax:      ₹180.00
Total:    ₹1180.00
```

## Concepts Used

- `input()` – Takes input from the user.
- `float()` – Converts input into a decimal number.
- Variables – Stores values such as `subtotal`, `tax_rate`, `tax`, and `total`.
- Arithmetic operators – Used for tax and total calculations.
- f-strings – Used to display variable values in formatted text.
- `.2f` – Displays exactly two digits after the decimal point.

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Install Python 3.x.
2. Save the code as `bill_calculator.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python bill_calculator.py
```

## Project Purpose

This project is designed for beginners learning Python. It demonstrates user input, variables, arithmetic operations, and formatted output through a practical bill-calculation example.
