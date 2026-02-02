print("General tuples\n~~~~")
dictionary = {"cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print("~~~~\nTuples keys() function and sorted\n~~~~")

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])


print("~~~~\nTuples items() and values() methods\n~~~~")

for english, french in dictionary.items():
    print(english, "->", french)

print("~~~~\nModifying tuples\n~~~~")

dictionary['cat'] = 'minou'
print(dictionary)

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"duck": "canard"})
print(dictionary)

del dictionary['dog']
print(dictionary)

dictionary.popitem()
print(dictionary)