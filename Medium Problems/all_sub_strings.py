# Printing all sub strings of a given string

class Recursion:

    def allSubStrings(self, str, newstr, idx, container):
        if idx == len(str):
            if newstr in container:
                return
            else:
                print(newstr)
                container.add(newstr)
                return

        # placing element in the new string
        self.allSubStrings(str, newstr+str[idx], idx+1, container)

        # not placing element in the new string
        self.allSubStrings(str, newstr, idx+1, container)

if __name__ == '__main__':
    string = input('Enter String: ')
    run = Recursion()
    container = set()
    run.allSubStrings(string, '', 0, container)