##IRPF

salario = float(input('informe seu salario'))

if salario < 1903.98:
    print('seu salario é : {}'.format(salario-((salario*8)/100)))
elif salario == 1903.98 or salario < 2826.65:
    print('seu salario é : {}'.format(salario-((salario*15.5)/100)))
elif salario == 2826.66 or salario < 3751.05:
    print('seu salario é : {}'.format(salario-((salario*23)/100)))
elif salario == 3751.06 or salario < 4664.68:
    print('seu salario é : {}'.format(salario-((salario*30.5)/100)))
else:
    print('seu salario é : {}'.format(salario - ((salario * 35.5) / 100)))