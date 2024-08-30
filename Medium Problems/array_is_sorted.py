# Checking if an array is sorted i.e. strictly increasing

class Recursion:

    def sorted(self, arr, idx):
        if idx == len(arr):
            return True
        if arr[idx-1] < arr[idx] :
            return self.sorted(arr, idx+1)
        else:
            return False

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    run = Recursion()
    print(run.sorted(arr, 1))
    