# importando as bibliotecas da parte de criaçao do dataframe
import pandas as pd
import numpy as np
from faker import Faker
import random
fake = Faker('pt_BR')
# %% Creating

num_registros = 100 # determinando quantidade de linhas

# criando os ids entre 1 a 101 utilizando formataçao e zfill(5) - valor numerico de 5 casas que serão completadas por 0 se forem indefinidas
delivery_ids = [f'DEL{str(i).zfill(5)}' for i in range(1, num_registros + 1)]
order_ids = [f'ORD{str(i).zfill(5)}' for i in range(1, num_registros + 1)]
client_ids = [f'CLI{str(i).zfill(5)}' for i in range(1, num_registros + 1)]

# criando os nomes das companhias e tipo de cliente por fake e random
company_names = [fake.company()  for _ in range(num_registros)]
customer_types = [random.choice(['Pessoa Física', 'Pessoa Jurídica']) for _ in range(num_registros)]
# %%

# criando o dataframe e nomeando as colunas
df = pd.DataFrame({'delivery_id':delivery_ids,
                   'order_id':order_ids,
                   'client_id':client_ids,
                   'company_name':company_names,
                   'customer_type':customer_types})
# %%

estados = { # criando a coluna dos estados
    'SP': 'Sudeste',
    'RJ': 'Sudeste',
    'MG': 'Sudeste',
    'ES': 'Sudeste',
    'BA': 'Nordeste',
    'PE': 'Nordeste',
    'CE': 'Nordeste',
    'PI': 'Nordeste',
    'MA': 'Nordeste',   
    'RN': 'Nordeste',
    'PB': 'Nordeste',
    'AL': 'Nordeste',
    'SE': 'Nordeste',
    'RS': 'Sul',
    'SC': 'Sul',
    'PR': 'Sul',
    'AM': 'Norte',
    'PA': 'Norte',
    'AC': 'Norte',
    'TO': 'Norte',
    'AP': 'Norte',
    'RO': 'Norte',
    'RR': 'Norte',
    'MT': 'Centro-Oeste',
    'GO': 'Centro-Oeste',
    'DF': 'Centro-Oeste'
}

# listas
cities = []
states = []
regions = []

# preenchendo as linhas com cidades, estados e regioes aleatorias
for _ in range(num_registros): 
    estado = random.choice(list(estados.keys()))
    cidade = fake.city()
    regiao = estados[estado]
    
    # append add itens na lista um por um na iteraçao
    cities.append(cidade)
    states.append(estado)
    regions.append(regiao)

# add no dataframe
df['city'] = cities
df['state'] = states
df['region'] = regions
# %%

from datetime import timedelta

order_dates = []
delivery_dates = []
delivery_status = []
product_quantities = []
product_weights = []
shipping_modes = []
freight_values = []
product_values = []

# opcoes de status e transporte
status_options = [
    'Entregue', 'Atrasada', 'Em andamento'
    ]
shipping_options = [
    'Rodoviário', 'Aéreo', 'Ferroviário', 'Marítimo'
    ]

# gerando dados ficticios p cada linha
for _ in range(num_registros):
    order_date = fake.date_between(start_date='-1y', end_date='today') # data ficticia dos ultimos 365 dias
    delivery_days = random.randint(1, 15) # intervalo aleatorio de entrega entre 1 e 15 dias
    delivery_date = order_date + timedelta(days=delivery_days) # calculando a data de entrega
    
    status = random.choices(status_options, weights=[0.7, 0.15, 0.15], k=1)[0]
    quantity = random.randint(1, 100)
    weight = round(random.uniform(0.5, 100.0), 2)
    shipping = random.choice(shipping_options)
    product_value = round(random.uniform(100, 10000), 2)
    freight = round(5 + (weight * random.uniform(0.1, 0.3)), 2)
    freight = min(freight, 35.0)

    order_dates.append(order_date)
    delivery_dates.append(delivery_date)
    delivery_status.append(status)
    product_quantities.append(quantity)
    product_weights.append(weight)
    shipping_modes.append(shipping)
    product_values.append(product_value)
    freight_values.append(freight)

df['order_date'] = order_dates
df['delivery_date'] = delivery_dates
df['delivery_status'] = delivery_status
df['product_quantity'] = product_quantities
df['product_weight_kg'] = product_weights
df['shipping_mode'] = shipping_modes
df['product_value'] = product_values
df['freight_value'] = freight_values
# %%

payment_methods = ['Cartão de Crédito',
                   'Cartão de débito',
                   'Boleto',
                   'Pix',
                   'Transferência'
                   ]

payment_method = []
customer_feedback = []
has_tracking_code = []

for _ in range(num_registros):
    method = random.choice(payment_methods)
    feedback = random.randint(1,5)
    tracking = random.choices([True, False], weights=[0.95,0.05])[0]
    
    payment_method.append(method)
    customer_feedback.append(feedback)
    has_tracking_code.append(tracking)
    
