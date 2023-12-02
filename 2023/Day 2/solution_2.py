def parse_line(line):
    chunk = line.strip().split(":") # we split the input in two parts (game id: and played games)
    cube_sets = chunk[1].split(";") # we separate all the played games
    

    rgb = {"red": 0, "green": 0, "blue": 0} # this is the minimum number
    for set in cube_sets:
        color_sets = set.split(",") # we split all the cubes with values
        for color_set in color_sets:
            num_color_cube = color_set.strip().split(" ") # now we have the cube number and color
            num = int(num_color_cube[0]) # number stored in num variable
            color = num_color_cube[1] # color in a separate variable
            if num > rgb[color]: # if num greater than our minimum
                rgb[color] = num # we set the color in array rbg to minimum

    minimum_cube_product = 1
    # Iterate through the minimum cube values for each color stored in min_cubes dictionary
    for value in rgb.values():
        minimum_cube_product = minimum_cube_product * value # Multiply the current value with the product
    return minimum_cube_product



with open("C:/Users/zubai/Desktop/advent-of-code/2023/Day 2/input.txt") as input:
    sum = 0
    for line in input:
        sum += parse_line(line)
    print(f"The sum is: {sum}")




# The sum is: 70265