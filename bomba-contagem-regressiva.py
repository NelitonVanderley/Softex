import time
tempo = int(input('Informe o tempo para a contagem regressiva: '))
def contagem_regressiva(tempo):
  print('\n\nAtenção! \nIniciando contagem regressiva... ')
  time.sleep(1)
  for i in range(tempo, -1, -1):
    if i == 0:
      print("Buuum!!!!  \nA bomba explodiu!!!!") 
      break
    print(i)
    time.sleep(1)
contagem_regressiva(tempo)

#Realiza a contagem regressiva para a explosão de uma bomba!