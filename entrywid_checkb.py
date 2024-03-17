from tkinter import *


#Funcion entradas elementos de subpanel costos:    
def entry_widget_panel_inferior(subpanel:Variable, state, row:int, columna:int, variable:StringVar):
    
    """
    Crea los entry widgets para el panel inferior con una fuentes y tamaño de letra establecidos
    (Total comidas, total bebidas, total postres, subtotal, impuestos, total).

    Args:
        subpanel: subpanel donde estrá contenido el entry widget.
        satate: estado del entrywidget.
        row: fila en el panel donde estará ubicado.
        columna: columna en el panel donde estará ubicado.
        variable: variable de tipo "StringVar" donde se almacenará el contenido del entry widget
        
    No Returns.  
    """
    
    entrada = Entry(subpanel, font=("arial", 11), state=state, bd=1, width=10, textvariable=variable )
    entrada.grid(row=row, column=columna)
        
        
#Función creadora de cuadros de entrada para categorias (entry widgets):
def entry_widget_categorias(subpanel:Variable, lista_contenedora:list, lista_contenido_entryw:list):
    
    """
    Crea los entry widgets para cada elemento de las categorias con una fuente y tamaño, ubicacion
    en el panel establecidos.
    
    Args:
        subpanel: subpanel donde estrá contenido el entry widget.
        lista_contenedora: lista donde se almacenarán los objetos de tipo "Entry" creados con esta función.
        lista_textos_entryw: lista contenedora del contenido almacenado en los entry widgets.
        
    No Returns.  
    """
    
    for i, c in enumerate(list(range(1,9))):  #
        
        #Estableciendo valor por defecto de los cuadros de entrada (0):
        lista_contenido_entryw.append("")
        lista_contenido_entryw[i] = StringVar()
        lista_contenido_entryw[i].set("0")
        
        #Creando los cuadros de entrada:
        lista_contenedora.append(Entry(subpanel, font=("arial", 12, "bold"), bd=2, width= 3, state=DISABLED, 
                                textvariable=lista_contenido_entryw[i]))                            
        lista_contenedora[i].grid(row=i, column= 1)
    
    
#Funcion "Checking" comprueba el estado de los check buttons (su valor en offvalue y onvalue):
def checking(valores_categoria:list, entrywid:list, contenido_entrywid:list):
    
    """
    Comprueba el estado de los "check buttons" (onvalue, offvalue) y habilita los cuadros de entrada
    correspondientes si estos están activados; si están desactivados, deshabilitaran los entry widgets
    correspondientes y estableceran su contenido en 0.
    
    Args:
        valores_categoria: lista contenedora de los objetos "CheckButtons.
        entrywid: lista contenedora de los objetos "Entry.
        contenido_entrywid: lista de los contenidos de los entry widgets.
        
    No Returns.  
    """

    for i, cuadro in enumerate(entrywid):
        if valores_categoria[i].get() == 1:
            cuadro.config(state=NORMAL)
            if cuadro.get() == "0":
                cuadro.delete(0, END)
                cuadro.focus()
        else:
            cuadro.config(state=DISABLED)
            contenido_entrywid[i].set("0") 
        
        
#Definiendo check buttons para cada elemento de las listas correspondientes al menú:
def checkbuttons(lista:list, subpanel:Variable, valores_check:list, entrywidgets:list, contenido_entrywidgets:list):   
    
    """
    Crea y configura los checkbuttons para cada elemento en la lista proporcionada,
    asociando cada checkbutton con una variable de control (variable). (función "checking") 
    Cuando se activa un checkbutton, habilita el entrywidget correspondiente y actualiza su valor 
    en la lista de valores asociada. Cuando se desactiva un checkbutton, deshabilita el entrywidget 
    correspondiente y restablece su valor en la lista de valores a cero.

    Args:
        lista: Lista de elementos de categorias para los cuales se crearán checkbuttons.
        subpanel: Subpanel en el que se crearán los checkbuttons.
        valores_cat: Lista de variables que almacenarán el valor de los checkbuttons (onvalue, offvalue).
        entrywidgets: Lista de entrywidgets asociados a los checkbuttons.
        contenido_entrywidgets: Lista que almacena el contenido de los entry widgets.
        
    No Returns.
    """
    
    for i, e in enumerate(lista):
        valores_check.append(IntVar())
        check_button = Checkbutton(subpanel, text=e[1].title(), font=("arial", 12, "bold"), onvalue=1,
                                    offvalue=0, bg="blue3", variable=valores_check[i], command=lambda: checking(valores_check, entrywidgets, contenido_entrywidgets))
        check_button.grid(row=i, column=0, sticky=W)
        
    #Creando el entry widget para cada elemento de la categoria:
    entry_widget_categorias(subpanel, entrywidgets, contenido_entrywidgets)
