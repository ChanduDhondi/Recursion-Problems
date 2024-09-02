# Printing combinations of mobile keypad

class Recursion:

    def keypad_combinations(self, combination, idx, newStr,keypad):
        # base condition
        if idx == len(combination):
            return print(newStr)
        # logic
        currCombi = combination[idx]
        for i in keypad[currCombi]:
            self.keypad_combinations(combination, idx+1, newStr+i, keypad)

if __name__ == '__main__':
    keypad = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs',
              '8':'tuv', '9':'wxyz', '0':''}
    print('Keypad combination mapping is ', keypad)
    combination = input('Enter combination(numbers): ')
    try:
        run = Recursion()
        run.keypad_combinations(combination, 0, '',keypad)
    except ValueError as e:
        print(e)