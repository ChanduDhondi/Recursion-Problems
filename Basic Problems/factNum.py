# Factorial of Number using Recursion

class Recursion:

    def factorail(self, number):
        if number == 1:
            return 1
        return number * self.factorail(number-1)
           
        
if __name__ == '__main__':
    number = int(input('Enter Number :'))
    a = Recursion()
    fact = a.factorail(number)
    print(f'Factorial of {number} is : {fact}')