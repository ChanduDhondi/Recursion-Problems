# Calculating x^n using Recursion

class Recursion:

    # storing previous value in power variable
    def logic1(self, number, power):
        if number == 0:
            return 0
        elif power == 0:
            return 1
        power = self.logic1(number, power-1)
        self.value = number * power
        return self.value
            
    # storing in seperate variable 
    def logic2(self, number, power, value):
        if number == 0:
            return 0
        elif power == 0:
            return print(value)
        value = value*number
        self.logic2(number, power-1, value)

    # Optimizing stack height to logn
    def optimizeSol(self, number, power):
        if number == 0:
            return 0
        elif power == 0:
            return 1
        # Odd power
        if power % 2 == 0:
            return self.optimizeSol(number, power/2)*self.optimizeSol(number, power/2)
        else:
            return self.optimizeSol(number, power//2)*self.optimizeSol(number, power//2)*number



if __name__ == '__main__':
    number = int(input('Enter Number :'))
    power = int(input('Enter power : '))
    a = Recursion()
    print(a.logic1(number, power))
    a.logic2
    print(a.optimizeSol(number, power))
