class Eletronico:
	def __init__(self):
		self.ligado = False
	def ligar(self):
		self.ligado = True
	def desligar(self):
		self.ligado = False
	def situacao (self):
		return self.ligado

class Som (Eletronico):
	def __init__(self):
		Eletronico.__init__(self)
		self.volume = 0
	def aumentar_volume(self):
		self.volume = self.volume +1
	def diminuir_volume(self):
		if self.volume > 0: 
			self.volume = self.volume - 1
	def mute (self):
		self.volume = 0
	def obter_volume(self):
		return self.volume

	def aumentar_volume_dez_vezes(self):
		for i in range (0,10,1):
			self.aumentar_volume()

class Celular (Eletronico):
	def __init__(self):
		Eletronico.__init__(self)
		self.tocar = False
	def chamar (self):
		self.tocar = True
	def parar_tocar(self):
		self.tocar = False
	def tocando (self):
		return self.tocar

class Televisao (Eletronico):
	def __init__ (self):
		Eletronico.__init__(self)
		self.canal = 0
	def mudar_canal (self):
		self.canal = self.canal + 1	
	def saber_canal(self):
		return self.canal
	def mudar_canal_dez_vezes(self):
		for i in range (0,10,1):
			self.mudar_canal()


	
		


som = Som()
print(som.situacao())
som.ligar()
print(som.situacao())
print(som.obter_volume())
print(som.aumentar_volume_dez_vezes())
print(som.obter_volume())

tv = Televisao()
print(tv.situacao())
tv.ligar()
print(tv.situacao())
print(tv.saber_canal())		
tv.mudar_canal_dez_vezes()
print(tv.saber_canal())	

cel = Celular()
cel.chamar()
print(cel.tocando())

