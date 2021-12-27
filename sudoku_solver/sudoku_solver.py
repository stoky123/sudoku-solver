import time

tables = [
    [
        [0, 0, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 2, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 7, 5],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 6, 0, 0]
    ],
    [
        [0, 3, 0, 0, 1, 0, 0, 6, 0],
        [7, 5, 0, 0, 3, 0, 0, 4, 8],
        [0, 0, 6, 9, 8, 4, 3, 0, 0],
        [0, 0, 3, 0, 0, 0, 8, 0, 0],
        [9, 1, 2, 0, 0, 0, 6, 7, 4],
        [0, 0, 4, 0, 0, 0, 5, 0, 0],
        [0, 0, 1, 6, 7, 5, 2, 0, 0],
        [6, 8, 0, 0, 9, 0, 0, 1, 5],
        [0, 9, 0, 0, 4, 0, 0, 3, 0]
    ]
]

def print_table(table):
    print("-" * 38)
    for i in range(3):
        for j in range(3):
            print(" | {}  {}  {}  |  {}  {}  {}  |  {}  {}  {}  | ".format(*table[i*3+j]))
        print("-" * 38)


def solve(x, y, table):
    if table[x][y] == 0:
        valid_numbers = find_valid_numbers(x, y, table)
        if not valid_numbers:
            table[x][y] = 0
            return
        for number in valid_numbers:
            table[x][y] = number
            if x == y == 8:
                print_table(table)
                exit()
            else:
                i = x
                j = y
                while table[i][j] != 0:
                    if i == 8:
                        j = j + 1
                        i = 0
                    else:
                        i = i + 1

                solve(i, j, table)

            table[x][y] = 0

def find_valid_numbers(x, y, table):
    valid_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for i in range(9):
        valid_numbers.discard(table[i][y])
        valid_numbers.discard(table[x][i])
    
    x_block = x // 3 * 3
    y_block = y // 3 * 3
    
    for i in range(x_block, x_block + 3):
        for j in range(y_block, y_block + 3):
            valid_numbers.discard(table[i][j])

    return valid_numbers

def main():
    solve(0, 0, tables[0])

if __name__ == "__main__":
    main()