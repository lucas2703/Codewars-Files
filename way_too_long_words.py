for _ in range(int(input())):
    s = input()
    arr = list(s)
    if len(arr) > 10:
        s = arr[0] + str(len(s)-2) + arr[-1]
    print(s)
    