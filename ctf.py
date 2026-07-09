from itertools import permutations

victim = {
    "a": "Aziz",
    "b": "2009",
    "c": "12",
    "d": "06",
}

for i in range(1, 4):
    for j in permutations('abcd', i):
        word = "".join([victim[d] for d in j])
        print(word)
