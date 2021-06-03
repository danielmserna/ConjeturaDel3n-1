numero = int(input('Ingrese el número: '))
cadena = ""
while numero!=1 and numero>0:
  if numero%2 == 0:
    numero//=2
  else:
    numero = 3*numero + 1
  cadena = cadena + " " + str(numero)
print(cadena)