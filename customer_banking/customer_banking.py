# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_CD_account


# Define the main function
def main():
    
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your current savings balance"))
    interest_rate = float(input("What is your current interest rate"))
    months = int(input("What is the amount of months your savings account has been open"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_balance , interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(interest_earned)
    print(updated_balance)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is the CD balance"))
    interest_rate= float(input("what is the CD interest rate"))
    months = int(input("What is your amount of months that your CD term is for"))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_CD_account(cd_balance , interest_rate , months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(updated_cd_balance , cd_interest_earned )

if __name__ == "__main__":
    # Call the main function.
    main()