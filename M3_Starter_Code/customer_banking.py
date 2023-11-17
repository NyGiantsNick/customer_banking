# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from Account import Account
from Account import SavingsAccount
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = (float(input("Please enter your savings account balance: ")))
    interest_rate = (float(input("Please enter the APR interest rate for your savings account: ")))
    savings_maturity = (int(input("Please enter the number of months you've had this savings account: ")))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance = create_savings_account(savings_balance, interest_rate, savings_maturity)
    interest_earned_savings = (float((interest_rate/100) * (savings_maturity)))

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Interest earned on savings accoung: {interest_earned_savings:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter the initial CD account balance: "))
    interest_rate = float(input("Enter the APR interest rate for the CD account: "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    interest_earned_cd = create_cd_account(cd_balance, interest_rate, cd_maturity)
    updated_cd_balance = cd_balance * (float((interest_rate/100) * (cd_maturity)))
    print(f"Updated CD account balance with interest: {interest_earned_cd}")
   
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest your CD account has earned is ${updated_cd_balance:.2f}.")
    

if __name__ == "__main__":

    # Call the main function.
    main()