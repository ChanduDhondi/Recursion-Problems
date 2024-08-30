# remove duplicates from string

class Recursion:

    def remove_duplicates(self, str, newstr, idx) -> None:
        if idx == len(str):
            return print(newstr)
        if str[idx] in newstr:
            self.remove_duplicates(str, newstr, idx+1)
        else:
            newstr += str[idx]
            self.remove_duplicates(str, newstr, idx+1)

if __name__ == '__main__':
    string = input('Enter string : ')
    run = Recursion()
    run.remove_duplicates(string, '', 0)