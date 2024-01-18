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



#DATA CLEANING

def check_nan(df: pd.DataFrame) -> None:
    
    """ Función de Yona
    Recibe un dataframe y enseña el % de nulos y lo grafica
    """
            
    nan_cols = df.isna().mean() * 100  # % de valores nulos
            
    nan_cols = nan_cols[nan_cols>0]
            
    displayhook(f'N nan cols: {len(nan_cols)}')
    displayhook(nan_cols)

    # Crear subgráficos

def boxplots(rows, cols, size_x, size_y, df):

    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(size_x, size_y))

    # Aplanar la matriz de subgráficos
    axes = axes.flatten()

    # Iterar sobre las columnas y trazar boxplots
    for i, col in enumerate(df.columns):
        sns.boxplot(x=df[col], ax=axes[i])
        axes[i].set_title(f'Boxplot de {col}')
        axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=30)

    # Ajustar el diseño
    plt.tight_layout()
    plt.show()

def scaterplots_models(rows, cols, size_x, size_y, X, y, colors, cmap, name_X, name_y, titles):
    # Crear dos subgráficos
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # Subgráfico para 'labels'
    scatter_labels = axes[0].scatter(X, y, c=colors[0], cmap=cmap)
    axes[0].set_title(titles[0])
    axes[0].set_xlabel(name_X)
    axes[0].set_ylabel(name_y)

    # Subgráfico para 'labels_DBSCAN'
    scatter_dbscan = axes[1].scatter(X, y, c=colors[1], cmap=cmap)
    axes[1].set_title(titles[1])
    axes[1].set_xlabel(name_X)
    axes[1].set_ylabel(name_y)


    # Ajustar diseño y mostrar gráfico
    plt.tight_layout()
    plt.show();

    