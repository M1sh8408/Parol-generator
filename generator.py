import random

simvoli = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']

dlina = int(input('Какую вы хотите длину пароля? (Число) '))

parol = ''

for i in range(dlina):
    parol += random.choice(simvoli)
print(parol)

while True:
    vopros = int(input('Не нравится пароль? Сгенерируй другой! Перегенерировать? (1-да, 2-нет) '))
    if vopros == 1:
        dlina = int(input('Какую вы хотите длину пароля? (Число) '))

        parol = ''

        for i in range(dlina):
            parol += random.choice(simvoli)
        print(parol)
    else:
        break
