"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
        



def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums



def get_odd_indices(items):
    pass  # TODO: replace this line with your code

    result=[]
    for idx in items:
        if idx %2 != 0:
            result.append(items[idx])
            
    return result


def print_as_numbered_list(items):
    i = 1

    for item in range(len(items) - 1):
        print(f"{i}. {items[i]}")

        i += 1


def get_range(start, stop):
    nums = []
    for num in range(stop):
        nums.append(num)

    print(nums)



def censor_vowels(word):
    chars =[]
    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        
        else:
            chars.append(letter)

    string = "".join(chars)

    print(string)
   


def snake_to_camel(string):
    case=[]
    for word in string:
        case.append(word[0].uppercase()[1]

    snake_to = "".join(chars)

    print(snake_to)
        




def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
