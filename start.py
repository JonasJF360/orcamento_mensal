import os
import platform
from datetime import datetime

data_hora = datetime.now()
DATA_HOJE = data_hora.strftime('%d/%m/%Y')

# Configuracões para Windows e Linux
DIRETORIO =  str(__file__).replace('start.py','') + 'db/'

if not os.path.exists(DIRETORIO):
    os.makedirs(DIRETORIO)

if str(platform.system()) == 'Linux':
    LIMPAR_TELA = 'clear'
else:
    LIMPAR_TELA = 'cls'

# Opções de cadastro
import arquivos as OpArquivo
opcoes_arquivos = OpArquivo.OpcoesArquivos(DIRETORIO)

# Titulos do sistema
tamanho_linha = 35

def titulo(texto, x='-'):
    tamanho_linha
    linha = x * tamanho_linha
    # Mudar o numero ":^34" sempre que alterar a global tamanho_linha
    print(f'{linha}\n{texto.upper():^35}\n{linha}')

def cabecalio():
    os.system(LIMPAR_TELA)
    titulo('APP - JJF CONTABIL', '=')

def imprecao_personalizada(x, y):
        aux = tamanho_linha - (len(x) + len(y)) - 2
        if aux < 0:
            aux = 0
        pontilhados = '.' * aux
        print(f'{x} {pontilhados} {y}')

def parar():
    x = input('\nTecle ENTER continuar ')


def editar_valores_receitas():
    listar_receitas = opcoes_arquivos.listar_dados('receitas')
    listar_receitas.pop(-1)
    opcoes_arquivos.apagar_arquivo('receitas')
    for i in listar_receitas:
        x = 1
        while True:
            cabecalio()
            if x == -1:
                print('# Valor inválido, tente novamente!')
            titulo('Editar receitas')
            x = input(f'{i[1]}: ').replace(',', '.')
            try:
                x = float(x)
                break
            except:
                x = -1

        i[2] = opcoes_arquivos.add_zeros(x)

    texto = ''
    for x, y, z in  listar_receitas:
        texto += f'{x} - {y} - {z}, '

    texto += f'{len(listar_receitas) + 1} - TOTAL - 0, '
    opcoes_arquivos.escrever_arquivo('receitas', texto)


def abrir_receitas(validacao):
    cabecalio()
    if validacao == -1:
        print('## OPÇÃO INVÁLIDA!')
    titulo('Receitas do mês')
    opcoes_arquivos.atualizar_total('receitas')
    listar_receitas = opcoes_arquivos.listar_dados('receitas')
    total = listar_receitas[-1]
    listar_receitas.pop(-1)
    print()
    for x, y, z in listar_receitas:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)
    print()
    valor_a = f'{total[1]}:'
    valor_b = f'R$ {total[2]}'
    imprecao_personalizada(valor_a, valor_b)
    
    print('\n01 - Editar valores',
          '\n00 - Voltar')
    opcoes = input('## : ')
    if opcoes == '1':
        editar_valores_receitas()
    elif opcoes == '0':
        return 0
    else:
        return -1
    return 1


def editar_valores_despesas():
    listar_receitas = opcoes_arquivos.listar_dados('despesas')
    listar_receitas.pop(-1)
    opcoes_arquivos.apagar_arquivo('despesas')
    for i in listar_receitas:
        x = 1
        while True:
            cabecalio()
            if x == -1:
                print('# Valor inválido, tente novamente!')
            titulo('Editar despesas')
            x = input(f'{i[1]}: ').replace(',', '.')
            try:
                x = float(x)
                break
            except:
                x = -1

        i[2] = opcoes_arquivos.add_zeros(x)

    texto = ''
    for x, y, z in  listar_receitas:
        texto += f'{x} - {y} - {z}, '

    texto += f'{len(listar_receitas) + 1} - TOTAL - 0, '
    opcoes_arquivos.escrever_arquivo('despesas', texto)


