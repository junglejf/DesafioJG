'''
    Módulo que contém as funções de output do programa
'''
import sys 
import const
import rules as rl

def jovensgenios(num):
    '''
    Funciona que utiliza rules pra retornar a string correta
    '''
    s = ''
    if(rl.divisivel_por_3(num)):
        s = "Jovens"
    if(rl.divisivel_por_5(num)):
        s = ''.join([s ,"Gênios"])
    # se s = '' => retorna o número não divisível por 3 e nem por 5
    return ( s or str(num) )  


def print_jg (x):
    '''
    Função para imprimar o valores de 0 até x da função jovensgenios
    '''
    sys.stdout.write('\n')
    for num in range(x+1):
        sys.stdout.write(''.join([jovensgenios(num),' | ']))
    sys.stdout.write('\n \n')

def input_X():
    '''
    Função para receber uma entrada X válida
    '''
    erros = 0
    while True:
        try:
            if (erros == const.MAXIMO_TENTATIVAS):
                raise Exception(const.RED+" Excesso de tentativas !!!"+const.RESET)          

            x = int(input("\n Entre com o valor de X: "))
            assert x >= 0

        except AssertionError :
            sys.stdout.write(const.RED+"\nO valor de X não pode ser negativo, escolha outro valor !!!\n"+const.RESET)
            erros += 1
            continue 
            # continua até que o número máximo de tentativas mal sucedidas seja alcançado

        return x