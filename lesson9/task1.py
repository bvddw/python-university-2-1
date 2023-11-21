def uncommon(s1, s2):
    words = s1.split().extend(s2.split())
    return list(filter(lambda item: words.count(item) == 1, words))

print(uncommon("a b c", "a a d"))