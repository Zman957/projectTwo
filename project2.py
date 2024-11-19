class Beverage:
    """Represents a beverage in the vending machine."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    """Represents the vending machine with beverages and functionality."""
    def __init__(self):
        self.beverages = {
            1: Beverage("Cola", 1.50),
            2: Beverage("Water", 1.00),
            3: Beverage("Orange Juice", 1.75),
            4: Beverage("Lemonade", 1.25),
            5: Beverage("Coffee", 2.00),
            6: Beverage("Tea", 1.50)
        }

    def display_menu(self):
        """Displays the beverage menu."""
        print("\nWelcome to the Vending Machine!")
        print("Here are the available beverages:")
        for key, beverage in self.beverages.items():
            print(f"{key}: {beverage.name} - ${beverage.price:.2f}")

    def vend_beverage(self):
        """Handles the vending process."""
        while True:
            self.display_menu()


            try:
                choice = int(input("Please select a beverage by entering the number: "))
                if choice not in self.beverages:
                    print("Invalid selection. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            selected_beverage = self.beverages[choice]
            print(f"You selected {selected_beverage.name}. Price: ${selected_beverage.price:.2f}")


            try:
                money = float(input("Please insert money: $"))
            except ValueError:
                print("Invalid input. Please insert valid money.")
                continue


            if money >= selected_beverage.price:
                change = money - selected_beverage.price
                print(f"Vending {selected_beverage.name}... Enjoy!")
                if change > 0:
                    print(f"Your change is: ${change:.2f}")
            else:
                print(f"Insufficient funds. Please insert at least ${selected_beverage.price:.2f}.")
                continue


            cont = input("Would you like another beverage? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Thank you for using the vending machine!")
                break


vending_machine = VendingMachine()
vending_machine.vend_beverage()