def editar_valores_despesas_apenas_uma():
    cabecalio()
    titulo('Editar uma despesa')
    listar_despesas = opcoes_arquivos.listar_dados('despesas')
    listar_despesas.pop(-1)
    opcoes_arquivos.apagar_arquivo('despesas')
    x = 1
    while True:
        cabecalio()
        if x == -1:
            print('# Valor inválido, tente novamente!')
        titulo('Editar uma despesa')
        for x, y, z in listar_despesas:
            valor_a = f'{x} - {y}:'
            valor_b = f'R$ {z}'
            imprecao_personalizada(valor_a, valor_b)

        x = input('\nDigite o numero da despesa que\ndeseja editar o valor: ').replace(',', '.')
        try:
            a, b = float(x), int(x)
            if (a - b) != 0:
                x = -1
            else:
                break
        except:
            x = -1
    
    for i in listar_despesas:
        if x == i[0]:
            y = 1
            while True:
                cabecalio()
                if y == -1:
                    print('# Valor inválido, tente novamente!')
                titulo('Editar uma despesa')
                y = input(f'{i[1]}: ').replace(',', '.')
                try:
                    y = float(y)
                    break
                except:
                    y = -1

            i[2] = opcoes_arquivos.add_zeros(y)
    
    texto = ''
    for x, y, z in  listar_despesas:
        texto += f'{x} - {y} - {z}, '

    texto += f'{len(listar_despesas) + 1} - TOTAL - 0, '
    opcoes_arquivos.escrever_arquivo('despesas', texto)


def adicionar_uma_despesa():
    listar_receitas = opcoes_arquivos.listar_dados('despesas')
    listar_receitas.pop(-1)
    opcoes_arquivos.apagar_arquivo('despesas')
    erro = 0
    while True:
        cabecalio()
        if erro == -1:
            print('Digite uma descrição válida')
        titulo('Adiciona uma despesa')
        nome = input(f'Dê um nome para a despesa\n## : ').upper()
        if not nome:
            erro == -1
        else:
            try:
                nome = float(nome)
                erro = -1
            except:
                break

    texto = ''
    for x, y, z in  listar_receitas:
        texto += f'{x} - {y} - {z}, '

    texto += f'{len(listar_receitas) + 1} - {nome} - 0, '
    texto += f'{len(listar_receitas) + 2} - TOTAL - 0, '
    opcoes_arquivos.escrever_arquivo('despesas', texto)


def apagar_uma_despesa():
    cabecalio()
    titulo('Apagar uma despesa')
    listar_despesas = opcoes_arquivos.listar_dados('despesas')
    listar_despesas.pop(-1)
    opcoes_arquivos.apagar_arquivo('despesas')
    x = 1
    while True:
        cabecalio()
        if x == -1:
            print('# Valor inválido, tente novamente!')
        titulo('Apagar uma despesa')
        for x, y, z in listar_despesas:
            valor_a = f'{x} - {y}:'
            valor_b = f'R$ {z}'
            imprecao_personalizada(valor_a, valor_b)

        x = input('\nDigite o numero da despesa que\nvocê deseja apagar: ').replace(',', '.')
        try:
            a, b = float(x), int(x)
            if (a - b) != 0:
                x = -1
            else:
                break
        except:
            x = -1
        
    texto, numero = '', 1
    for a, b, c in  listar_despesas:
        if x == a:
            pass
        else:
            texto += f'{numero} - {b} - {c}, '
            numero += 1

    texto += f'{len(listar_despesas) + 1} - TOTAL - 0, '
    opcoes_arquivos.escrever_arquivo('despesas', texto)


def abrir_despesas(validacao):
    cabecalio()
    if validacao == -1:
        print('## OPÇÃO INVÁLIDA!')
    titulo('Despesas do mês')
    opcoes_arquivos.atualizar_total('despesas')
    listar_despesas = opcoes_arquivos.listar_dados('despesas')
    total = listar_despesas[-1]
    listar_despesas.pop(-1)
    print()
    vazio = 0
    if not listar_despesas:
        vazio = 1
        print('* NENHUMA DESPESA CADASTRADA')
    for x, y, z in listar_despesas:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)

    print()
    valor_a = f'{total[1]}:'
    valor_b = f'R$ {total[2]}'
    imprecao_personalizada(valor_a, valor_b)
    print('\n01 - Editar valores',
          '\n02 - Adicionas despesa',
          '\n03 - Apagar uma despesa'
          '\n00 - Voltar')
    opcoes = input('## : ')
    if opcoes == '1':
        if vazio == 1:
            return -1
        while True:
            cabecalio()
            titulo('Editar despesas')
            print('\n01 - Editar toda as despesa')
            uma_ou_tudo = input('02 - Editar apenas uma\n## : ')
            if uma_ou_tudo == '1':
                editar_valores_despesas()
                break
            if uma_ou_tudo == '2':
                editar_valores_despesas_apenas_uma()
                break
                
    elif opcoes == '2':
        adicionar_uma_despesa()
    elif opcoes == '3':
        if vazio == 1:
            return -1
        apagar_uma_despesa()
    elif opcoes == '0':
        return 0
    else:
        return -1
    return 1


def listar_datas(parcelas, data_compra):
    MAX_MESES = 12
    lista_das_datas = []
    parcelas_restantes = 0

    # Data da compra
    data_da_compra = str(data_compra).split('/')
    dia, mes, ano = int(data_da_compra[0]), int(data_da_compra[1]), int(data_da_compra[2])

    lista_das_datas.append([dia, mes, ano])

    # Data hoje
    data_hoje = str(DATA_HOJE).split('/')
    dia_hoje, mes_hoje, ano_hoje = int(data_hoje[0]), int(data_hoje[1]), int(data_hoje[2])

    lista_das_datas.append([dia_hoje, mes_hoje, ano_hoje])

    # Data inicial do pagamento
    mes_inicio = mes + 1
    ano_inicio = ano
    if mes_inicio > 12:
        mes_inicio = 1
        ano_inicio += 1

    lista_das_datas.append([dia, mes_inicio, ano_inicio])

    # Data final do pagamento
    mes_final = mes
    ano_final = ano
    contar = 'nao'
    for i in range(parcelas):
        mes_final += 1
        if mes_final > 12:
            mes_final = 1
            ano_final += 1
        if ano_final == ano_hoje:
            if mes_final >= mes_hoje:
                contar = 'sim'
        if contar == 'sim':
            parcelas_restantes += 1
        
    lista_das_datas.append([dia, mes_final, ano_final])

    # Parcelas restantes
    lista_das_datas.append(parcelas_restantes)

    return lista_das_datas


def calcular_cartao_mes(valor, parcela, data_compra):
    lst_datas = listar_datas(parcela, data_compra)
    if lst_datas[4] == 0:
        valor_parcela = 0
    else:
        valor_parcela = valor / parcela
    return valor_parcela


def calcular_total_cartao(valor, parcela, data_compra):
    lst_datas = listar_datas(parcela, data_compra)
    valor_total = 0
    if lst_datas[4] == 0:
        if lst_datas[0][1] == lst_datas[1][1] and lst_datas[0][2] == lst_datas[1][2]:
            valor_total = valor - (valor * lst_datas[4])
        else:
            valor_total = 0
    else:
        valor_total =  calcular_cartao_mes(valor, parcela, data_compra) * lst_datas[4]
    return valor_total


def vizualizar_compras_cartao_de_credito():
    cabecalio()
    titulo('Dividas no cartão')
    listar_cartao = opcoes_arquivos.listar_dados('cartao')
    listar_cartao.pop(-1)
    print()
    total_pagar = 0
    total_devendo = 0
    for x, y, z, a, b, in listar_cartao:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)
        valor_a = f'PARCELAS: {a}x'
        valor_b = f'DIA: {b}'
        imprecao_personalizada(valor_a, valor_b)
        valor = calcular_cartao_mes(float(z) , int(a), b)
        valor_a = 'PAGAR:'
        valor_b = f'R$ {opcoes_arquivos.add_zeros(valor)}'
        imprecao_personalizada(valor_a, valor_b)
        total_pagar += valor
        total_devendo += calcular_total_cartao(float(z) , int(a), b)
        print()

    valor_a = f'TOTAL DO MÊS:'
    valor_b = f'R$ {total_pagar:.2f}'
    imprecao_personalizada(valor_a, valor_b)
    valor_a = f'TOTAL RESTANTE:'
    valor_b = f'R$ {total_devendo:.2f}'
    imprecao_personalizada(valor_a, valor_b)
    parar()


def adicionar_compra_cartao():
    listar_cartao = opcoes_arquivos.listar_dados('cartao')
    listar_cartao.pop(-1)
    if len(listar_cartao) == 1 and listar_cartao[0][1] == 'SEM COMPRA':
        listar_cartao.pop(-1)
    opcoes_arquivos.apagar_arquivo('cartao')
    erro = 0
    while True:
        cabecalio()
        if erro == -1:
            print('Digite uma descrição válida')
        titulo('Adicionar uma compra')
        nome = input(f'Dê um nome para a compra\n## : ').upper()
        if not nome:
            erro == -1
        else:
            try:
                nome = float(nome)
                erro = -1
            except:
                break
    erro = 0
    while True:
        cabecalio()
        if erro == -1:
            print('Algo está errado, tente novamente')
        titulo('Adicionar uma compra')
        valor = input(f'Insira o valor total da compra\n## : ').replace(',', '.')
        if not valor:
            erro == -1
        else:
            try:
                valor = float(valor)
                if valor < 0:
                    erro = -1
                else:
                    valor = opcoes_arquivos.add_zeros(valor)
                    break
            except:
                erro = -1
    erro = 0
    while True:
        cabecalio()
        if erro == -1:
            print('Algo está errado, tente novamente')
        if erro == -2:
            print('Inválido! Minimo 1 e máximo 100')
        titulo('Adicionar uma compra')
        parcela = input(f'Insira a quantidade de parcelas\n## : ').replace(',', '.')
        if not parcela:
            erro == -1
        else:
            try:
                parcela = float(parcela)
                if float(parcela) - int(parcela) != 0:
                    erro = -1
                elif parcela < 1 or parcela > 100:
                    erro = -2
                else:
                    parcela = int(parcela)
                    break
            except:
                erro = -1
    lista_hoje = str(DATA_HOJE).split('/')
    mes_hoje, ano_hoje = int(lista_hoje[1]), int(lista_hoje[2])
    erro = 0
    while True:
        cabecalio()
        if erro == -1:
            print('Algo está errado, tente novamente')
        if erro == -2:
            print('A data não pode ser maior que hoje')
        titulo('Adicionar uma compra')
        data_compra = input(f'Insira a data de reaização da\ncompra DD/MM/AAAA\n## : ').replace('-', '/')
        if not data_compra:
            erro == -1
        else:
            try:
                x = data_compra.split('/')
                y = int(data_compra.replace('/', ''))
                if len(x[0]) != 2 or len(x[1]) != 2 or len(x[2]) != 4:
                    erro = -1
                    continue
                if int(x[1]) < 1 or int(x[1]) > 12:
                    erro = -1
                    continue
                if int(x[2]) > ano_hoje:
                    erro = -2
                    continue
                if int(x[2]) == ano_hoje:
                    if int(x[1]) > mes_hoje:
                        erro = -2
                        continue
                break              
            except:
                erro = -1

    texto = ''
    if listar_cartao:
        for x, y, z, a, b in  listar_cartao:
            texto += f'{x} - {y} - {z} - {a} - {b}, '

    texto += f'{len(listar_cartao) + 1} - {nome} - {valor} - {parcela} - {data_compra}, '
    texto += '0 - TOTAL - 0.00, '
    opcoes_arquivos.escrever_arquivo('cartao', texto)


def apagar_uma_compra_cartao():
    listar_cartao = opcoes_arquivos.listar_dados('cartao')
    listar_cartao.pop(-1)
    if len(listar_cartao) == 1 and listar_cartao[0][1] == 'SEM COMPRA':
        print('\nNão existe nenhuma compra ainda!\n')
        parar()
    else:
        opcoes_arquivos.apagar_arquivo('cartao')
        x = 1
        while True:
            cabecalio()
            if x == -1:
                print('Algo está errado, tente novamente!')
            titulo('Dividas no cartão')
            print()
            for x in listar_cartao:
                valor_a = f'{x[0]} - {x[1]}:'
                valor_b = f'R$ {x[2]}'
                imprecao_personalizada(valor_a, valor_b)

            cod = input('\nDigite o numero da compra que\nvocê deseja apagar: ').replace(',', '.')
            try:
                a, b = float(cod), int(cod)
                if (a - b) != 0:
                    x = -1
                else:
                    break
            except:
                x = -1

        texto = ''
        if len(listar_cartao) == 1:
            if cod == listar_cartao[0][0]:
                texto = f'1 - SEM COMPRA - 0.00 - 0 - {DATA_HOJE}, '
            else:
                pass
        elif listar_cartao:
            novo_cod = 1
            for x, y, z, a, b in  listar_cartao:
                if cod == x:
                    pass
                else:
                    texto += f'{novo_cod} - {y} - {z} - {a} - {b}, '
                    novo_cod += 1

        texto += '0 - TOTAL - 0.00, '
        opcoes_arquivos.escrever_arquivo('cartao', texto)


def abrir_cartao(validacao):
    opcoes_arquivos.atualizar_total('cartao')
    cabecalio()
    if validacao == -1:
        print('## OPÇÃO INVÁLIDA!')
    titulo('Dividas no cartão')
    print('01 - Visualizar compras',
          '\n02 - Adicionas uma nova',
          '\n03 - Apagar uma compra'
          '\n00 - Voltar')
    opcoes = input('## : ')
    if opcoes == '1':
        vizualizar_compras_cartao_de_credito()
    elif opcoes == '2':
        adicionar_compra_cartao()
    elif opcoes == '3':
        apagar_uma_compra_cartao()
    elif opcoes == '0':
        pass
        return 0
    else:
        return -1
    return 1


def ver_resumo():
    cabecalio()
    print('    RESUMO DE GANHOS E DESPESAS\n')
    
    # Visualizar e salvar as receitasa
    opcoes_arquivos.atualizar_total('receitas')
    listar_receitas = opcoes_arquivos.listar_dados('receitas')
    total = listar_receitas[-1]
    listar_receitas.pop(-1)
    titulo('Receitas')
    for x, y, z in listar_receitas:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)
    print()
    valor_a = f'{total[1]}:'
    valor_b = f'R$ {total[2]}'
    imprecao_personalizada(valor_a, valor_b)
    ganho_total = total[2]

    # Visualizar e salvar as despesas
    opcoes_arquivos.atualizar_total('despesas')
    listar_despesas = opcoes_arquivos.listar_dados('despesas')
    total = listar_despesas[-1]
    listar_despesas.pop(-1)
    print()
    titulo('Despesas')
    if not listar_despesas:
        print('* NENHUMA DESPESA CADASTRADA')
    for x, y, z in listar_despesas:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)

    print()
    valor_a = f'{total[1]}:'
    valor_b = f'R$ {total[2]}'
    imprecao_personalizada(valor_a, valor_b)
    despesas_total = total[2]

    # Visualizar e salvar as compras no cartão
    print()
    titulo('Cartão de crédito')
    listar_cartao = opcoes_arquivos.listar_dados('cartao')
    listar_cartao.pop(-1)
    print()
    total_pagar = 0
    total_devendo = 0
    for x, y, z, a, b, in listar_cartao:
        valor_a = f'{y}:'
        valor_b = f'R$ {z}'
        imprecao_personalizada(valor_a, valor_b)
        valor_a = f'PARCELAS: {a}x'
        valor_b = f'DIA: {b}'
        imprecao_personalizada(valor_a, valor_b)
        valor = calcular_cartao_mes(float(z) , int(a), b)
        valor_a = 'PAGAR:'
        valor_b = f'R$ {opcoes_arquivos.add_zeros(valor)}'
        imprecao_personalizada(valor_a, valor_b)
        total_pagar += valor
        total_devendo += calcular_total_cartao(float(z) , int(a), b)
        print()

    valor_a = f'TOTAL DO MÊS:'
    valor_b = f'R$ {total_pagar:.2f}'
    imprecao_personalizada(valor_a, valor_b)
    valor_a = f'TOTAL RESTANTE:'
    valor_b = f'R$ {total_devendo:.2f}'
    imprecao_personalizada(valor_a, valor_b)

    # Resumo final
    print()
    titulo('Resumo geral')
    valor_a = f'GANHO:'
    valor_b = f'R$ {float(ganho_total):.2f}'
    imprecao_personalizada(valor_a, valor_b)
    valor_a = f'GASTOS:'
    total_gasto = float(despesas_total) + total_pagar
    valor_b = f'R$ {total_gasto:.2f}'
    imprecao_personalizada(valor_a, valor_b)
    valor_a = f'LIVRE:'
    total_livre = float(ganho_total) - total_gasto
    valor_b = f'R$ {total_livre:.2f}'
    imprecao_personalizada(valor_a, valor_b)
    parar()


