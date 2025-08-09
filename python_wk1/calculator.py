def calculator():
    print("Simple Calculator")
    print("-" * 20)
    
    try:
        # Get operation first
        print("Available operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter an operation (+, -, *, /): ").strip()
        
        # Get numbers based on operation type with explanations
        if operation == '+':
            print("\nFor addition, we need two addends (numbers to be added together)")
            num1 = float(input("Enter the first addend: "))
            num2 = float(input("Enter the second addend: "))
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result}")
            
        elif operation == '-':
            print("\nFor subtraction:")
            print("- Minuend: the number you're subtracting FROM")
            print("- Subtrahend: the number you're subtracting")
            num1 = float(input("Enter the minuend: "))
            num2 = float(input("Enter the subtrahend: "))
            result = num1 - num2
            print(f"The difference of {num1} and {num2} is {result}")
            
        elif operation == '*':
            print("\nFor multiplication:")
            print("- Multiplicand: the number being multiplied")
            print("- Multiplier: the number you multiply by")
            num1 = float(input("Enter the multiplicand: "))
            num2 = float(input("Enter the multiplier: "))
            result = num1 * num2
            print(f"The product of {num1} and {num2} is {result}")
            
        elif operation == '/':
            print("\nFor division:")
            print("- Dividend: the number being divided")
            print("- Divisor: the number you divide by")
            num1 = float(input("Enter the dividend: "))
            num2 = float(input("Enter the divisor: "))
            if num2 != 0:
                result = num1 / num2
                print(f"The quotient of {num1} and {num2} is {result}")
            else:
                print("Error: Division by zero is not allowed!")
                
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    calculator()