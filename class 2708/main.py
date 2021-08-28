dicionario_produ={}
produto={}
dados_produ=[None,None]
laco='sim'
while(laco=="sim"):
    code=input('inform o codigo do produto')
    name=input('informe o nome do produto')
    preco= float(input('informe o preco do produto'))
    dados_produ[0]=name
    dados_produ[1]=preco
    produto={code:dados_produ}
    dicionario_produ.update(produto)
    laco=input("Deseja add mais produtos ? sim ou nao")
print(dicionario_produ)
print(dicionario_produ["2020"])