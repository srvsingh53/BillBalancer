def input_names(name, n):
    for i in range(n):
        print("Enter the name: ", end="")
        d = input() # string
        name[d] = i # string to
        print()

def find_label(name, n, d):
    return name[d]

def find_name(m, n, value):
    for key, val in m.items():
        if val == value:
            return key

def main():
    n = int(input("Enter the number of persons: "))
    name = {}
    input_names(name, n)# input is a pair of name and its label in adj matrix
    arr = [[0 for _ in range(n)] for _ in range(n)]

    while True:
        m = int(input("What's the expense? : "))
        p = input("WHO PAID IT? : ")
        x = find_label(name, n, p)
        expense = m // n

        for i in range(n):
            if i == x:
                arr[x][x] = 0
            else:
                arr[x][i] += expense

        test = int(input("Press -1 to stop OR press any number to continue: "))
        if test == -1:
            break

    print("\n")
    for row in arr:
        print(" ".join(map(str, row)))

    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")

    for i in range(n - 1):
        x = i
        for j in range(i + 1, n):
            y = j
            v1 = arr[x][y]
            v2 = arr[y][x]
            diff = v1 - v2
            name_x = find_name(name, n, x)
            name_y = find_name(name, n, y)
            if diff == 0:
                print(name_x, name_y, "no payment")
            elif diff < 0:
                print(name_x, "needs to pay", name_y, abs(diff))
            else:
                print(name_y, "needs to pay", name_x, abs(diff))

if __name__ == "__main__":
    main()