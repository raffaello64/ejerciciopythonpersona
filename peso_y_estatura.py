peso = int(input('Ingrese su peso en kg:'))
estatura = float(input('Ingrese su estatura en metros'))
IMC = peso / (estatura/100)**2

print('Su peso es: ', peso, ',', 'su estatura es: ', estatura,
'y su índice de masa corporal es: ', IMC)
