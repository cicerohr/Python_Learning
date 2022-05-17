# -*- coding: utf-8 -*-
r"""expressoes_regulares.py in: 2022-05-10.

Python version: 3.10.0

[Otávio Miranda](https://www.youtube.com/watch?v=wBI0yv2FG6U)

[Operações com expressões regulares](https://docs.python.org/3.10/library/re.html)

[Expressões Regulares - HOWTO](https://docs.python.org/3/howto/regex.html)
"""
import re

from tests.loguru_conf import logger


def main():
    """Função principal."""
    string = r"""
    search() -> Varre a string procurando a primeira ocorrência de uma RE.
    findall() -> Retorna uma lista de todas as correspondências encontradas.
    sub() -> Substitui todas as ocorrências de uma RE por um valor.
    compile() -> Compila uma RE para uso posterior.
    """
    print(re.search(r'RE', string))
    print(re.findall(r'RE', string))
    print(re.sub(r'RE', 'expressão regular', string))

    # Compila uma RE para uso posterior.
    regex = re.compile(r'RE')
    print(regex.search(string))
    print(regex.findall(string))
    print(regex.sub('expressão regular', string))

    meta_caracteres = r"""
    Meta-caracteres -> . ^ $ * + ? { } [ ] \ | ( )
    . -> qualquer caractere exceto uma nova linha
    ^ -> início da string
    $ -> fim da string
    * -> 0 ou mais ocorrências
    + -> 1 ou mais ocorrências
    ? -> 0 ou 1 ocorrência
    {...} -> quantidade de ocorrências
    [...] -> lista de ocorrências
    \ -> escape
    | -> ou
    (...) -> grupo de ocorrências
    """
    print(meta_caracteres)

    quantificadores = r"""
    Quantificadores -> * + ? {...}
    * -> 0 ou mais ocorrências
    + -> 1 ou mais ocorrências
    ? -> 0 ou 1 ocorrência
    {...} -> quantidade de ocorrências
    Obs.: o quantificador analisa a ocorrência imediatamente antes do caractere
    de referência.
    """
    # caractere de referência é o 'r'
    print(re.findall(r'ocor+', quantificadores))
    print(re.findall(r'ocor{2}', quantificadores))
    print(re.findall(r'oco[rr]{2}', quantificadores))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
