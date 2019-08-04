'''
    Módulo com a regras para definir quando um número será:
    Jovens e/ou Gênios
'''

def divisivel_por_3(num):
    '''
    Regra para atribuir Jovens 
    '''
    return (num % 3 == 0)


def divisivel_por_5(num):
    '''
    Regra para atribuir Gênios 
    '''
    return (num % 5 == 0)