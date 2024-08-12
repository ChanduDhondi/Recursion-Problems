# Printing given string in Reverse order

class Recursion:

    def stringReverse(self, str, newstr, idx):
        if len(str)+1 == idx:
            return print(newstr)
        newstr += str[-idx]
        self.stringReverse(str, newstr, idx+1)

if __name__ == '__main__':
    str = input('Enter any string : ')
    run = Recursion()
    reverseString = run.stringReverse(str, '', 1)