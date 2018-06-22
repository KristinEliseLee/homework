english_to_lolcat = {
    "cheese": "cheez", "hello": "oh hai", "like": "liek", "you": "u", "have":
    "has", "kitty": "kitteh", "my": "mah", "some": "sum", "would": "wud",
    "are": "r", "the": "teh"
}


def translate(word):
    if word in english_to_lolcat:
        return english_to_lolcat[word]
    else:
        return "Oh no! that word does not exist in lolcat speak!"


hello = translate("hello")
print(hello)

potato = translate("potato")
print(potato)
