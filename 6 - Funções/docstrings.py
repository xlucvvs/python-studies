# Documentando funções com docstrings
# Podemos ter acesso a documentação de uma função em python utilizando a propriedade especial (.__doc__)
# Podemos ainda fazer acesso a documentação com a função help().

# Exemplos
def diz_oi():
    """Uma funcao simples que retorna a string 'oi'"""
    return 'Oi'

def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' elevado a potencia informada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia a qual o numero será elevado. Por padrão é 2.
    :return: Retorna o exponencial de numero ^ potencia:
    """
    return numero ** potencia

