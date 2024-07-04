import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Cuántos caracteres debe tener tu contraseña?"))
password = ""
for i in range(longitud):
    letra = random.choice(caracteres)
    password = password + letra
print(password)
