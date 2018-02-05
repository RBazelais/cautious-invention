# shift array values
def shift_left(arr):
    for idx in range(0, len(arr)-1):
        arr[idx] = arr[idx] -1
    arr[len(arr)-1] = 0
    print arr

x = [12, 13, 42, 95]
shift_left(x)
# first value should disappear
# then add 0 to the end of arr