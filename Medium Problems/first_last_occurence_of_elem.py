# Printing first and last occurence of given element

class Recursion:

    first = 0
    last = 0
    def firstLastOccurence(self, str, ele, idx):
            if idx == len(str)-1:
                print(f'first occurence- {self.first}, last occurence- {self.last}')
                return
            
            if str[idx] == ele:
                 if self.first == 0:
                    self.first = idx 
                 else:
                    self.last = idx

            self.firstLastOccurence(str, ele, idx+1)
                 

if __name__ == '__main__':
    str = input('Enter any string : ')
    ele = input('Enter element in the string : ')
    run = Recursion()
    if ele in str:
        run.firstLastOccurence(str, ele, 0)
    else:
         print('Element you entered is not in the string')