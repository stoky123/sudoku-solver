import time

start = time.time()

table = [
    [0, 0, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 3],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 3, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 5],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 0]
]

# table = [
#     [0, 3, 0, 0, 1, 0, 0, 6, 0],
#     [7, 5, 0, 0, 3, 0, 0, 4, 8],
#     [0, 0, 6, 9, 8, 4, 3, 0, 0],
#     [0, 0, 3, 0, 0, 0, 8, 0, 0],
#     [9, 1, 2, 0, 0, 0, 6, 7, 4],
#     [0, 0, 4, 0, 0, 0, 5, 0, 0],
#     [0, 0, 1, 6, 7, 5, 2, 0, 0],
#     [6, 8, 0, 0, 9, 0, 0, 1, 5],
#     [0, 9, 0, 0, 4, 0, 0, 3, 0]
# ]

def solve(x, y):
    if table[x][y] == 0:
        valid_numbers = find_valid_numbers(x, y)
        if len(valid_numbers) == 0:
            table[x][y] = 0
            return
        for number in valid_numbers:
            table[x][y] = number
            if x == y == 8:
                for row in table:
                    print(row)
                print(time.time() - start)
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

                solve(i, j)

            table[x][y] = 0

def find_valid_numbers(x, y):
    valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if table[i][y] != 0:
            try:
                valid_numbers.remove(table[i][y])
            except ValueError:
                pass

    for i in range(9):
        if table[x][i] != 0:
            try:
                valid_numbers.remove(table[x][i])
            except ValueError:
                pass
    
    x_block = x // 3 * 3
    y_block = y // 3 * 3
    
    for i in range(x_block, x_block + 3):
        for j in range(y_block, y_block + 3):
            if table[i][j] != 0:
                try:
                    valid_numbers.remove(table[i][j])
                except ValueError:
                    pass

    return valid_numbers

def main():
    solve(0, 0)

if __name__ == "__main__":
    main()
    print(time.time() - start)