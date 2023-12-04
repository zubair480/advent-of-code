from collections import defaultdict

def part1():
    with open('./input.txt', 'r') as file:
        cards = file.read().split('\n')
        total = 0
        for card in cards:
            _, numbers = card.split(': ') #we get the numbers and card id
            winning, given = numbers.split(' | ') # we split the numbers
            seen = set(winning.split()) # we winning numbers set in a seen set
            score = 0.5  # as we have to multiply we can't give zero
            for num in given.split():
                if num in seen: # now we are cchecking if we have seen the number
                    score *= 2 # we will increase the score if it is already seen
            if score > 0.5:  # if zero is greater than zero we add it to total
                total += score
    return total

print(part1())


def part2():
    with open('./input.txt', 'r') as file:
        copies = defaultdict(int)
        cards = file.read().split('\n')
        for i, card in enumerate(cards):
            _, numbers = card.split(': ') # again we split the card number
            winning, given = numbers.split(' | ') # then the winning numbers and given numbers
            seen = set(winning.split()) # then we put winning numbers in a set
            matching_nums = 0
            for num in given.split():
                if num in seen:
                    matching_nums += 1  # if the given number is in seen we will increase the matching sum
            copies[i] += 1 # then increase the copies 
            for _ in range(copies[i]): 
                for val in range(1, matching_nums + 1): # we check the values in default dict named matching nums
                    copies[i + val] += 1
    return sum(copies.values()) # we simply sum the values in copies default dic to get our answer

print(part2())