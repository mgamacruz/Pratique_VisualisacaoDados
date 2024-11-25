import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

print(df.columns.tolist())

plt.figure(figsize=(15, 10))
plt.subplot(3, 3, 1)
plt.hist(df['Nota'], bins=100, color='green' , alpha=0.8)
plt.title('Quantidade de Vendas vs Avaliacao/Nota do produto')
plt.xlabel('Nota')
plt.xticks(ticks=range(0 , int(df['Nota'].max()), 1))
plt.ylabel('Qtd_Vendidos_Cod')
plt.grid(True)


plt.subplot(3, 3, 2)
plt.scatter(df['Nota'], df['Qtd_Vendidos_Cod'], color='#98FB98', alpha=0.6,s=30)
plt.title('Dipersao - Notas vs Quantidade de Vendas')
plt.xticks(ticks=range(0 , int(df['Nota'].max())+1, 1))
plt.xlabel('Nota')
plt.ylabel('Qtd_Vendidos_Cod')


# Mapa de Calor
plt.subplot(3, 3, 3)
corr = df[['Temporada_Cod','Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlacao Vendas por Temporada')

# Grafico de Barra
x1 = df['Desconto'].value_counts().index
y1 = df['Desconto'].value_counts().values

plt.subplot(3,3, 4)
plt.bar(x1, y1, color='#98FB98')
plt.title('Distribuicao de Desconto')
plt.xlabel('Desconto')
plt.ylabel('Quantidade')

# Grafico de Pizza
plt.subplot(3, 3, 5)
x2 = df['Temporada'].value_counts().index
y2 = df['Temporada'].value_counts().values
plt.pie(y2, labels=x2, autopct='%.1f%%', startangle=90)
plt.title('Representatividade de vendas vs Temporada')

# Grafico de Densidade
plt.subplot(3, 3, 6)
sns.kdeplot(df['Preço'], fill=True, color='#98FB98')
plt.title('Densidade de Preço')
plt.xlabel('Preço')

#Grafico de Regressão
plt.subplot(3,3,7)
sns.regplot(x='Preço', y='N_Avaliações', data=df, color='#98FB98', scatter_kws={'alpha':0.5, 'color': '#000000'})
plt.title('Regressão de N° de Avaliações vs Preço')
plt.xlabel('Preço')
plt.ylabel('N_Avaliações')

plt.tight_layout()
plt.show()
