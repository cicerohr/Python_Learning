# -*- coding: utf-8 -*-
r"""calculator.py in: 2022-05-06.

Python version: 3.10.0
"""
import tkinter as tk
from pathlib import Path

from tests.loguru_conf import logger

LARGE_FONT_STYLE = ('Arial', 40, 'bold')
SMALL_FONT_STYLE = ('Arial', 16)
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')
DEFAULT_FONT_STYLE = ('Arial', 20)
OFF_WHITE = '#F8FAFF'
WHITE_COLOR = '#FFFFFF'
LIGHT_BLUE = '#CCEDFF'
LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'


class Calculator:
    r"""Classe para criar uma calculadora."""

    def __init__(self):
        r"""Inicialização da classe.

        Caracteres ‘Unicode’ e a sequência de escape. (/, *, -, +)
        https://www.rapidtables.com/code/text/unicode-characters.html
        """
        self.window = tk.Tk()
        self.window.iconbitmap(
            f'{Path(__file__).parent.parent}\\assets\\calculator.ico'
        )
        self.window.title('Calculator')
        self.window.geometry('375x667')
        self.window.resizable(False, False)
        self.total_expression = ''
        self.current_expression = ''
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2),
            '.': (4, 1),
        }
        self.operations = {
            '/': '\u00F7',
            '*': '\u00D7',
            '-': '\u002D',
            '+': '\u002B',
        }
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        r"""Método para adicionar as teclas na operação."""
        self.window.bind('<Return>', lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(
                str(key),
                lambda event, value=key: self.add_to_expression(value),
            )

        for key in self.operations:
            self.window.bind(
                key, lambda event, value=key: self.add_to_expression(value)
            )

    def create_special_buttons(self):
        r"""Método para criar os botões especiais."""
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        r"""Método para criar os labels de display."""
        total_label = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor=tk.E,
            font=SMALL_FONT_STYLE,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
        )
        total_label.pack(expand=True, fill=tk.BOTH)

        label = tk.Label(
            self.display_frame,
            text=self.current_expression,
            anchor=tk.E,
            font=LARGE_FONT_STYLE,
            bg=LIGHT_GRAY,
            fg=LABEL_COLOR,
            padx=24,
        )
        label.pack(expand=True, fill=tk.BOTH)
        return total_label, label

    def create_display_frame(self):
        r"""Método para criar o frame de display."""
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    def add_to_expression(self, value):
        r"""Método para adicionar um valor à expressão."""
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        r"""Método para criar os botões dos dígitos."""
        for digit, grid_values in self.digits.items():
            button = tk.Button(
                self.buttons_frame,
                text=str(digit),
                font=DIGIT_FONT_STYLE,
                bg=WHITE_COLOR,
                fg=LABEL_COLOR,
                borderwidth=0,
                command=lambda value=digit: self.add_to_expression(value),
            )
            button.grid(
                row=grid_values[0], column=grid_values[1], sticky=tk.NSEW
            )

    def append_operator(self, operator):
        r"""Método para adicionar um operador à expressão."""
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        r"""Método para criar os botões de operações."""
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(
                self.buttons_frame,
                text=symbol,
                font=DEFAULT_FONT_STYLE,
                bg=OFF_WHITE,
                fg=LABEL_COLOR,
                borderwidth=0,
                command=lambda value=operator: self.append_operator(value),
            )
            button.grid(
                row=i,
                column=4,
                sticky=tk.NSEW,
            )
            i += 1

    def clear(self):
        r"""Método para limpar a expressão."""
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        r"""Método para criar o botão de limpar."""
        button = tk.Button(
            self.buttons_frame,
            text='C',
            font=DEFAULT_FONT_STYLE,
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            borderwidth=0,
            command=self.clear,
        )
        button.grid(
            row=0,
            column=1,
            sticky=tk.NSEW,
        )

    def square(self):
        r"""Método para calcular o quadrado de um número."""
        self.current_expression = str(eval(f'{self.current_expression}**2'))
        self.update_label()

    def create_square_button(self):
        r"""Método para criar o botão de quadrado de um número."""
        button = tk.Button(
            self.buttons_frame,
            text='x\u00B2',
            font=DEFAULT_FONT_STYLE,
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            borderwidth=0,
            command=self.square,
        )
        button.grid(
            row=0,
            column=2,
            sticky=tk.NSEW,
        )

    def sqrt(self):
        r"""Método para calcular a raiz quadrada de um número."""
        self.current_expression = str(eval(f'{self.current_expression}**0.5'))
        self.update_label()

    def create_sqrt_button(self):
        r"""Método para criar o botão raiz quadrada."""
        button = tk.Button(
            self.buttons_frame,
            text='\u221Ax',
            font=DEFAULT_FONT_STYLE,
            bg=OFF_WHITE,
            fg=LABEL_COLOR,
            borderwidth=0,
            command=self.sqrt,
        )
        button.grid(
            row=0,
            column=3,
            sticky=tk.NSEW,
        )

    def evaluate(self):
        r"""Método para calcular a expressão."""
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(f'{self.total_expression}'))
            self.total_expression = ''
        except Exception as e:
            logger.error(e)
            self.current_expression = 'Error'
        finally:
            self.update_label()

    def create_equals_button(self):
        r"""Método para criar o botão de igual."""
        button = tk.Button(
            self.buttons_frame,
            text='=',
            font=DEFAULT_FONT_STYLE,
            bg=LIGHT_BLUE,
            fg=LABEL_COLOR,
            borderwidth=0,
            command=self.evaluate,
        )
        button.grid(
            row=4,
            column=3,
            columnspan=2,
            sticky=tk.NSEW,
        )

    def create_buttons_frame(self):
        r"""Método para criar o frame de botões."""
        frame = tk.Frame(
            self.window, height=221, bg=LIGHT_GRAY
        )
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    def update_total_label(self):
        r"""Método para atualizar todas as labels."""
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        r"""Método para atualizar a label."""
        self.label.config(text=self.current_expression[:11])

    def run(self):
        r"""Método para iniciar a classe."""
        self.window.mainloop()


def main():
    """Função principal."""
    calc = Calculator()
    calc.run()


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
