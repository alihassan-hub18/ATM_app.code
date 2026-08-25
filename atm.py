import datetime


class ATMSystem:

  def __init__(self, account_holder, pin, initial_balance=0.0):
    self.account_holder = account_holder
    self.__pin = pin  # Private variable for security
    self.balance = initial_balance
    self.transaction_history = []
    self.is_authenticated = False 

  def authenticate(self):
    print("\n" + "=" * 50)
    print("             SECURE ATM LOGIN")
    print("=" * 50)
    attempts = 3
    while attempts > 0:
      entered_pin = input("Enter your 4-digit PIN: ").strip()
      if entered_pin == self.__pin:
        print(
            "\033[92m[+] Authentication Successful! Welcome,"
            f" {self.account_holder}\033[0m"
        )
        self.is_authenticated = True
        return True
      else:
        attempts -= 1
        print(
            f"\033[91m[-] Incorrect PIN. Attempts remaining:"
            f" {attempts}\033[0m"
        )
    print("\033[91m[-] Card blocked due to multiple incorrect attempts.\033[0m")
    return False

  def check_balance(self):
    print("\n" + "-" * 50)
    print(f"Current Account Balance: ${self.balance:.2f}")
    print("-" * 50)
    self.transaction_history.append(
        f"Checked balance: ${self.balance:.2f} at"
        f" {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

  def deposit(self):
    print("\n" + "-" * 50)
    try:
      amount = float(input("Enter amount to deposit ($): "))
      if amount > 0:
        self.balance += amount
        print(f"\033[92m[+] Successfully deposited: ${amount:.2f}\033[0m")
        print(f"Updated Balance: ${self.balance:.2f}")
        self.transaction_history.append(
            f"Deposited: ${amount:.2f} at"
            f" {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
      else:
        print("\033[91m[-] Deposit amount must be greater than zero.\033[0m")
    except ValueError:
        print("\033[91m[-] Invalid input. Please enter a numerical value.\033[0m")
    print("-" * 50)

  def withdraw(self):
    print("\n" + "-" * 50)
    try:
      amount = float(input("Enter amount to withdraw ($): "))
      if amount > 0:
        if amount <= self.balance:
          self.balance -= amount
          print(f"\033[92m[+] Successfully withdrew: ${amount:.2f}\033[0m")
          print(f"Remaining Balance: ${self.balance:.2f}")
          self.transaction_history.append(
              f"Withdrew: ${amount:.2f} at"
              f" {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
          )
        else:
          print("\033[91m[-] Insufficient funds in your account!\033[0m")
      else:
        print("\033[91m[-] Withdrawal amount must be greater than zero.\033[0m")
    except ValueError:
        print("\033[91m[-] Invalid input. Please enter a numerical value.\033[0m")
    print("-" * 50)

  def show_history(self):
    print("\n" + "=" * 50)
    print("             TRANSACTION HISTORY")
    print("=" * 50)
    if not self.transaction_history:
      print("  (No transactions recorded yet!)")
    else:
      for idx, record in enumerate(self.transaction_history, 1):
        print(f"  {idx}. {record}")
    print("=" * 50)


def main():
  # Initializing account with Holder Name: "Muhammad Ali", PIN: "1234", Balance: $1500.00
  my_atm = ATMSystem(
      account_holder="Muhammad Ali Hassan", pin="1234", initial_balance=1500.00
  )

  if not my_atm.authenticate():
    return

  while True:
    print("\n" + "=" * 50)
    print("             ATM MAIN MENU")
    print("=" * 50)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit & Lock Session")
    print("=" * 50)

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
      my_atm.check_balance()
    elif choice == "2":
      my_atm.deposit()
    elif choice == "3":
      my_atm.withdraw()
    elif choice == "4":
      my_atm.show_history()
    elif choice == "5":
      print(
          "\n\033[92mThank you for using the ATM System. Have a great day!\033[0m\n"
      )
      break
    else:
      print("\n\033[91m[-] Invalid choice. Please select between 1 and 5.\033[0m")


if __name__ == "__main__":
  main()