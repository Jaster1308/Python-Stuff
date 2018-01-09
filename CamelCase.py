# sentences = input()
#
# words = sentences.split(' ')
# print(words)
#
# firstWord = words[1]
#
#
# restOfWords = words[1:]
#
#
# for sentences in words:
#     s = ''
#     print (s.join(words))
#
#     for words in s.join(words):
#         str(words)
#         words[1].capitalize()

# tried to use above method but couldn't get it to capitalize words so instead went a different route
# and not use inputs

def snake_to_camel(sentences):
    import re
    return ''.join(x.capitalize() or '_' for x in sentences.split('_'))


print(snake_to_camel('python_exercises'))