df['payment_method'] = payment_method
df['customer_feedback'] = customer_feedback
df['has_tracking_code'] = has_tracking_code
# %% Analyzing
# importando as bibliotecas
import matplotlib.pyplot as plt
import seaborn as sbn

# %%

print(df.head()) # 5 primeiras linhas do dataframe
print(df.info()) # infos gerais do dataframe
print(df.describe().T) # estatisticas descritivas - linhas como colunas
for col in df.columns:
    print(f'{col}: {df[col].nunique()} valores únicos') # numero de valores unicos por coluna
# %%

df['order_date'] = pd.to_datetime(df['order_date']) # alterando o tipo da variavel pra data
df['delivery_date'] = pd.to_datetime(df['delivery_date']) # alterando o tipo da variavel pra data
df['delivery_time_days'] = (df['delivery_date'] - df['order_date']).dt.days # criando um objeto pro tempo de entrega

df['order_month'] = df['order_date'].dt.month # extraindo o mes do pedido
df['order_weekday'] = df['order_date'].dt.day_name() # extraindo o dia da semana do pedido

df.loc[df['delivery_status'] == 'Em andamento', 'delivery_time_days'] = np.nan # atribuindo valores NaN na coluna delivery_time_days para todas as linhas que estão com o pedido em andamento no status
tempo_medio_regiao = df.groupby('region')['delivery_time_days'].mean().sort_values() # media do tempo de entrega por regiao, agrupando

plt.figure(figsize=(14,8)) # define o tamanho do grafico
sbn.barplot (
    x=tempo_medio_regiao.values, # valores medios eixo x
    y=tempo_medio_regiao.index, # regioes eixo y
    palette='viridis' # paleta de cores 
    )

for i, value in enumerate(tempo_medio_regiao.values): # add os valores reais nas barras
    plt.text( # add texto ao lado das barras
        value + 0.1, # posicao x levemente a frente da barra
        i, # posicao y (indice da barra)
        f'{value:.1f} dias', # formatando o texto com 1 casa decimal
        va='center', # posicionando verticalmente no centro da barra
        fontsize=11, # tamanho da fonte 
        color='black' # cor
        )

plt.title('Tempo Médio de Entrega por Região',fontsize=18) # titulo
plt.xlabel('Dias (média)',fontsize=14) # subtitulo eixo x
plt.ylabel('Região',fontsize=14) # subtitulo eixo y
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5) # grade do tipo linha com 0.5 de largura e 0.4 de transparencia (entre 0 e 1)
plt.tight_layout() # ajusta o padding entre o titulo, rotulos e eixos
plt.show() # mostra o grafico

# %%

sbn.set_style("white")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
# padronizando os graficos que serão gerados estilo visual e tamanho do grafico, titulo, nomes eixo x e y e valores no eixo

numeric_cols = ['product_quantity', 'product_weight_kg', 'product_value', 'freight_value']
nomes_formatados = {
    'product_quantity': 'Quantidade de Produtos',
    'product_weight_kg': 'Peso do Produto (kg)',
    'product_value': 'Valor do Produto (R$)',
    'freight_value': 'Valor do Frete (R$)'
} # criação de 2 objetos: 1 pra cada nome da coluna e outro atribuindo as colunas com nomes pt-br

for col in numeric_cols: # inicia o loop pra gerar um grafico pra cada nome das colunas listadas
    plt.figure() # cria uma nova figura pra cada iteração
    sbn.histplot( # histograma, grafico que cria barras c base num valor numerico continuo
        data=df, # escolha do dataframe
        x=col, # escolha do eixo x
        bins=30, # quantidade de "barras"
        kde=True, # add a linha de intensidade
        color="#4c72b0", # cor
        alpha=0.8 # transparencia quase 100% (=1)
    )
    plt.title(f'Distribuição de {nomes_formatados[col]}') # da o titulo com a versao formatada dos nomes das colunas
    plt.xlabel(nomes_formatados[col]) 
    plt.ylabel('Frequência') 
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.4) 
    sbn.despine() # remove a borda superior e da direita
    plt.tight_layout() 
    plt.show() 
# %%
    
customer_counts = df['customer_type'].value_counts() # conta qts clientes por tipo

plt.figure(figsize=(6,6))
plt.pie(customer_counts, # grafico do tipo torta fatiada com o counts
        labels=customer_counts.index, # rotulos das fatias
        autopct='%1.1f%%', # # mostra a porcentagem com 1 casa decimal dentro de cada fatia
        startangle=90, # angulo inicial do grafico
        colors=sbn.color_palette('viridis')
        )
plt.title('Proporção por Tipo de Cliente',fontsize=18)
plt.tight_layout()
plt.show()

