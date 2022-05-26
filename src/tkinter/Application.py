# -*- coding: utf-8 -*-
r"""Application.py in: 2022-05-18.

Interfaces gráficas em Python

@author: João
@modified by: Cícero
@link: https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
"""
import tkinter as tk

from tests.loguru_conf import logger


class MainApplication(tk.Frame):
    r"""MainApplication.

    Classe principal da aplicação.
    """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.bg_primary = '#48484A'
        self.bg_secondary = '#E3E3E3'
        self.color_primary = '#B7B7BD'
        self.color_secondary = '#929296'
        self.color_tertiary = '#656596'
        self.font_primary = ('Helvetica', 15, 'normal')
        self.font_secondary = ('Helvetica', 12, 'normal')
        self.font_tertiary = ('Helvetica', 10, 'normal')
        self.parent = parent
        self.parent.title('Informações Meteorológicas')
        self.parent.geometry('400x550')
        self.parent.configure(bg=self.bg_primary)
        self.parent.resizable(False, False)
        self.label_title = None
        self.entry_city = None
        self.button_search = None
        self.search_city = None
        self.create_widgets()

    def create_widgets(self):
        r"""create_widgets.
        
        Cria os widgets da aplicação.
        """
        self.label_title = tk.Label(
            self.parent, text='Clima Atual',
            bg=self.bg_primary, fg=self.color_primary,
            font=self.font_primary,
        )
        self.label_title.pack(fill=tk.X, padx=10, pady=10)

        self.entry_city = tk.Entry(
            self.parent, bg=self.bg_secondary,
            fg=self.color_tertiary,
            font=self.font_secondary,
            justify=tk.CENTER
        )
        self.entry_city.pack(fill=tk.X, padx=10, pady=10)
        self.entry_city.focus_set()
        self.entry_city.bind('<Return>', self.search_city)

        self.button_search = tk.Button(
            self.parent, text='Buscar',
            width=15,
            bg=self.bg_primary, fg=self.color_primary,
            activebackground=self.bg_secondary,
            activeforeground=self.color_secondary,
            border=0.5,
            font=self.font_secondary,
            command=self.search_city
        )
        self.button_search.pack(padx=10, pady=10)

        self.search_city = tk.Label(
            self.parent, text='Cidade/País | YYYY-MM-DD HH:MM | Fuso horário',
            bg=self.bg_primary, fg=self.color_primary,
            font=self.font_secondary
        )
        self.search_city.pack(fill=tk.X, padx=10, pady=10)


def main():
    r"""main.

    Função principal.
    """
    logger.debug('main')
    root = tk.Tk()
    MainApplication(root).pack(side='top', fill='both', expand=True)
    root.mainloop()


if __name__ == '__main__':
    logger.info('Início do programa.')
    main()
    logger.info('Fim do programa.')
