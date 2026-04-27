import docx
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib as plt

#%%
doc = docx.Document('TheSirensOfTitan.docx')
libro = ""
for p in doc.paragraphs:
    libro += p.text.lower() + " "
palabras = libro.split()
libro_limpio = re.sub(r'[^a-z\s]', '', libro)
libro = " ".join(libro_limpio.split())
#%%
#df = pd.DataFrame(palabras, columns=['palabra'])
#df['palabra'] = df['palabra'].str.replace(r'[^a-z]', '', regex=True)
#conteo = df['palabra'].value_counts().reset_index()
#%%
stwrd = set(STOPWORDS)

nube = WordCloud(
    width=800, 
    height=400,
    background_color='white',
    stopwords=stwrd,
    colormap='viridis'
).generate(libro)

# 3. Guardar y mostrar el gráfico
# Siguiendo las reglas de tu entorno, usamos savefig
plt.imshow(nube, interpolation='bilinear')
plt.axis("off") # Para que no salgan los ejes de coordenadas
plt.tight_layout(pad=0)
plt.savefig('nube_palabras_tarea3.png')