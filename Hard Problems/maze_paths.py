# Finding total number of paths, maze moves from (0.0) to (n,m)

class Recursion:

    def paths(self, i, j, n, m):
        if (i == n-1 and j == m-1):
            return 1
        if (i == n or j == m):
            return 0
        # move downwards
        downwards = self.paths(i+1, j, n, m)

        # move right
        right = self.paths(i, j+1, n, m)
        return downwards + right

if __name__ == '__main__':
    n = int(input('Enter rows: '))
    m = int(input('Enter columns: '))
    run = Recursion()
    totalpaths = run.paths(0, 0, n, m)
    print(totalpaths)