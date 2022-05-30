# Estudo de programação orientada a objetos

## Índice

<p align="center">
<a href="#conteúdo">Conteúdo</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#códigos-de-exemplo">Códigos de exemplo</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="#referências">Referências</a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>

---

## Conteúdo

* O que é uma classe?

  O objetivo primordial da POO foi, e é, organizar e evitar repetições de
  trechos de código em um programa. Sempre que houver repetições, analise esta
  premissa.

  Uma classe é um bloco de código que contém várias funções. Porque eles estão
  localizados dentro de uma classe eles são chamados métodos, mas significam a
  mesma coisa. Além disso, as variáveis armazenadas dentro de uma classe são
  chamadas
  atributos.

  O objetivo de uma classe é chamá-la mais tarde, permitindo a você
  acessar/utilizar os métodos (ou funções) quantas vezes forem necessárias.

[🔝](#índice)

* O que é um objeto?

  Sempre que precisamos criar “algo” com base em uma classe, dizemos que
  estamos
  “instanciando objetos”.
  O ato de instanciar um objeto significa que estamos criando a representação
  de
  uma classe em nosso programa.

[🔝](#índice)

* O que é um método?

  Um método é uma função que está dentro de uma classe.

[🔝](#índice)

* O que é método de classe?

  Um método de classe é um método chamado diretamente pelo nome da classe.

  É aquele que pertence à classe como um todo. Não requer uma instância. Em vez
  disso, a classe será enviada automaticamente como o primeiro argumento.

  O método de classe é declarado com o decorador @classmethod.

      class Foo:
        @classmethod
        def hello(cls):
            print(f'Hello from {cls.__name__}.')

      Foo.hello() # Hello from Foo.

[🔝](#índice)

* O que é método de instância?

  São funções chamadas pelo objeto instanciado.

      class Foo:
        def hello(self):
            print(f'Hello from {self.__class__.__name__}.')

      foo = Foo()
      foo.hello() # Hello from Foo.

      Foo.hello() # TypeError: Foo.hello() missing 1 required positional argument: 'self'

[🔝](#índice)

* O que é método estático?

  Um método estático pertence a uma classe; ainda assim, não está vinculado ao
  objeto dessa classe.
  Assim, ele pode ser chamado sem criar uma instância da classe em que reside.

  Como os métodos estáticos não estão vinculados a um objeto, ele não conhece
  as propriedades de uma classe,
  portanto não pode acessar ou modificar as propriedades da classe.

      class Foo:
        @staticmethod
        def hello():
            print('Hello from Foo.')
        
      Foo.hello() # Hello from Foo.

      foo = Foo()
      foo.hello() # Hello from Foo.

[🔝](#índice)

* O que são os métodos Getter e Setter?

  Os métodos Getter e Setter são métodos que permitem acessar e modificar os
  atributos de um objeto, mas sem alterar o valor do atributo.

  Funciona como se fosse um filtro, ou seja, o valor do atributo é passado
  para o método, e o método retorna o valor modificado. O atributo chamado não
  é alterado.

  O método Getter é o método chamado para obter o valor de um atributo.
  O método Setter é o método chamado para modificar o valor de um atributo.

  O método Getter é declarado com o decorador @property.
  O método Setter é declarado com o decorador @property.setter.

      class Foo:
        def __init__(self):
            self.bar = 'Hello World'

        @property
        def bar(self):
            """Retorna a propriedade bar"""
            return self._bar
    
        @bar.setter
        def bar(self, value):
            """Define a propriedade bar"""
            self._bar = value

        def __str__(self):
            """Retorna a string representando o objeto"""
            return self.bar
    
      foo = Foo()
      print(foo) # Hello World

      foo.bar = 'Hello'
      print(foo.bar) # Hello

      foo.bar = 'World'
      print(foo.bar) # World

      print(str(Foo())) # Hello World

* O que é um atributo?

  São variáveis que armazenam valores para serem usadas em outras funções.

[🔝](#índice)

* O que é Encapsulamento?

  O encapsulamento é o processo de encapsular as propriedades de um objeto,
  para que elas não sejam acessadas diretamente (public, private, protected).

  Em Python, é possível acessar as propriedades de um objeto,
  mas não se deve modificá-las por convenção.

  O encapsulamento é sinalizado com a convenção de ' _' ou ' __ ' antes do nome do atributo.
  Onde ' _ ' é usado para sinalizar que o atributo é 'privado', e '__' é usado para sinalizar que o atributo é 'protegido'.

  Na verdade, o interpretador Python não sabe se o atributo é 'privado' ou 'protegido'. 
  Esta convenção é usada para o programador Python.

  Os métodos Getter e Setter podem ser usados para encapsular os atributos.

      class Funcionario:
          def __init__(self, nome, cargo, valor_hora_trabalhada):
              self.nome = nome
              self.cargo = cargo
              self.valor_hora_trabalhada = valor_hora_trabalhada
              self.__salario = 0
              self.__horas_trabalhadas = 0

          @property
          def salario(self): 
             return self.__salario

          @salario.setter
          def salario(self, novo_salario): 
              raise ValueError('Impossivel alterar salario diretamente. Use a funcao calcula_salario().')

          def registra_hora_trabalhada(self):
              self.__horas_trabalhadas += 1

          def calcula_salario(self):
              self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

      pedro = Funcionario('Pedro', 'Gerente de Vendas', 50)
      pedro.salario = 100000 # ValueError: Impossivel alterar salario diretamente. Use a funcao calcula_salario()

[🔝](#índice)
  
* O que é relação entre classes?
  
  É a forma de agrupar objetos de forma que eles possam ser manipulados na totalidade.

  As formas de relacionar objetos são:
    - Associação (Um objeto **USA** outro objeto). Símbolo: '->'.
    - Agregação (Objeto **TEM** o outro(s) objeto). Símbolo: '-<>'.
    - Composição (Objeto **É DONO** do outro(s) objeto). Símbolo: '-<*>'.
    - Herança (O objeto **É** o outro objeto). Símbolo: '-*>'.

[🔝](#índice)

* O que é Associação? (Um objeto **USA** outro objeto) Símbolo: '->'.

  As classes são independentes, mas podem ser associadas entre si.

  O exemplo abaixo demonstra a forma de associação:

        class Escritor:
            def __init__(self, nome):
                self.__nome = nome
                self.__ferramenta = None # elemento de associação

            @property
            def nome(self):
                return self.__nome
          
            @property
            def ferramenta(self):
                return self.__ferramenta

            @ferramenta.setter
            def ferramenta(self, ferramenta):
                self.__ferramenta = ferramenta

        class Caneta:
            def __init__(self, marca):
                self.__marca = marca

            @property
            def marca(self):
                return self.__marca
  
            def escrever(self):
                print(f'Estou escrevendo com a caneta {self.__marca}')

        class MaquinaEscrever:
            def escrever(self):
                print('Estou escrevendo com a máquina de escrever')

        escritor = Escritor('Pedro')
        caneta = Caneta('Bic')
        maquina = MaquinaEscrever()
  
        escritor.ferramenta = caneta
        escritor.ferramenta.escrever() # Estou escrevendo com a caneta Bic

        escritor.ferramenta = maquina
        escritor.ferramenta.escrever() # Estou escrevendo com a máquina de escrever

[🔝](#índice)

* O que é Agregação? (Objeto **TEM** o outro(s) objeto) Símbolo: '-<>'.
  
  As classes podem existir independentes, mas podem ser agregadas entre si.

  Ex.: um carro existir sem as rodas e as rodas existem sem o carro. 
  Porém, um caro não se locomove sem as rodas.

  O exemplo abaixo demonstra a forma de agregação:

        class CarrinhoDeCompras:
            def __init__(self):
                self.produtos = []

            def inserir_produto(self, produto): # agregação
                self.produtos.append(produto)

            def listar_produtos(self):
                for produto in self.produtos:
                    print(produto.nome, produto.preco)

            def soma_total(self):
                total = 0
                for produto in self.produtos:
                    total += produto.preco
                return total

        class Produto:
            def __init__(self, nome, preco):
                self.nome = nome
                self.preco = preco

        carrinho = CarrinhoDeCompras()
        p1 = Produto('Notebook', 2000)
        p2 = Produto('Mouse', 10)
        p3 = Produto('Teclado', 20)
  
        carrinho.inserir_produto(p1) # agregação
        carrinho.inserir_produto(p2) # agregação
        carrinho.inserir_produto(p3) # agregação

        carrinho.listar_produtos()
        print(carrinho.soma_total())

[🔝](#índice)

* O que é Composição? (Objeto **É DONO** do outro(s) objeto) Símbolo: '-<*>'.

  É quando uma classe está contida em outra.

  Ex.: um carro é composto por uma parte de motor e uma parte de rodas.
  Um carro não se locomove sem o motor e nem as rodas.

      class Cliente:
          def __init__(self, nome, idade):
              self.nome = nome
              self.idade = idade
              self.enderecos = []

          def inserir_endereco(self, cidade, estado):
              self.enderecos.append(Endereco(cidade, estado))  # composição
        
          def listar_enderecos(self):
              for endereco in self.enderecos:
                  print(endereco.cidade, endereco.estado)
        
          def __del__(self):
              print(f'Objeto {self.nome} foi apagado.')


       class Endereco:
           def __init__(self, cidade, estado):
               self.cidade = cidade
               self.estado = estado
       
           def __del__(self):
               print(f'Objeto {self.cidade}/{self.estado} foi apagado.')

       cliente1 = Cliente('João', 30)
       cliente1.inserir_endereco('São Paulo', 'SP')
       print(cliente1.nome)
       cliente1.listar_enderecos()
       print()
   
       cliente2 = Cliente('Maria', 25)
       cliente2.inserir_endereco('Taubaté', 'SP')
       print(cliente2.nome)
       cliente2.listar_enderecos()
       print()
   
       cliente3 = Cliente('Pedro', 35)
       cliente3.inserir_endereco('Brasília', 'DF')
       print(cliente3.nome)
       cliente3.listar_enderecos()
       print()
   
       print(' Fim do programa. '.center(50, '='))

[🔝](#índice)

* O que é Polimorfismo?

    Apresenta multiplas formas de fazer uma mesma coisa.

    Tipos:

  - Paramétrico (parametrizado - generics)

  - Sobrecarga de métodos (sobrecarrega - overloading)

  - Sobrescrita de métodos (sobrescrita - overriding)


  * Polimorfismo Paramétrico (generics)

    É quando um método tem diferentes comportamentos para diferentes tipos 
    de dados.
  
    O método pode receber como parâmetro ora uma ‘string’, ora um int, ora um float, ora uma list, ora um dict, etc., 
    ou seja, o método pode ser parametrizado com tipos diferentes de dados.

  * Polimorfismo de sobrecarga de métodos (overloading)

    É quando um método tem a mesma assinatura, mas diferentes implementações.

        def soma(x, y):
            return x + y
        def soma(x, y, z):
            return x + y + z
        def multiplica(x: int, y: int) -> int:
            return x * y
        def multiplica(x: float, y: float) -> float:
            return x * y
        def multiplica(x: int, y: float) -> float:
            return x * y
        def multiplica(Complex, Complex) -> Complex:
            return Complex * Complex
        def multiplica(list, list) -> list:
            return list + list

    O método pode ter diferentes implementações, mas a assinatura é a mesma.


  * Polimorfismo de sobrescrita de métodos (overriding)

    É quando um método tem a mesma assinatura e mesmo comportamento, mas diferentes implementações.
  
    O método da classe pai é substituído, sobrescrito, pelo método da classe filha de mesmo nome.

    e.g. uma classe pai tem um método que retorna um valor inteiro, e uma classe filha tem o mesmo método que retorna um valor float.


      from abc import ABC, abstractmethod
      
      
      class Empregado(ABC):
      
          @abstractmethod
          def pagamento_do_mes(self):
              raise NotImplementedError(
                  'Subclasses precisam implementar o método pagamento_do_mes()'
              )
      
      
      class EmpregadoHorista(Empregado):
          def __init__(self, valor_da_hora, horas_trabalhadas):
              super().__init__()
              self.valor_da_hora = valor_da_hora
              self.horas_trabalhadas = horas_trabalhadas
      
          def pagamento_do_mes(self):
              return self.valor_da_hora * self.horas_trabalhadas
      
          def __str__(self):
              return f'Empregado horista: ' \
                     f'R$ {self.valor_da_hora:.2f} * {self.horas_trabalhadas} h = ' \
                     f'R$ {self.pagamento_do_mes():.2f}\n'
      
      
      class EmpregadoMensalista(Empregado):
          def __init__(self, salario, encargos):
              super().__init__()
              self.salario_mensal = salario
              self.taxa_encargos_trabalhistas = encargos
      
          def pagamento_do_mes(self):
              return self.salario_mensal * self.taxa_encargos_trabalhistas
      
          def __str__(self):
              return f'Empregado mensalista: ' \
                     f'R$ {self.salario_mensal:.2f} * {self.taxa_encargos_trabalhistas} = ' \
                     f'R$ {self.pagamento_do_mes():.2f}\n'
      
      
      class EmpregadoAvulso(Empregado):
          def __init__(self, pagamento):
              super().__init__()
              self.pagamento = pagamento
      
          def pagamento_do_mes(self):
              return self.pagamento
      
          def __str__(self):
              return f'Empregado avulso: R$ {self.pagamento:.2f}\n'
      
      
      def main():
          """Função principal."""
          joao = EmpregadoHorista(valor_da_hora=100, horas_trabalhadas=30)
          maria = EmpregadoMensalista(salario=5000, encargos=1.8)
          pedro = EmpregadoAvulso(pagamento=7000)
      
          print(joao, maria, pedro, sep='\n', end='\n\n')
          print(f'Total de custo: R$ {joao.pagamento_do_mes() + maria.pagamento_do_mes() + pedro.pagamento_do_mes():.2f}')  # polimorfismo

[🔝](#índice)

* O que é herança? (O objeto **É** o outro objeto) Símbolo: '-*>'.

    É quando uma classe herda de outra.

    Ex.: uma Pessoa é uma pessoa física, uma pessoa jurídica e uma pessoa física é um pessoa.

        class Pessoa:
            def __init__(self, nome, idade):
                self.nome = nome
                self.idade = idade 

            def __str__(self):
                return f'{self.nome} - {self.idade}'

        class PessoaFisica(Pessoa):
            def __init__(self, nome, idade, cpf):
                super().__init__(nome, idade)
                self.cpf = cpf

            def __str__(self):
                return f'{self.nome} - {self.idade} - {self.cpf}'

        class PessoaJuridica(Pessoa):
            def __init__(self, nome, idade, cnpj):
                super().__init__(nome, idade)
                self.cnpj = cnpj

            def __str__(self):
                return f'{self.nome} - {self.idade} - {self.cnpj}'

        p1 = Pessoa('João', 30)
        print(p1)
        print()

        p2 = PessoaFisica('Maria', 25, '123.456.789-00')
        print(p2)
        print()

        p3 = PessoaJuridica('Pedro', 35, '123.456.789/0001-00')
        print(p3)
        print()

        print(' Fim do programa. '.center(50, '='))

[🔝](#índice)

## Códigos de exemplo

* [Herança](heranca.py)
* [Pong Game](pong.py)
* [QR Code](qr_code_encoder_decoder)
* [Informações Meteorológicas](informacoes_meteorologicas)

[🔝](#índice)

## Referências

* [Código do Estagiário](https://www.youtube.com/watch?v=cTeR3ATHpZo)
* [Princípios de Algoritmos e Estruturas de Dados Usando Python](https://panda.ime.usp.br/algoritmos/static/algoritmos/index.html)
* [Python: O Guia do Programador](https://docs.python.org/pt-br/3/tutorial/classes.html)
* [Laboratório de Programação Orientada a Objetos](https://www.coursera.org/learn/lab-poo-parte-1)
* [Python Orientado a Objetos - Python POO](https://www.youtube.com/playlist?list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7)
* [Introdução à Ciência da Computação com Java e Orientação a Objetos](https://ccsl.ime.usp.br/files/publications/files/2008/intro-java-cc.pdf)

[🔝](#índice)