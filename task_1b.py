import random
import string
# considering the letters to be the runes

def earliest (word='LUMOS'):
    letters = list(string.ascii_letters)
    runes = random.sample(letters, 52)

    print('Runes available: ',runes)

    target = set(word)      # collects all the letters of LUMOS as a set
    collect = set()

    for i,r in enumerate (runes, 1):
        if r in target:
            collect.update(r)
            if collect == target:
                return i
    return -1

result = earliest("LUMOS")
print("Earliest step Hermione can cast LUMOS:", result)