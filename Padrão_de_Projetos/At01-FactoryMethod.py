from abc import ABC, abstractclassmethod ## Methodo para criar a interface

class Fabrica :
    def create_computer(self):
      pass
    def fabricacao(self) :
      computador = self.create_computer()
      result = (f"Computador: {computador.configuracao()}")

      return  result

class Fabrica_pc(Fabrica):
    def __init__(self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
        	  
    def create_computer(self):
     return Pc (str(self.ram), self.hd, self.cpu)

class Fabrica_server (Fabrica):
    def __init__(self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu

    def create_computer(self):
     return Server(self.ram, self.hd, self.cpu)
   
class Computador (ABC) : ##Informando que será uma interface
      @abstractclassmethod
      def configuracao(self):
        pass
    
class Pc (Computador):
    def __init__ (self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
      self.type = 'PC'
    def configuracao(self):
      result = (f"Configuração: RAM: {self.ram} GB, HD: {self.hd} GB, CPU: {self.cpu} GHZ, Tipo: {self.type}")
      return result

class Server (Computador):
    def __init__ (self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
      self.type = 'Server'
    def configuracao(self):
      result = (f"Configuração: RAM: {self.ram} GB, HD: {self.hd} GB, CPU: {self.cpu} GHZ, Tipo: {self.type}")
      return result
	

def requerimento (fabrica: Fabrica):
	print(f"Computador fabricado pela {fabrica.__class__.__name__}.", f"{fabrica.fabricacao()}")


def interacao_usuario():
	ram = int(input('Informe quantos GB de mémoria RAM o computador terá: '))
	hd = int(input('Informe quantos GB de HD o computador terá: '))
	cpu = int(input('Informe quantos GHz de CPU o computador terá: '))
	type = input('Informe quantos o tipo do computador (PC ou Server)? ')


	if type == 'PC':
		requerimento(Fabrica_pc(ram, hd, cpu))
	elif type == 'Server':
		requerimento(Fabrica_server(ram, hd, cpu))

interacao_usuario()