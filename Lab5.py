string = []
string2 = []

print("Введите слова через enter. Чтобы завершить, напишите !")
while (True):
    word = input("Слово: ")
    if (word[-1]) == '!':
        break
    else:
        string.append(word)
string_set = set(string)
print("Множество: ", string_set)
words = len(str(string).split())
print("В множестве", words, "слов.")
length = str(string)
print("Длина строки =", len(length) - (int(words) * 4))
print("Введите новое множество с тем же количеством слов")
for i in range(len(string)):
    word2 = input("Слово " + str(i + 1) + ": ")
    string2.append(word2)
d = {}
d = {string[i]: string2[i] for i in range(words)}
print("Словарь:")
print(d)
