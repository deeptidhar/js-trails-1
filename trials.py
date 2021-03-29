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

    string = "".join(chars)#[a,e,i]convert into string  

    print(string)
   


def snake_to_camel(string):
    case=[]
    # for word in string.split('_'):
    #     w = word[0].upper()
    #     x = slice(1)
    #     case.append(w[x])
    # snake = "".join(case)

    # print(snake)

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)
        


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    result=[]
    for char in string:
        if len(result) == 0 or char!= result[len(result)-1]: 
            result.append(char)
    

    print(''.join(result))
           


def has_balanced_parens(string):
    parens = 0
    
    for char in string:
        if char == '(':
            parens+=1
        elif char == ')':
            parens-=1
            if parens < 0:
                return false

    return parens == 0

def compress(string):
    compressed = []
    currChar = ''
    charCount = 0

    for char in string:
        if char != currChar:
            compressed.append(currChar)

            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0

        charCount += 1

    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))

    return ''.join(compressed
    
