# Pringint all the permulations of the given string

class Recursion:

    def all_permutations(self, string, output):
        if len(string) == 0:
            print(output)
            return
        
        for i in range(len(string)):
            currChar = string[i]
            newString = string[:i] + string[i+1:]
            self.all_permutations(newString, output+currChar)

if __name__ == '__main__':
    string = input('Enter String: ')
    run = Recursion()
    run.all_permutations(string, '')