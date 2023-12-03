import re

# Read the grid from the input file
grid = open('./input.txt').read().splitlines()

# Read the engine schematic grid from the input file
# Define a function to get valid neighbors for a given cell in the grid
# Initialize variables to track the sum of part numbers and gears with associated numbers
# Iterate through each line of the grid
    # Find matches of numbers in the line
    # For each match, extract the number and initialize flags
    # Iterate through characters in the match range
        # Check valid neighbors of the current cell
        
        # If the character is not a digit or period, set flags accordingly
        # If the character is a gear symbol and not already a gear, update gears dictionary
    # If the match represents a part number, add it to the sum
# Calculate the product of part numbers for gears with exactly two numbers


def get_valid_neighbors(x, y):
    valid_neighbors = []
    # defining the relative coordinates of neighboring cells
    relative_neighbor_coordinates = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for relative_x, relative_y in relative_neighbor_coordinates:
        neighbor_x, neighbor_y = x + relative_x, y + relative_y
        # Check if the neighbor is within the grid boundaries
        if (0 <= neighbor_x < len(grid[0])) and (0 <= neighbor_y < len(grid)):
            valid_neighbors.append((neighbor_x, neighbor_y))
    return valid_neighbors

# Initialize variables
sum_of_part_numbers, gears_dict = 0, {}

# Iterate through each line of the grid
for current_y, line_content in enumerate(grid):
    for match_obj in re.finditer(r'(\d+)', line_content):
        # Extract the number from the match
        current_number, is_part_number, is_gear = int(match_obj.group()), False, False
        # Iterate through the characters in the match range
        for current_x in range(match_obj.start(), match_obj.end()):
            # Check neighbors of the current cell
            for neighbor_x, neighbor_y in get_valid_neighbors(current_x, current_y):
                current_char = grid[neighbor_y][neighbor_x]
                # Skip digits and periods
                if current_char.isdigit() or current_char == '.':
                    continue
                is_part_number = True
                # Check if the character is a gear symbol
                if current_char == '*' and not is_gear:
                    # Update gears dictionary
                    if (neighbor_x, neighbor_y) not in gears_dict:
                        gears_dict[neighbor_x, neighbor_y] = [current_number]
                    else:
                        gears_dict[neighbor_x, neighbor_y].append(current_number)
                    is_gear = True
        # If the current match represents a part number, add it to the sum
        if is_part_number:
            sum_of_part_numbers += current_number

# Calculate the product of part numbers for gears with exactly two numbers
product_of_part_numbers = 0
for gear_numbers in gears_dict.values():
    if len(gear_numbers) == 2:
        product_of_part_numbers += gear_numbers[0] * gear_numbers[1]


print(sum_of_part_numbers)  
print(product_of_part_numbers)  
