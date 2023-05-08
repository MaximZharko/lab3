word = ""
word_next = input()

while word_next != "stop":
    word += word_next
    word_next = input()

print(word)
