#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head(10)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[5]:



result = black_friday.shape
def q1():   
    # Retorne aqui o resultado da questão 1.
    return result
    pass 
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[29]:



genero = (black_friday['Gender']=="F") & (black_friday['Age']=="26-35")
qtd_m = black_friday[genero].shape[0]

def q2():
    # Retorne aqui o resultado da questão 2.
    return qtd_m
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[41]:


qtd_u = len(black_friday.User_ID.unique())

def q3():
    # Retorne aqui o resultado da questão 3.
    return qtd_u
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[68]:



qtd_d = int(len(black_friday.dtypes.unique()))

#qtd_d = len(info.dtypes)

def q4():
   # Retorne aqui o resultado da questão 4.
   return qtd_d
   pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[70]:


porcentagem_null = (black_friday.shape[0] - black_friday.dropna().shape[0])/ black_friday.shape[0]

def q5():
    # Retorne aqui o resultado da questão 5.
    return porcentagem_null
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[94]:



sum = int((black_friday.isna().sum()[black_friday.isna().sum()>0]).max())

def q6():
    # Retorne aqui o resultado da questão 6.
    return sum
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[76]:


qtd_not_null = int(black_friday['Product_Category_3'].dropna().mode())

def q7():
    # Retorne aqui o resultado da questão 7.
    return qtd_not_null
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[136]:



import numpy as np

n = black_friday['Purchase'] 
max_value = black_friday['Purchase'].max() 
min_value = black_friday['Purchase'].min()

norm = (n - min_value)/(max_value  - min_value) 

media_p = np.mean(norm)
media_p


def q8():
    # Retorne aqui o resultado da questão 8.
    return float(media_p)
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[100]:


pad =pd.DataFrame()
media = black_friday['Purchase'].mean()
std = black_friday['Purchase'].std()
pad = (black_friday['Purchase'] - media)/std

qtd_oco = int(((pad<1) & (pad>-1)).sum()) 

def q9():
    # Retorne aqui o resultado da questão 9.
    return qtd_oco
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[90]:


null =  black_friday[['Product_Category_2', 'Product_Category_3']].isna()
resultado = null.loc[(null['Product_Category_2']==True) & (null['Product_Category_3']==True)].sum()
resultado

def q10():
    # Retorne aqui o resultado da questão 10.
    return True
    pass


# In[ ]:




