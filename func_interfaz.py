from tkinter import Frame, Label, LabelFrame, Variable


#Funcion creadora de paneles base:
def crear_panel(aplicacion:Variable, bd:int, relief:str, *args):
    
    """
    Crea un panel principal que contendrá subpaneles.
    
    Args:
        aplicacion: pantalla principal de la aplicación.
        bd: ancho de bordes que tendrá el panel.
        relief: tipo de relieve del panel.
        *args: color de fondo del panel (opcional)
            
    Returns:
        El panel creado sin ubicación especifica en la pantalla. 
        """
        
    panel = Frame(aplicacion, bd= bd, relief=relief, bg= args)
    return panel


#Funcion etiquetas:
def crear_etiqueta(subpanel:Variable, texto:str, row:int, columna:int, *args):
    
    """
    Crea una etiqueta (texto contenido en los paneles y subpaneles).
    
    Args:
        subpanel: panel o subpanel donde se ubicará el texto.
        texto: el texto definirá a la etiqueta.
        row: fila del panel o subpanel en la que se ubicará la etiqueta.
        columna: columna del panel o subpanel en la que se ubicará la etiqueta.
        *args (opcional): definirá el "padx" o ancho de la etiqueta.
            
    Returns:
        La etiqueta creada y establecida en un panel o subpanel. 
        """
        
    etiqueta = Label(subpanel, text=texto, font=("arial", 12), bg= "blue3", fg="white" )
    etiqueta.grid(row=row, column=columna, padx=args)
    
    
#Funcion creadora de subpaneles:   
def crear_subpanel(panel_principal:Variable, bd:int, relief:str, texto:str, fuente:tuple, fg:str, bg:str):
        
    """
    Crea un subpanel dentro del panel principal.
    
    Args:
        panel_principal: El panel principal en el que se creará el subpanel.
        bd: El ancho del borde del subpanel.
        relief: El estilo de relieve del subpanel.
        texto: El texto que se mostrará en el subpanel.
        fuente: Información sobre la fuente del texto en forma de tupla ("fuente", tamaño fuente).
        fg: Color del texto.
        bg: Color de fondo del subpanel.
    
    Returns:
        El subpanel creado.
    """

    sub_panel = LabelFrame(panel_principal, bd=bd, relief=relief, font=(fuente[0], fuente[1], "bold"), fg=fg,
                            text=texto, bg=bg)
    return sub_panel


