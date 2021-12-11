class OpcoesArquivos:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def add_zeros(self, valor): 
        valor = str(valor).replace(',', '.')
        valor = str(round(float(valor), 2))
        if float(valor) == 0:
            valor = '0.00'
        else:
            cont = -1
            for i in valor:
                if i == '.':
                    cont += 1
                if cont >= 0:
                    cont += 1
            
            if cont == 2:
                valor += '0'
        
        return valor

    
    def criar_arquivo(self, nome, conteudo=''):
        try:
            arquivo = open(f'{self.diretorio}{nome}.txt', 'r')
            if not arquivo.read():
                OpcoesArquivos(self.diretorio).escrever_arquivo(nome, conteudo)
            arquivo.close()

        except:
            OpcoesArquivos(self.diretorio).escrever_arquivo(nome, conteudo)


    def escrever_arquivo(self, nome, conteudo=''):
        arquivo = open(f'{self.diretorio}{nome}.txt', 'a')
        arquivo.write(f'{conteudo}')
        arquivo.close()
    

    def apagar_arquivo(self, nome):
        arquivo = open(f'{self.diretorio}{nome}.txt', 'w')
        arquivo.write('')
        arquivo.close()


    def listar_dados(self, nome):
        arquivo = open(f'{self.diretorio}{nome}.txt', 'r')
        lista = arquivo.read().split(', ')
        lista.pop(-1)
        arquivo.close()

        aux = []
        for i in lista:
            x = i.split(' - ')
            aux.append(x)

        for i in aux:
            i[2] = OpcoesArquivos(self.diretorio).add_zeros(i[2])

        return aux


    def atualizar_total(self, nome):
        aux = OpcoesArquivos(self.diretorio).listar_dados(nome)
        aux.pop(-1)

        ganho = 0.00
        if nome == 'receitas':
            for x, y, z in aux:
                if int(x) < 6:
                    ganho += float(z.replace(',', '.'))
                else:
                    ganho -= float(z.replace(',', '.'))
        else:
            for i in aux:
                ganho += float(i[2].replace(',', '.'))
        
               
        texto = ''
        if nome == 'cartao':
            for x, y, z, a, b in aux:
                texto += f'{x} - {y} - {z} - {a} - {b}, '
        else:
            for x, y, z in aux:
                texto += f'{x} - {y} - {z}, '
        
        texto += f'{len(aux) + 1} - TOTAL - {OpcoesArquivos(self.diretorio).add_zeros(ganho)}, '

        arquivo = open(f'{self.diretorio}{nome}.txt', 'w')
        arquivo.write(texto)
        arquivo.close()


if __name__ == '__main__':  ## Local para testes
    a = str(__file__).replace('arquivos.py','')
    print(a)