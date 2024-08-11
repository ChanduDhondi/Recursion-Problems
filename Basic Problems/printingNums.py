# Printing Numbers using Recursion

class Recursion:

    def reverse(self, number):
        if number == 0:
            return print(number)
        print(number)
        self.reverse(number-1)

    def forward(self, number):
        if number == 0:
            return print(number)
        self.forward(number-1)
        print(number)

if __name__ == '__main__':
    number = int(input('Enter Number :'))
    a = Recursion()
    print(f'Printing from {number} to 0')
    a.reverse(number)
    print(f'Printing from 0 to {number}')
    a.forward(number)

