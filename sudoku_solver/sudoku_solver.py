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


def solve_next_place(empty_places, table):
    if not empty_places:
        print_table(table)
        return True

    x = empty_places[0][0]
    y = empty_places[0][1]
    valid_numbers = find_valid_numbers(x, y, table)

    if not valid_numbers:
        table[x][y] = 0
        return False
        
    for number in valid_numbers:
        table[x][y] = number

        if solve_next_place(empty_places[1:], table):
            return True

        table[x][y] = 0


def solve(table):
    empty_places = find_empty_places(table)
    return solve_next_place(empty_places, table)


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


def find_empty_places(table):
    empty_places = []
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                empty_places.append((i, j))
    
    return empty_places


def main():
    start_time = time.time()
    if solve(tables[0]):
        print("Solved.")
    else:
        print("Cannot be solved")
    end_time = time.time()
    print(f"Running finished in {end_time - start_time} seconds.")


if __name__ == "__main__":
    main()