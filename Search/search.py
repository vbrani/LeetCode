def func():
    arr = [1,3,5,6]
    x = (len(arr))
    target = 6
    if target > arr[x-1] :
        print(x)
    for i in range(x):
        if arr[i] == target:
            print(i)
func()