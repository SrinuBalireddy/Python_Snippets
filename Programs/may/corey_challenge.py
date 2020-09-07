# Write your code here :-)

class Sentence1:

    def __init__(self, stmt):
        self.stmt = stmt
        self.index = 0
        self.words = self.stmt.split(' ')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        else:
            index = self.index
            self.index+=1
            return self.words[index]


def Sentence(stmt):
    words = stmt.split(' ')
    index = 0
    while index<len(words):
        yield words[index]
        index +=1


my_sentence = Sentence('This is a test')

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
