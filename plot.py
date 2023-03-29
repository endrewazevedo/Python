
# Pacotes
import numpy as np
import pandas as pd
import os
from plotnine import *
# mudan�a de diretorio
os.chdir("C:\GitHub\Python")

# Conjunto de dados
# argumento sep = ';' indica que as colunas s�o separadas por ponto e v�rgula
# argumento decimal = ',' indica que o separador decimal � v�rgula
df = pd.read_excel(r'C:\GitHub\Python\pokedex.xlsx')
# Mostrar parte do conjunto de dados
df.head()

""" # Gr�fico de barras
(ggplot(df, aes(x = 'regiao')) +
  geom_bar(fill = 'blue') +
  labs(x = 'Regiao', y = 'Frequencia') +
  theme(axis_title_x = element_text(size = 12),
    axis_title_y = element_text(size = 12),
    axis_text_x = element_text(size = 10),
    axis_text_y = element_text(size = 12)
  )
) """

""" # Histograma
# o argumento bins � a quantidade de intervalos
(ggplot(df, aes(x = 'Altura(m)')) +
  geom_histogram(bins = 6, color = 'white', fill = 'blue') +
  labs(x = 'Altura (m)', y = 'Frequencia')+
  theme(axis_title_x = element_text(size = 12),
    axis_title_y = element_text(size = 12),
    axis_text_x = element_text(size = 10),
    axis_text_y = element_text(size = 12)
  )
)

# Box-plot
(ggplot(df, aes(x = 0, y = 'altura')) +
  geom_boxplot() +
  labs(x = ' ', y = 'Altura (m)') +
  theme(axis_title_y = element_text(size = 12),
    axis_text_y = element_text(size = 12),
    axis_text_x = element_blank(),
    axis_ticks_major_x=element_blank()
  )
) """

""" # Box-plot por grupos
(ggplot(df, aes(x = 'type1', y = 'Altura(m)')) +
  geom_boxplot() +
  labs(x = 'Tipo', y = 'Altura (m)') +
  theme(axis_title_y = element_text(size = 12),
    axis_text_y = element_text(size = 12),
    axis_title_x = element_text(size = 12),
    axis_text_x = element_text(size = 10)
  )
) """

#print(df)

