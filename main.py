# Este arquivo esta sendo usado apenas para
# Excutrar o arquivo mestre do app
from start import menu_de_opcoes

if __name__ == '__main__':
    retorno = 1
    while True:
        retorno = menu_de_opcoes(retorno)
        if retorno == 0:  ## Simbolico
            break
