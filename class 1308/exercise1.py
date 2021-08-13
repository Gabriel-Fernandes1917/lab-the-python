## system the

height = float(input('inform the height'))
weight = float(input('inform the weight'))
imc = weight/(height*height)
print('your index the imc is {:.2f}'.format(imc)) ## the .2f it suits to show only 2 decimal houses

if imc < 17:
    print('Muito abaixo do peso')
elif imc == 17 or imc < 18.49:
    print('abaixo do peso')
elif imc == 18.5 or imc < 24.99:
    print('peso normal')
elif imc == 25 or imc < 29.99:
    print('acima do peso')
elif imc == 30 or imc < 34.99:
    print('Obesidade |')
else:
    print('Obesidade ||')