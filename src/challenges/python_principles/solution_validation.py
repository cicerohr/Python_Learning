# -*- coding: utf-8 -*-
r"""solution_validation.py in: 2022-05-02.

Python version: 3.10.0

O objetivo deste desafio é escrever código que possa analisar envios de código.
Vamos simplificar muito as coisas para não tornar isso muito difícil.

Escreva uma função chamada validate que usa o código representado como uma
‘string’ como seu único parâmetro.

Sua função deve verificar algumas coisas:

    o código deve conter a palavra-chave def
        caso contrário, retorne "def ausente"
    o código deve conter o símbolo :
        caso contrário, retorne "ausente :"
    o código deve conter ( e ) para a lista de parâmetros
        caso contrário, retorne "parêntese ausente"
    o código não deve conter ()
        caso contrário, retorne "param ausente"
    o código deve conter quatro espaços para recuo
        caso contrário, retorne "recuo ausente"
    o código deve conter validate
        caso contrário, retorne "nome errado"
    o código deve conter uma instrução de retorno
        caso contrário, retorne "falta de retorno"

Se todas essas condições forem atendidas, seu código deverá retornar True.

Aí vem a reviravolta: sua solução deve retornar True ao se validar.
"""
from tests.loguru_conf import logger


def validate(code):
    """Valida o código."""
    if 'def' not in code:
        return 'missing def'
    if ':' not in code:
        return 'missing :'
    if '(' not in code or ')' not in code:
        return 'missing paren'
    if '(' + ')' in code:
        return 'missing param'
    if '    ' not in code:
        return 'missing indent'
    if 'validate' not in code:
        return 'wrong name'
    if 'return' not in code:
        return 'missing return'
    return True


def main():
    """Função principal."""
    print(
        validate(
            """
            def validate(code):
                if 'def' not in code:
                    return 'missing def'
                if ':' not in code:
                    return 'missing :'
                if '(' not in code or ')' not in code:
                    return "missing paren'
                if '(' + ')' in code:
                    return 'missing param'
                if '    ' not in code:
                    return 'missing indent'
                if 'validate' not in code:
                    return 'wrong name'
                if 'return' not in code:
                    return 'missing return'
                return 
            """
        )
    )


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
