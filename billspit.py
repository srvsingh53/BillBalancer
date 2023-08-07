def input_names(name, n):
    for i in range(n):
        print("Enter the name: ", end="")
        d = input() # string
        name[d] = i # assign a label to the name in the dictionary
        print()

def find_label(name, n, d):
    return name[d] # returns the label associated with the name

def find_name(m, n, value):
    for key, val in m.items():
        if val == value:
            return key # finds the name associated with a label

def main():
    n = int(input("Enter the number of persons: "))
    name = {} # dictionary to store names and their labels
    input_names(name, n) # input names and assign labels

    # Create an empty 2D list (matrix) to track expenses between individuals
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # Loop to input expenses and update the expense matrix
    while True:
        m = int(input("What's the expense? : "))
        p = input("WHO PAID IT? : ")
        x = find_label(name, n, p) # find the label for the person who paid
        expense = m // n # calculate the equal expense per person

        for i in range(n):
            if i == x:
                arr[x][x] = 0
            else:
                arr[x][i] += expense # update the expense matrix

        test = int(input("Press -1 to stop OR press any number to continue: "))
        if test == -1:
            break

    # Print the expense matrix
    print("\n")
    for row in arr:
        print(" ".join(map(str, row)))

    # Calculate and print who owes whom
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
