lista_nome = []

def formatar_nome(nome):
    return nome.strip().lower()

while True:
    print('\n' + '='*30)
    print('    MENU PRINCIPAL     ')
    print('[1] Cadastrar\n'
          '[2] Listar \n'
          '[3] Buscar\n'
          '[4] Remover\n'
          '[5] sair ')
    print('-='* 30)

    try:
        opcao = int(input('Digite um numero para entrar em uma opção: '))
        print('-=' * 20)
    except ValueError:
        print('Digite apenas numeros ')
        continue


    if opcao == 1:
        nome = formatar_nome(input('Digite o nome:'))
        if nome in lista_nome:
            print(f'Nome {nome} ja cadastrado')
        else:
            lista_nome.append(nome)
            print(f'Nome {nome} cadastrado com sucesso')

    elif opcao == 2:
        print('-------Nomes cadastrados-------')
        if not lista_nome:
            print('Nenhum nome cadastrado.')

        for i,nome in enumerate(lista_nome, start=1):
            print(f'{i}. {nome}')

        input('\nPressione ENTER para continuar...')

    elif opcao == 3:
        buscar = formatar_nome(input('Digite o nome do buscar: '))

        if buscar in lista_nome:
            print(f'Nome {buscar} encontrado com sucesso! ')

        else:
            print(f"Nome não encontrado! ")
            print('-=' * 20)
        input('\nPressione ENTER para continuar...')


    elif opcao == 4:
        deletar = formatar_nome(input('Digite o nome do remover: '))

        if deletar in lista_nome:
            confirmar = input(f'Tem certeza que deseja remover {deletar}? [S/N] ').lower()
            if confirmar == 's':
                lista_nome.remove(deletar)
                print(f"Nome {deletar} encontrado, removido com sucesso! ")
            else:
                print('Remoção cancelada')
        else:
            print("Nome não encontrado!")
            print('-=' * 20)
        input('\nPressione ENTER para continuar...')

    elif opcao == 5:
        print("saindo do programa ...")
        break

    else:
        print('opcão invalida!')
        input('\nPressione ENTER para continuar...')
        print('-=' * 20)



