class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550
    state = None
    input1 = None

    def __init__(self):
        self.state = 'WA'

    def start(self):
        while True:
            if self.state == 'WA':
                self.input1 = input('Write action (buy, fill, take, remaining, exit)')

                if self.input1 == 'buy':
                    self.state = 'choosing a coffee'

                elif self.input1 == 'fill':
                    self.state = 'filling'

                elif self.input1 == 'take':
                    self.state = 'take'

                elif self.input1 == 'remaining':
                    self.state = 'remaining'

                elif self.input1 == 'exit':
                    self.state = 'exit'

            elif self.state == 'choosing a coffee':
                self.input1 = input(
                    'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if self.input1 == '1':
                    self.buy_1()

                elif self.input1 == '2':
                    self.buy_2()

                elif self.input1 == '3':
                    self.buy_3()

                elif self.input1 == 'back':
                    self.state = 'WA'

                self.state = 'WA'

            elif self.state == 'filling':
                w = int(input('Write how many ml of water do you want to add:'))
                self.water = self.water + w

                w = int(input('Write how many ml of milk do you want to add:'))
                self.milk = self.milk + w

                w = int(input('Write how many grams of coffee beans do you want to add:'))
                self.coffee = self.coffee + w

                w = int(input('Write how many disposable cups do you want to add:'))
                self.cups = self.cups + w

                # Set state back to 'Write Action'
                self.state = 'WA'

            elif self.state == 'take':
                print(f'I gave you ${self.money}\n')
                self.money = 0
                self.state = 'WA'

            elif self.state == 'remaining':
                self.print_contents()
                self.state = 'WA'

            elif self.state == 'exit':
                break

    def check_resource(self, wa, m, c):
        if wa > self.water:
            return 'water'
        elif m > self.milk:
            return 'milk'
        elif c > self.coffee:
            return 'coffee'
        elif self.cups < 1:
            return 'cups'
        else:
            return 1

    def buy_1(self):
        check = self.check_resource(250, 0, 16)
        if check == 1:
            print('I have enough resources, making you a coffee!')
            self.water = self.water - 250
            self.coffee = self.coffee - 16
            self.money = self.money + 4
            self.cups = self.cups - 1
        else:
            print('Sorry, not enough', check, '!')

    def buy_2(self):
        check = self.check_resource(350, 75, 20)
        if check == 1:
            print('I have enough resources, making you a coffee!')
            self.water = self.water - 350
            self.milk = self.milk - 75
            self.coffee = self.coffee - 20
            self.money = self.money + 7
            self.cups = self.cups - 1
        else:
            print('Sorry, not enough', check, '!')

    def buy_3(self):
        check = self.check_resource(200, 100, 12)
        if check == 1:
            print('I have enough resources, making you a coffee!')
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.coffee = self.coffee - 12
            self.money = self.money + 6
            self.cups = self.cups - 1
        else:
            print('Sorry, not enough', check, '!')

    def print_contents(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(f'${self.money} of money\n')


machine_one = CoffeeMachine()

machine_one.start()









"""



while True:
    n = input('Write action (buy, fill, take, remaining, exit)')

    if n == 'fill':
        w = int(input('Write how many ml of water do you want to add:'))
        water = water + w

        w = int(input('Write how many ml of milk do you want to add:'))
        milk = milk + w

        w = int(input('Write how many grams of coffee beans do you want to add:'))
        coffee = coffee + w

        w = int(input('Write how many disposable cups do you want to add:'))
        cups = cups + w

    elif n == 'take':
        print('I gave you $', money, '\n')
        money = 0

    elif n == 'buy':
        w = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

        if w == '1':
            check = check_resource(250, 0, 16)
            if check == 1:
                print('I have enough resources, making you a coffee!')
                water = water - 250
                coffee = coffee - 16
                money = money + 4
                cups = cups - 1
            else:
                print('Sorry, not enough', check, '!')

        elif w == '2':
            check = check_resource(350, 75, 20)
            if check == 1:
                print('I have enough resources, making you a coffee!')
                water = water - 350
                milk = milk - 75
                coffee = coffee - 20
                money = money + 7
                cups = cups - 1
            else:
                print('Sorry, not enough', check, '!')

        elif w == '3':
            check = check_resource(200, 100, 12)
            if check == 1:
                print('I have enough resources, making you a coffee!')
                water = water - 200
                milk = milk - 100
                coffee = coffee - 12
                money = money + 6
                cups = cups - 1
            else:
                print('Sorry, not enough', check, '!')

        elif w == 'back':
            continue

    elif n == 'remaining':
        print_contents()

    elif n == 'exit':
        break
"""
