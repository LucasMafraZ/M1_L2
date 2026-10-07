import random
c_senha = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

comprimento = int(input('Qual o comprimento da senha?'))    

senha = ''

for i in range(comprimento):
    senha += random.choice(c_senha)

print('\n')
print(f'nova senha: {senha}')
