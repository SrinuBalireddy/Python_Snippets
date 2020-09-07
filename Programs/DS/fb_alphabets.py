# Write your code here :-)


# create two lists , one for alphabets and other for corresponding numbers
alphabets  = []
alpha_nums = [n for n in range(1,27)]

for i in range(26):
    alphabets.append(chr(97+i))

#print(list(zip(alphabets, alpha_nums)))

# function to calculate the numbers of options to create the given string
def possibilities(input_str):

    counter = 0

    # TODO: if input_str first index is 0:
    if input_str[0] == '0':
        return 'Invalid options'

    # TODO: edge cases where string is null or of length one
    if len(input_str) == 0:
        return 'No string provided'
    elif len(input_str) == 1:
        return 1

    # TODO: input_str length 2 or more
    elif len(input_str) == 2:
        # possibilities are 1 or more
        # traverse thru the input_str
        for i in input_str:
            # check if it is available in integers list
            if int(i) in alpha_nums:
                counter+=1
        if counter == len(input_str):
            counter == 1

        if input_str in alpha_nums:
            counter+=1

    else:

        for i in range(len(input_str)):
            if i+1 < len(input_str):
                if (input_str[i:i+1] in alpha_nums):
                and
                    counter


    return counter

        # if the whole input_str is available in the in integers list
            # fetch the index and find the alphabets list for the same index

print(possibilities('3'))
