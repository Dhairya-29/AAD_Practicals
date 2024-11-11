def fn():
    a = []
    b = []
    count1 = 0
    count2 = 0

    for i in range(0, 3): # type: ignore
        a.append(input("Enter marks for chef 1: "))
    
    for i in range(0, 3):
        b.append(input("Enter marks for chef 2: "))

# to check 

    for i in range(0, 3):
        if a[i] > b[i]:
            count1 += 1
        elif a[i] < b[i]:
            count2 += 1
        else:
            continue

    c = [count1, count2]
    print(c)

if __name__ == "__main__":
    fn()