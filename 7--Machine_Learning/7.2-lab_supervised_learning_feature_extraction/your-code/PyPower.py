from sys import displayhook
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt


# DATA CLEANING
def check_nan(df: pd.DataFrame) -> None:
    
    """ Función de Yona
    Recibe un dataframe y enseña el % de nulos y lo grafica
    """
    
    nan_cols = df.isna().mean() * 100  # % de valores nulos
    
    nan_cols = nan_cols[nan_cols>0]
    
    displayhook(f'N nan cols: {len(nan_cols)}')
    displayhook(nan_cols)



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



def rename_columns(df, dictio):
    """
    Function to change the name of the columns specified in the dictio param
    
    """    
    return df.rename(columns=dictio)


def replace_to(string, change_for, change_to):

    """
    Function that replace 'change_for' for 'change_to' in string

    It is usefull for the comma character in a  spanish float number, for the dot in an english one

    return the string with the replace function
    
    """

    return string.replace(change_for, change_to)



def change_type(df, column, type_from, type_to):

    """
    Function to change a given column from a given DataFrame 
    from 'type_from'
    to 'type_to'

    return the modified DataFrame
    
    """

    #If the type from is object
    if type_from == 'object':

        if df[column].dtype == 'object':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is float
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int                
            elif type_to=='int':
                df[column] = df[column].astype(int)

    
    #If the type from is float
    elif type_from == 'float':

        if df[column].dtype == 'float':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is object
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int    
            elif type_to=='int':
                df[column] = df[column].astype(int)

    
    #If the type from is int
    elif type_from == 'int64':

        if df[column].dtype == 'int64':

            df[column]= pd.to_numeric(df[column]) 

            #If the type to is object
            if type_to=='float':
                df[column] = df[column].astype(float)

            #If the type to is int    
            elif type_to=='object':
                df[column] = df[column].astype(object)

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
