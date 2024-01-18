from sys import displayhook
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

def column_unification(df):

    """
    Function that remove spaces from rows
    and
    lowercase and replace spaces with _
    in the columns names
    
    """

    #Remove spaces from rows
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    #Lowercase and spaces with _
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]

    return df

# Heatmap
def plot_corr(df, fuente):

    """
    Función de clase   
    
    """

    plt.plot(figsize=(15, 10))   

    sns.set(style='white')   

    mask=np.triu(np.ones_like(df.corr(numeric_only=True), dtype=bool))    # mascara para tapar lo de arriba

    cmap=sns.diverging_palette(0, 10, as_cmap=True)   # paleta de  colores


    ax =sns.heatmap(df.corr(numeric_only=True),    
            mask=mask,
            cmap=cmap,
            center=0,
            square=True,
            annot=True,
            annot_kws={'size': fuente},  # Ajusta el tamaño del texto de annot
            linewidths=0.5,
            cbar_kws={'shrink': 0.5});
    
    # Ajusta el tamaño de la fuente de los ejes x e y
    ax.tick_params(axis='x', labelsize=fuente)
    ax.tick_params(axis='y', labelsize=fuente)

    plt.show()
