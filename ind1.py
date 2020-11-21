s = list(input('Напечатайте предложение: ').split())
c = input('Какой символ проверить на вхождение: ')
for i in range(len(s)):
    if c in s[i]:
        print(s[i])
