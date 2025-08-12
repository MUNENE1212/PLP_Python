def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount and subtract from original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price


# Main program - get user input and calculate final price
def main():
    try:
        # Get original price from user
        price = float(input("Enter the original price of the item: $"))
        
        # Get discount percentage from user
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price using the function
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied (less than 20%). Original price: ${final_price:.2f}")
            
    except ValueError:
        print("Please enter valid numeric values.")


# Run the program
if __name__ == "__main__":
    main()