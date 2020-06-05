ESPRESSO = {
    "water": 250,
    "milk": 0,
    "coffee_beans": 16,
    "cost": 4,
}

LATTE = {
    "water": 350,
    "milk": 75,
    "coffee_beans": 20,
    "cost": 7,
}

CAPUCCINO = {
    "water": 200,
    "milk": 100,
    "coffee_beans": 12,
    "cost": 6,
}


class CoffeeMachine:
    def __init__(self, water=0, milk=0, coffee_beans=0, cups=0, amount=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.amount = amount
        self.status = None
        self.reset_status()

    def reset_status(self):
        self.status = None
        print('\nWrite action (buy, fill, take, remaining, exit):')

    def check_input(self, user_input):
        if self.status is None:
            return self.choose_program(user_input)
        if self.status == 'buy':
            self.buy_coffee(user_input)
        elif self.status == 'fill':
            self.fill_machine(user_input)
        else:
            print('wrong_status!')
            self.reset_status()
        return True

    def choose_program(self, action):
        if action == 'exit':
            print('Bye!')
            return False
        if action == 'buy':
            self.buy_coffee()
        elif action == 'fill':
            self.fill_machine()
        elif action == 'take':
            self.take_money()
        elif action == 'remaining':
            self.show_resourses()
        else:
            print('Wrong action!')
            self.reset_status()
        return True

    def show_resourses(self):
        print(f'The coffee machine has:\n'
              f'{self.water} of water\n'
              f'{self.milk} of milk\n'
              f'{self.coffee_beans} of coffee beans\n'
              f'{self.cups} of disposable cups\n'
              f'${self.amount} of money')
        self.reset_status()

    def take_money(self):
        print(f'I gave you ${self.amount}')
        self.amount = 0
        self.reset_status()

    def fill_machine(self, user_input=None):
        self.status = 'fill'
        if user_input is None:
            self.fill_step = 'water'
            print('Write how many ml of water do you want to add:')
            return
        try:
            int(user_input)
        except ValueError:
            print('Wrong input!')
            self.reset_status()
            return
        if self.fill_step == 'water':
            self.water += int(user_input)
            self.fill_step = 'milk'
            print('Write how many ml of milk do you want to add:')
        elif self.fill_step == 'milk':
            self.milk += int(user_input)
            self.fill_step = 'coffee_beans'
            print('Write how many grams of coffee beans do you want to add:')
        elif self.fill_step == 'coffee_beans':
            self.coffee_beans += int(user_input)
            self.fill_step = 'cups'
            print('Write how many disposable cups of coffee do you want to add:')
        else:
            self.cups += int(user_input)
            self.reset_status()

    def buy_coffee(self, user_input=None):
        self.status = 'buy'
        if user_input is None:
            print('What do you want to buy?',
                  '1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            return
        if user_input == 'back':
            self.reset_status()
            return
        if user_input == '1':
            self.make_coffee(ESPRESSO)
        elif user_input == '2':
            self.make_coffee(LATTE)
        elif user_input == '3':
            self.make_coffee(CAPUCCINO)
        else:
            print('Wrong choise!')
        self.reset_status()

    def make_coffee(self, type_coffee):
        if self.check_resourses(type_coffee):
            print('I have enough resources, making you a coffee!')
            self.water -= type_coffee["water"]
            self.milk -= type_coffee["milk"]
            self.coffee_beans -= type_coffee["coffee_beans"]
            self.cups -= 1
            self.amount += type_coffee["cost"]

    def check_resourses(self, type_coffee):
        if self.water < type_coffee["water"]:
            print('Sorry, not enough water!')
            return False
        if self.milk < type_coffee["milk"]:
            print('Sorry, not enough milk!')
            return False
        if self.coffee_beans < type_coffee["coffee_beans"]:
            print('Sorry, not enough coffee_beans!')
            return False
        if self.cups < 1:
            print('Sorry, not enough cups!')
            return False
        return True


def main():
    coffee_machine = CoffeeMachine(water=400,
                                   milk=540,
                                   coffee_beans=120,
                                   cups=9,
                                   amount=550,
                                   )
    while True:
        if not coffee_machine.check_input(input()):
            break
    return None


if __name__ == '__main__':
    main()