shipping_counts = df['shipping_mode'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(shipping_counts,
        labels=shipping_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sbn.color_palette('viridis')
        )
plt.title('Distribuição dos Modos de Envio', fontsize=18)
plt.tight_layout()
plt.show()

payment_counts = df['payment_method'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(payment_counts,
        labels=payment_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sbn.color_palette('viridis')
        )
plt.title('Distribuição das Formas de Pagamento',fontsize=18)
plt.tight_layout()
plt.show()
# %%
feedback_labels = { # transformando os valores numericos em txt
    1: 'Péssimo',
    2: 'Ruim',
    3: 'Regular',
    4: 'Bom',
    5: 'Ótimo'
}

df['feedback_texto'] = df['customer_feedback'].map(feedback_labels) # criando uma nova coluna com txt
feedback_counts = df['feedback_texto'].value_counts(normalize=True).reindex(['Péssimo', 'Ruim', 'Regular', 'Bom', 'Ótimo']) * 100 # calcula a proporçao de cada feedback em %

plt.figure(figsize=(12,6))
sbn.barplot(x=feedback_counts.index, y=feedback_counts.values, palette='viridis') # grafico de barras c/ valores agregados (media, soma etc) de variaveis por categoria 
plt.title('Distribuição dos Feedbacks dos Clientes', fontsize=18)
plt.xlabel('Feedback', fontsize=14)
plt.ylabel('Proporção (%)', fontsize=14)
plt.tight_layout()
plt.show()
# %%

import plotly.express as px
import plotly.io as pio

fig_2d = px.scatter( # grafico de dispersao
    df,
    x='product_value',                      
    y='freight_value',                     
    color='region',                        # cor dos pontos por região
    size='product_weight_kg',              # tamanho das bolhas com base no peso do produto
    hover_data=['company_name', 'state', 'shipping_mode'],  # info extras ao passar o mouse
    title='Relação do Valor do Produto e Frete por Região',
    labels={
        'product_value':'Valor do Produto (R$)',
        'freight_value':'Valor do Frete (R$)',
        'region':'Região'
    },
    template='plotly_dark',                # dark mode
)

fig_2d.update_layout(
    title_font_size=20,
    legend_title='Região',                
    legend_font_size=14,                   
    height=650,                            # altura do grafico
    margin=dict(l=40, r=40, t=80, b=80),   # margem
)

import webbrowser

fig_2d.write_html("grafico_produto_frete.html")
webbrowser.open("grafico_produto_frete.html")  # abre automatici no navegador em HTML
# fig_2d.show()
# %%

import geopandas as gpd

file_path = "C:/Users/DELL/Desktop/projects/creating-n-analyzing/data/brazil-states.geojson" # acha o arquivo sem erro
gdf = gpd.read_file(file_path) # carrega o geojson com os estados

mapeamento_estado_sigla = { # mapeando o nome com as siglas
    'Acre': 'AC', 'Alagoas': 'AL', 'Amapá': 'AP', 'Amazonas': 'AM', 'Bahia': 'BA',
    'Ceará': 'CE', 'Espírito Santo': 'ES', 'Goiás': 'GO', 'Maranhão': 'MA', 'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS', 'Minas Gerais': 'MG', 'Pará': 'PA', 'Paraíba': 'PB',
    'Paraná': 'PR', 'Pernambuco': 'PE', 'Piauí': 'PI', 'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN', 'Rio Grande do Sul': 'RS', 'Rondônia': 'RO', 'Roraima': 'RR',
    'Santa Catarina': 'SC', 'São Paulo': 'SP', 'Sergipe': 'SE', 'Tocantins': 'TO',
    'Distrito Federal': 'DF'
}

gdf['sigla'] = gdf['name'].map(mapeamento_estado_sigla) # add a coluna sigla no gdf

df.columns = df.columns.str.strip() # remove espaços nas colunas, se houver
df['state'] = df['state'].astype(str).str.upper().str.strip()  # garante que a coluna esteja formatada corretamente

pedido_por_estado = df['state'].value_counts().rename('total_pedidos') # agrupa os pedidos por estado e renomeia a série

gdf = gdf.set_index('sigla') # define a sigla como indice do gdf

gdf = gdf.join(pedido_por_estado) # junta a contagem de pedidos com o gdf

fig, ax = plt.subplots(1, 1, figsize=(12, 8)) # cria a figura e os eixos

gdf.plot( # plota o mapa com base na coluna total_pedidos
    column='total_pedidos',
    ax=ax, cmap='Oranges',
    edgecolor='black',
    legend=True,
    legend_kwds={
        'label': "Número de Pedidos por Estado", 'orientation': "horizontal"
        }
    )

ax.set_title('Distribuição de Pedidos por Estado no Brasil', fontsize=20) # customiza o grafico
ax.set_axis_off()
plt.tight_layout()
plt.show()
# %%










































