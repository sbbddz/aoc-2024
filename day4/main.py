file = open("input.txt", "r")
input = file.read().split("\n")
input.pop()

grid = []
for line in input:
    grid.append(list(line))

count_p1 = 0
count_p2 = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        # Horizontal founds
        if x+4 <= len(grid[y]):
            possible_xmas = "".join(grid[y][x:x+4])
            possible_rev_xmas = possible_xmas[::-1]
            if possible_xmas == "XMAS" or possible_rev_xmas == "XMAS":
                count_p1 += 1
        # Vertical founds
        if y+4 <= len(grid):
            possible_xmas_arr = []
            for i in range(y, y+4):
                possible_xmas_arr.append(grid[i][x])
            possible_xmas = "".join(possible_xmas_arr)
            possible_rev_xmas = possible_xmas[::-1]
            if possible_xmas == "XMAS" or possible_rev_xmas == "XMAS":
                count_p1 += 1

        # Horizontal founds
        if x+4 <= len(grid[y]) and y+4 <= len(grid):
            possible_xmas_arr = []
            for i in range(0, 4):
                possible_xmas_arr.append(grid[y+i][x+i])
            possible_xmas = "".join(possible_xmas_arr)
            possible_rev_xmas = possible_xmas[::-1]
            if possible_xmas == "XMAS" or possible_rev_xmas == "XMAS":
                count_p1 += 1

        # rev Horizontal founds
        if x-3 >= 0 and y+4 <= len(grid):
            possible_xmas_arr = []
            for i in range(0, 4):
                possible_xmas_arr.append(grid[y+i][x-i])
            possible_xmas = "".join(possible_xmas_arr)
            possible_rev_xmas = possible_xmas[::-1]
            if possible_xmas == "XMAS" or possible_rev_xmas == "XMAS":
                count_p1 += 1

        # X-MAS
        if x+1 < len(grid[y]) and y+1 < len(grid) and x-1 >= 0 and y-1 >= 0:
            diag_one = [grid[y-1][x-1], grid[y][x], grid[y+1][x+1]]
            diag_two = [grid[y-1][x+1], grid[y][x], grid[y+1][x-1]]
            one = False
            two = False
            possible_x_mas_one = "".join(diag_one)
            possible_x_mas_rev_one = possible_x_mas_one[::-1]
            if possible_x_mas_one == "MAS" or possible_x_mas_rev_one == "MAS":
                one = True
            possible_x_mas_two = "".join(diag_two)
            possible_x_mas_rev_two = possible_x_mas_two[::-1]
            if possible_x_mas_two == "MAS" or possible_x_mas_rev_two == "MAS":
                two = True

            if one and two:
                count_p2 += 1


print(count_p1)
print(count_p2)
