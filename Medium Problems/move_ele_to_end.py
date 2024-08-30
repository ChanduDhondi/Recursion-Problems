# Moving all x to the end of the string

class Recursion:

    count = 0
    def move_ele(self, str, ele, idx, newstr) -> None:
        if idx == len(str):
            print(f'{newstr}'+f'{ele*self.count}')
            return
        if str[idx] == ele:
            self.count += 1
            self.move_ele(str, ele, idx+1, newstr)
        else:
            newstr += str[idx]
            self.move_ele(str, ele, idx+1, newstr)

if __name__ == '__main__':
    string = input('Enter any string : ')
    ele = input('Enter an element you want to move to last : ')
    run = Recursion()
    if ele in string:
        run.move_ele(string, ele, 0, '')
    else:
        print('Element is not in the string')