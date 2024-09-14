
def rem(l, word):
    n = []
    for item in 1:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Zakir", "Harry", "shubham", "an"]
 
print(rem(l, "an"))
