def minion_game(string):
    # your code goes here

    """
    import re
    c = re.compile(r'[^AEIOU]')

    kevin_words = []
    stuart_words = []

    for i in range(len(string)):
        if c.search(string[i]) == None:
           for j in range(i+1, len(string)+1):
               kevin_words.append(string[i:j])
        else:
            for j in range(i+1, len(string)+1):
                stuart_words.append(string[i:j])

    if len(kevin_words)>len(stuart_words):
        result = f"Kevin {len(kevin_words)}"
    elif len(kevin_words)<len(stuart_words):
        result = f"Stuart {len(stuart_words)}"
    else:
        print('Draw')



    if len(kevin_words)>len(stuart_words):
        print("Kevin "+ str(len(kevin_words)))
    elif len(kevin_words)<len(stuart_words):
        print("Stuart "+ str(len(stuart_words)))
    else:
        print('Draw')

    print(kevin_words)
    print(stuart_words)

    """

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)
