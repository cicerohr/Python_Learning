# -*- coding: utf-8 -*-
r"""minimax.py in: 2022-05-08.

Python version: 3.10.0


"""
from math import log

from tests.loguru_conf import logger


def minimax(cur_depth,
            node_index,
            max_turn,
            scores,
            target_depth
            ):
    # base case : target_depth reached
    if cur_depth == target_depth:
        return scores[node_index]

    if max_turn:
        return max(
            minimax(
                cur_depth + 1, node_index * 2, False, scores, target_depth
            ),
            minimax(
                cur_depth + 1, node_index * 2 + 1, False, scores, target_depth
            )
        )
    else:
        return min(
            minimax(
                cur_depth + 1, node_index * 2, True, scores, target_depth
            ),
            minimax(
                cur_depth + 1, node_index * 2 + 1, True, scores, target_depth
            )
        )


def main():
    """Função principal."""
    scores = [3, 5, 2, 9, 12, 5, 23, 23]

    tree_depth = log(len(scores), 2)

    print("The optimal value is : ", end="")
    print(minimax(0, 0, True, scores, tree_depth))


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