def apagar_todos_os_registros(validacao):
    cabecalio()
    if validacao == -1:
        print('## OPÇÃO INVÁLIDA!')
    titulo('resetar todos os dados')
    print('Essa opção irá resetar todos os',
          '\ndados do sistema, fazendo com',
          '\nque tudo volte do zero, deseja',
          '\nmesmo fazer isso?')
    confirmacao = input('Sim ou Não [S/N]: ').upper()
    if confirmacao == 'S' or confirmacao == 'SIM':
        opcoes_arquivos.apagar_arquivo('receitas')
        opcoes_arquivos.apagar_arquivo('despesas')
        opcoes_arquivos.apagar_arquivo('cartao')
        criar_arquivos_do_sistema()
        print('\nSistema foi resetado com sucesso!')
        parar()
    elif confirmacao == 'N' or confirmacao == 'NAO' or confirmacao == 'NÃO':
        print('\nMuito bem, opcão cancelada!')
        parar()
    else:
        return -1

    return 0


def criar_arquivos_do_sistema():
    opcoes_arquivos.criar_arquivo('receitas', '1 - SALÁRIO - 0.00, 2 - BENEFICIOS - 0.00, 3 - HORAS EXTRAS - 0.00, 4 - PIS/FERIAS - 0.00, 5 - OUTROS - 0.00, 6 - DESCONTOS - 0.00, 7 - TOTAL - 0.00, ')
    opcoes_arquivos.criar_arquivo('despesas', '1 - COMPRAS - 0.00, 2 - ENERGIA - 0.00, 3 - ÁGUA - 0.00, 4 - INTERNET - 0.00, 5 - TRANSPORTE - 0.00, 6 - TOTAL - 0.00, ')
    opcoes_arquivos.criar_arquivo('cartao', f'1 - SEM COMPRA - 0.00 - 0 - {DATA_HOJE}, 2 - TOTAL - 0.00, ')


def menu_de_opcoes(x):
    criar_arquivos_do_sistema()
    cabecalio()
    if x != 1:
        print('## OPÇÃO INVÁLIDA!')
    titulo('Escolha uma opçao')
    print('01 - Receitas',
        '\n02 - Despesas',
        '\n03 - Cartão de crédito',
        '\n04 - Visualizar Resumo',
        '\n05 - Resetar dados',
        '\n00 - Sair do programa')
    opcao = input('## : ')
    if opcao == '1':
        bla = 1
        while True:
            bla = abrir_receitas(bla)
            if bla == 0:
                break
        
    elif opcao == '2':
        bla = 1
        while True:
            bla = abrir_despesas(bla)
            if bla == 0:
                break
        
    elif opcao == '3':
        bla = 1
        while True:
            bla = abrir_cartao(bla)
            if bla == 0:
                break
            
    elif opcao == '4':
        ver_resumo()
    elif opcao == '5': ## Fechar o programa
        bla = 1
        while True:
            bla = apagar_todos_os_registros(bla)
            if bla == 0:
                break
        
    elif opcao == '0': ## Fechar o programa
        return 0
    else:
        return -1
    return 1


if __name__ == '__main__':   ## Local para testes
    retorno = 1
    while True:
        retorno = menu_de_opcoes(retorno)
        if retorno == 0:  ## Simbolico
            print()
            titulo('Ok, até a próxima!', '=')
            x = input(' ')
            break
