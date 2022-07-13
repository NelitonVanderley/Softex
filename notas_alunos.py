import pandas as pd

df = pd.read_csv('notas_alunos.csv', sep =';')
#print(df.to_string()) 
media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media

df.loc[df['faltas'] > 5, "situacao"] = "Reprovado" 
df.loc[df['media'] < 7, "situacao"] = "Reprovado" 
df.loc[df['situacao']!= "Reprovado", "situacao"] = "Aprovado" 

print(df)

print('Maior número de faltas é ' + str(df['faltas'].max()))
print('A média geral das notas é ' + str(df["media"].mean()))
print('Maior média é ' + str(df['media'].max()))

df.to_csv(r'c:\Users\nelit\Desktop\Softex\alunos_situacao.csv', index=False)
print(df["media"])