'''
- implemente uma classe abstrata Veículo com um construtor padrão e os métodos clone e represent;
- o construtor da classe Veículo deve receber modelo, marca, cor e numeroRodas como parâmetros;
- crie pelo menos duas subclasses da classe Veículo, que acrescentem um ou mais atributos, por exemplo: 
carro que tem dois campos a mais, como numeroRodas e numeroPortas;
- desenvolva uma classe Aplicação que deve criar um array com seis veículos com dois tipos de veículos diferentes 
(subclasses), utilizando o método clone dos objetos para preencher o array;
- na classe Aplicação, implemente um método que retorne um array com o mesmo tamanho do array de veículos, onde cada 
elemento deve ser um clone dos elementos do array veículos;
- no final, deve imprimir na tela o retorno da função represent de cada elemento desse novo array de clones de veículos.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para 
que outros desenvolvedores possam analisá-lo.'''

from abc import ABC, abstractmethod;
from pprint import pprint
import copy


class Veiculo(ABC): 
  @abstractmethod
  def __init__(self):
    self.modelo = None
    self.marca = None
    self.cor = None
    self.num_rodas = None
    
  def clone(self):
    return copy.copy(self)
  
  def represent(self): 
    return None

class Carro (Veiculo):

  def __init__ (self, modelo, marca, cor, num_rodas):
      self.modelo = modelo   
      self.marca = marca
      self.cor = cor
      self.num_rodas = num_rodas


  def clone (self):
    return copy.copy(self)
    
  def represent(self): 
      self.velocidade_max = '200km'
      self.num_portas = 4
      return self.velocidade_max, self.num_portas
    
class Moto (Veiculo):

  def __init__(self, modelo, marca, cor, num_rodas):   
    self.modelo = modelo   
    self.marca = marca
    self.cor = cor
    self.num_rodas = num_rodas

  def clone (self):
    return copy.copy(self)

  def represent(self): 
    self.velocidade_max = '120km'
    self.num_portas = 0
    return self.velocidade_max, self.num_portas

class Aplicacao (Veiculo):
   
  veiculo1 = Carro('Palio', 'Fiat', 'preto', 4).clone()
  veiculo2 = Carro('Uno', 'Fiat', 'verde', 4).clone()
  veiculo3 = Carro('Onix', 'Chevrolet', 'branco', 4).clone()
  veiculo4 = Moto('Titan', 'Honda', 'branca', 2).clone()
  veiculo5 = Moto('Fan', 'Honda', 'vermelha', 2).clone()
  veiculo6 = Moto('Factor', 'Yamaha', 'preta', 2).clone()

  global array_veiculos 
  array_veiculos = [veiculo1, veiculo2, veiculo3, veiculo4, veiculo5, veiculo6]

  def clone_array():
    nova_array = []

    for elemento in array_veiculos:
      nova_array.append(elemento.clone())

    for i in nova_array:
      pprint(vars(i))
      print(i.represent())

Aplicacao.clone_array()

