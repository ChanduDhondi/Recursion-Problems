# Tower of Hanoi using Recursion

class Recursion:
    
    def towerOfHanoi(self, number, source, helper, destination):
        if number == 0:
            return 
        self.towerOfHanoi(number-1, source, destination, helper)
        print(f'Disk {number} moving from {source} to {destination}')
        self.towerOfHanoi(number-1, helper, source, destination)        

if __name__ == '__main__':
    number = int(input('Enter number : '))
    a = Recursion()
    source = 'A'
    helper = 'B'
    destination = 'C'
    a.towerOfHanoi(number, source, helper, destination)