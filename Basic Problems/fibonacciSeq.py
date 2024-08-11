# Fibonacci Sequence upto given number

class Recursion:

    def fibonacciSeq(self, zero, one, number):
        if number == 0:
            return
        self.sum = zero + one
        print(self.sum)
        self.fibonacciSeq(one, self.sum, number-1)

if __name__ == '__main__':
    number = int(input("Enter Number : "))
    print(0)
    print(1)
    a = Recursion()
    a.fibonacciSeq(0, 1, number-2)