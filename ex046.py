from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('\033[1;33mKA-BOOMMMMM!!!!!:colisão:\033[m', language='pt'))