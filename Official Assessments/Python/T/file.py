def add(numbers):
    return sum(numbers)

def countVowels(word: str) -> int:
    return len(list(filter(lambda n: n in "aeiou", word)))


tpls = {'a': 3} , {'c': 1}, {'b': 2}

str = "9106236034082"

result = sorted(tpls, key= lambda n: list(n.items())[0][0], reverse=False)

print(result)
lst = ['dog', 'cat', 'house']
dictionary = {word: len(word) for word in lst}
print(dictionary)

