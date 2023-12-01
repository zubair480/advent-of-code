# We need to add numbers 
# First and last integer must be added
# If there is only 1 integer we will add it twice
    
def run_part1(): 
    with open("input_1.txt", "r") as file:
        lines = file.readlines() # read lines
        total_sum = 0 
        for line in lines:
            digits = [int(char) for char in line if char.isdigit()] # just find digits from a single line and (if char.digit)
            number = int(f"{digits[0]}{digits[-1]}") # we will add first and last digit and it will add the first two 
            total_sum += number 

    return total_sum


# 2dfd3
print(run_part1())