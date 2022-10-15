
import enum


texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

nuevo = texto.split("#")

for i, c in enumerate(nuevo):
    nuevo[i] = c.capitalize()

    if i==0:
        nuevo[i] = nuevo[i] + "..."

    else:
        nuevo[i] = "- " + nuevo[i] + "."

for i in nuevo:
    print(i)