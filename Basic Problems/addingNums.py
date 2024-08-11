# Adding Numbers upto given Number using Recursion

class Recursion:

    def addingNums(self, number, sum):
        if number == 0:
            print(sum)
            return
        sum += number
        self.addingNums(number-1, sum)
        
if __name__ == '__main__':
    number = int(input('Enter Number :'))
    a = Recursion()
    print(f'Adding upto {number}')
    sum = a.addingNums(number, 0)