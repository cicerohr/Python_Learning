# -*- coding: utf-8 -*-
r"""pong.py in: 2022-05-09.

Python version: 3.10.0

Estudo de OOP (Object-oriented programming) com o jogo Pong.

O jogo Pong é um jogo de tiro e corrida de bolas de ping-pong.

A classe Turtle é usada para desenhar o jogo.

Desenvolvido por:
[Código do Estagiário](https://www.youtube.com/watch?v=cTeR3ATHpZo)
"""

import turtle

from loguru_conf import logger


class Shape(turtle.Turtle):
    """Classe abstrata para desenhar formas geométricas.

    A classe Shape é uma classe abstrata que herda de Turtle.

    Esta classe é usada para desenhar e posicionar as formas geométricas
    dos ‘players’, da bola e do placar.

    """

    def __init__(self, position_x: float = None):
        """Construtor da classe Shape.

        :param position_x: posição da forma no eixo x.
        :type position_x: float
        """
        # Construtor da classe mãe.
        turtle.Turtle.__init__(self)
        # retangulo 10x10
        self.shape('square')
        self.color('white')
        # retira o rastro da tartaruga
        self.penup()
        # posicionamento x e y do jogador na tela
        self.goto(position_x, 0)


class Player(Shape):
    """Classe que representa um jogador.

    A classe Player é uma subclasse (herda) da classe Shape.
    """

    def __init__(self, position_x: float = None):
        """Construtor da classe Player.

        :param position_x: posição do jogador no eixo x.
        :type position_x: float
        """
        # Construtor da classe mãe.
        Shape.__init__(self, position_x)
        # forma do jogador
        self.shapesize(6, 0.7)
        # velocidade do jogador
        self.player_speed = 20

    def up(self):
        """Método para mover o jogador para cima."""
        self.sety(self.ycor() + self.player_speed)

    def down(self):
        """Método para mover o jogador para baixo."""
        self.sety(self.ycor() - self.player_speed)


class Ball(Shape):
    """Classe que representa a bola.

    A classe Ball é uma subclasse (herda) da classe Shape.
    """

    def __init__(self, position_x=None):
        """Construtor da classe Ball.

        :param position_x: posição da bola no eixo x.
        :type position_x: float
        """
        # Construtor da classe mãe.
        Shape.__init__(self, position_x)
        # velocidade da bola nos eixos x e y
        self.speed_x = 0.1
        self.speed_y = 0.1

    def update(self, player_a: Player, player_b: Player):
        """Atualiza a posição da bola.

        :param player_a: jogador A.
        :type player_a: classe Player
        :param player_b: jogador B.
        :type player_b: classe Player
        """
        self.collision(player_a, player_b)
        self.setx(self.xcor() + self.speed_x)
        self.sety(self.ycor() + self.speed_y)

    def collision(self, player_a: Player, player_b: Player):
        """Verifica se a bola colidiu.

        :param player_a: jogador A.
        :type player_a: classe Player
        :param player_b: jogador B.
        :type player_b: classe Player
        """
        # verifica se a bola colidiu na parte superior da tela
        if self.ycor() > 290:
            self.sety(290)
            self.speed_y *= -1
        # verifica se a bola colidiu na parte inferior da tela
        if self.ycor() < -290:
            self.sety(-290)
            self.speed_y *= -1
        # verifica se a bola colidiu com o jogador A
        if self.xcor() < -340 and self.difference(player_a):
            self.speed_x *= -1
        # verifica se a bola colidiu com o jogador B
        if self.xcor() > 340 and self.difference(player_b):
            self.speed_x *= -1

    def difference(self, player: Player) -> bool:
        """Calcula a diferença entre a bola e o jogador.

        :param player: jogador.
        :type player: classe Player
        :return: True se a diferença for menor que 20, False caso contrário.
        :rtype: bool
        """
        return player.ycor() + 60 > self.ycor() > player.ycor() - 60


class Score(Shape):
    """Classe que representa o placar.

    A classe Score é uma subclasse (herda) da classe Shape.
    """

    def __init__(self, position_y: float = None):
        """Construtor da classe Score.

        :param position_y: posição do placar no eixo y.
        :type position_y: float
        """
        # Construtor da classe mãe.
        Shape.__init__(self, position_y)
        # posicionamento x e y do placar na tela
        # (sobrescreve o método da classe mãe - polimorfismo)
        self.goto(0, position_y)
        # escreve o placar
        self.score_a = 0
        self.score_b = 0
        # esconde a tartaruga
        self.hideturtle()
        self.draw_score()

    def draw_score(self):
        """Método para desenhar o placar."""
        self.write(
            f'{self.score_a} x {self.score_b}',
            align='center',
            font=('Arial', 30, 'normal'),
        )

    def update_score(self, ball: Ball):
        """Método para atualizar o placar.

        Se a bola colidir com as paredes laterais, o placar é atualizado.

        :param ball: classe Ball
        :type ball: Ball
        """
        if ball.xcor() > 350 or ball.xcor() < -350:
            if ball.xcor() > 350:
                self.score_a += 1
            elif ball.xcor() < -350:
                self.score_b += 1
            self.clear()
            self.draw_score()
            ball.goto(0, 0)


def main():
    """Função principal."""
    window = turtle.Screen()
    # configuração da janela
    window.title('Pong Game')
    window.bgcolor('black')
    window.setup(width=800, height=600)
    window.tracer(0)

    # criação dos objetos
    play_a = Player(-350)
    play_b = Player(350)
    ball = Ball(0)
    score = Score(260)

    # metodo para 'escutar' os eventos de teclado
    window.listen()
    # teclas para movimentar o jogador A
    window.onkeypress(play_a.up, 'w')
    window.onkeypress(play_a.down, 's')
    # teclas para movimentar o jogador B
    window.onkeypress(play_b.up, 'Up')
    window.onkeypress(play_b.down, 'Down')

    # loop para atualizar a tela
    while True:
        # método da classe Turtle, que atualiza a janela
        window.update()
        # método da classe Ball que atualiza a posição da bola
        ball.update(play_a, play_b)
        # método da classe Score que atualiza o placar
        score.update_score(ball)


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
