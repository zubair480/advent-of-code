limits = {"red": 12, "green": 13, "blue": 14}


def parse_line(line):
    chunk = line.strip().split(":") # it breaks the line in two chunks divided by : (Game id : and other part)
    id = int(chunk[0].split(" ")[-1]) # It helps us to get the id 
    cube_sets = chunk[1].split(";") # it gives us all the played games

    for set in cube_sets:
        color_sets = set.split(",") # we split all the colors played
        for color_set in color_sets:
            num_color_cube = color_set.strip().split(" ") # we split number with it's color cube
            num = int(num_color_cube[0]) # get the number in a separate variable
            color = num_color_cube[1] # get the color in a seprate
            if num > limits[color]: # check them both with our limits
                id = 0 # if limit excedes we set the id to zero
    return id



with open("C:/Users/zubai/Desktop/advent-of-code/2023/Day 2/input.txt") as input:
    sum = 0
    for line in input:
        sum += parse_line(line) #add the values that are possible
    print(f"sum {sum}")



# The sum is: 2265