def menu():
    print("1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrix\n"
          "5. Calculate determinant\n"
          "6. Inverse matrix\n"
          "0. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        add_matrices()
        menu()
    elif choice == 2:
        m_const()
        menu()
    elif choice == 3:
        m_matrices()
        menu()
    elif choice == 4:
        transpose()
    elif choice == 5:
        determinant()
        menu()
    elif choice == 6:
        inverse()
    elif choice == 0:
        exit_program()


def exit_program():
    pass


def print_res(matrix):
    print("The result is: ")
    for row in matrix:
        print(*row, end=" \n")


def enter_m():
    size = input("Enter size of matrix: ").split()
    row = int(size[0])
    print("Enter matrix: ")
    a = [input().split() for i in range(row)]
    return a


def add_matrices():
    # Enter matrix A
    digits_a = input("Enter size of first matrix: ").split()
    row_a = int(digits_a[0])
    column_a = int(digits_a[1])
    print("Enter first matrix: ")
    a = [input().split() for i in range(row_a)]
    a = [[a[i][j] for j in range(column_a)] for i in range(row_a)]

    # Enter matrix B
    digits_b = input("Enter size of second matrix: ").split()
    row_b = int(digits_b[0])
    column_b = int(digits_b[1])
    print("Enter second matrix: ")
    b = [input().split() for i in range(row_b)]
    b = [[b[i][j] for j in range(column_b)] for i in range(row_b)]

    # Check matrices for added
    if row_a == row_b and column_a == column_b:
        c = [[float(a[i][j]) + float(b[i][j]) for j in range(column_a)] for i in range(row_a)]
        print_res(c)
        print()
    else:
        print("The operation cannot be performed.")


def m_const():
    # Enter matrix
    a = enter_m()
    const = int(input("Enter constant: "))
    a = [[int(a[i][j]) * const for j in range(len(a[0]))] for i in range(len(a))]
    print_res(a)


def m_matrices():
    # Enter matrix A
    size_a = input("Enter size of first matrix: ").split()
    row_a = int(size_a[0])
    column_a = int(size_a[1])
    print("Enter first matrix: ")
    a = [input().split() for i in range(row_a)]
    a = [[a[i][j] for j in range(column_a)] for i in range(row_a)]

    # Enter matrix B
    size_b = input("Enter size if second matrix: ").split()
    row_b = int(size_b[0])
    column_b = int(size_b[1])
    print("Enter second matrix: ")
    b = [input().split() for i in range(row_b)]
    b = [[b[i][j] for j in range(column_b)] for i in range(row_b)]

    # Check matrices
    if column_a == row_b:
        c = [[0 for j in range(column_b)] for i in range(row_a)]
        for i in range(row_a):
            for j in range(column_b):
                for k in range(column_a):
                    c[i][j] += float(a[i][k]) * float(b[k][j])
        print_res(c)
    else:
        print("The operation cannot be performed.")


def transpose():
    print("1. Main diagonal\n"
          "2. Side diagonal\n"
          "3. Vertical line\n"
          "4. Horizontal line")
    choice = int(input("Your choice: "))
    a = enter_m()
    if choice == 1:
        print_res(t_main(a))
    elif choice == 2:
        t_side(a)
    elif choice == 3:
        t_vert(a)
    elif choice == 4:
        t_hor(a)
    menu()


def t_main(matrix):
    t = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t[i][j] = matrix[j][i]
    return t


def t_side(matrix):
    t = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t[i][j] = matrix[len(matrix[0]) - 1 - j][len(matrix) - 1 - i]
    print_res(t)
    return t


def t_vert(matrix):
    t = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t[i][j] = matrix[i][len(matrix[0]) - 1 - j]
    print_res(t)
    return t


def t_hor(matrix):
    t = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            t[i][j] = matrix[len(matrix) - 1 - i][j]
    print_res(t)
    return t


def determinant():
    a = enter_m()
    if len(a) == 1:
        print(int(a[0][0]))
    else:
        print("The result is:")
        deter = det(a)
        print(deter)
        return deter


def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def det(matrix):
    if len(matrix) == 2:
        return det2(matrix)
    else:
        return sum((-1) ** j * float(matrix[0][j]) * det(minor(matrix, 0, j)) for j in range(len(matrix)))


def det2(matrix):
    return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])


def inverse():
    a = enter_m()
    a_t = t_main(a)
    a_p = [[(-1) ** (i + j) * float(det(minor(a_t, i, j))) for j in range(len(a))] for i in range(len(a))]
    if det(a) == 0:
        print("The operation cannot be performed.")
    else:
        a_inv = [[float(a_p[i][j]) / det(a) for j in range(len(a))] for i in range(len(a))]
        print_res(a_inv)


menu()
