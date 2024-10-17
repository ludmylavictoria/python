 # Loop infinito -> Quando um código não tem fim #

condicao = True 

while condicao: 
    nome = input('Qual o seu nome:')
    
    if nome == 'sair':
        break # para a execução  de while, sai do loop de repetição 

    print(f'Seu nome e {nome}')

    print ('Acabou')