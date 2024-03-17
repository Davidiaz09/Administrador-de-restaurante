from tkinter import Button, END, DISABLED
from tkinter import filedialog, messagebox
import datetime, random
from database import *
from variables import *


#Creando y asignando funcionalidades a los botones (Total, Recibo, Guardar, Reset):
def crear_botones_opciones(panel, contenido_entrywidget_comida, contenido_entrywidget_bebidas,
                           contenido_entrywidget_postres, recibo, diccionario):
    
    """
    Crea y configura los botones de opciones dentro del panel proporcionado, como 
    "Total", "Recibo", "Guardar" y "Reset".
    Asigna a cada botón una función específica que se ejecutará cuando este se presione, realizando diferentes 
    acciones como calcular el total de la factura, mostrar un recibo, guardar el recibo como un archivo 
    de texto y restablecer todos los valores de la interfaz a sus estados iniciales.
    
    No Args.
    No Return.
    """
    
    #Definiendo nombres de los botones y agregandolos a la pantalla:
    nombre_botones = ["Total", "Recibo", "Guardar", "Reset"]
    objetos_botones = []
    for i, boton in enumerate(nombre_botones):
        b = Button(panel, text=boton.title(), font=("arial", 12), bg="White", fg="black", width=7)
        b.grid(row=0, column=i)
        objetos_botones.append(b)
    
    #asignando una función a cada botón:
    objetos_botones[0].config(command=lambda: boton_total(comidas, bebidas, postres,
                                                        contenido_entrywidget_comida, contenido_entrywidget_bebidas, contenido_entrywidget_postres, diccionario)) 
        
    objetos_botones[1].config(command=lambda: boton_recibo(recibo)) 
    objetos_botones[2].config(command=lambda: guardar_recibo(recibo))
    objetos_botones[3].config(command=lambda: reset(recibo, diccionario)) 
         
        
#Creando funcionalidad para el botón "Total":    
def boton_total(comidas: list, bebidas:list, postres:list, contenido_entryw_comidas:list,
                contenido_entryw_bebidas:list, contenido_entryw_postres:list, diccionario):
    
    """
    Calcula el total de la factura sumando los costos de las comidas, bebidas y postres seleccionados,
    incluyendo impuestos, y actualiza los valores mostrados en la pantalla para reflejar el resultado.
    Esta función toma como argumentos las listas de elementos disponibles y las cantidades ingresadas 
    para cada categoría.

    Args:
        comidas: Lista de tuplas (precio, nombre) de las comidas disponibles.
        bebidas: Lista de tuplas (precio, nombre) de las bebidas disponibles.
        postres: Lista de tuplas (precio, nombre) de los postres disponibles.
        contenido_entryw_comida: Lista de contenido para las cantidades de comidas ingresadas.
        contenido_entryw_bebida: Lista de contenido para las cantidades de bebidas ingresadas.
        contenido_entryw_postre: Lista de contenido para las cantidades de postres ingresadas.
        
    No Returns.
    """
    
    try:
        
        global subtotal, impuestos, total
        total_categoria1 = 0
        total_categoria2 = 0
        total_categoria3 = 0
        
        #Creando totales para cada categoria (comidas, bebidas, postres)
        # multiplicando el precio del elemento del menú por la cantidad ingresada en los entrywidgets
        for i, p in enumerate(comidas):
            total_categoria1 = total_categoria1 + (p[0]) * int(contenido_entryw_comidas[i].get())
        for i, p in enumerate(bebidas):
            total_categoria2 = total_categoria2 + (p[0]) * int(contenido_entryw_bebidas[i].get())
        for i, p in enumerate(postres):
            total_categoria3 = total_categoria3 + (p[0]) * int(contenido_entryw_postres[i].get())
            
        #Valores correspondientes a totales de categorias:   
        total_comida = total_categoria1
        total_bebidas = total_categoria2
        total_postres = total_categoria3    
        
        #Valor correspondiente a casillas de "subtotales", "impuestos" y "total":
        subtotal = total_categoria1+total_categoria2+total_categoria3
        impuestos = subtotal*0.07
        total= subtotal+impuestos
        
        #Asigando los valores anteriores a sus casillas correspondientes para mostrarlos en pantalla:
    
        diccionario["total_comidas"].set(f"${total_comida}")
        diccionario["total_bebidas"].set(f"${total_bebidas}")
        diccionario["total_postres"].set(f"${total_postres}")
        diccionario["subtotal"].set(f"${subtotal}")
        diccionario["impuestos"].set(f"${round(impuestos, 2)}")
        diccionario["total"].set(f"${total}")
        
    except:
        pass
    
    
#Creando funcionanlidad para el boton "Recibo"
def boton_recibo(recibo):
    
    """
    Crea un recibo que muestra la información de compra de los usuario de manera estructurada, ademas de 
    incluir datos como el numero de recibo, fecha y hora del momento en que se genera.
    
    No args
    No returns.
    """
    
    #Insertando datos en la pantalla del recibo (fecha, hora, comidas consumidas, cantidad comidas consumidas,
    # costo comidas consumidas, subtotal, impuestos y total):
    try:
        recibo.delete(1.0, END)
        numero_recibo = f"N# - {random.randint(100, 999)}"
        fecha_hora = datetime.datetime.today()
        insertar_fecha_hora = f"{fecha_hora.date()}.  \t\t{fecha_hora.time().hour}:{fecha_hora.time().minute}:{fecha_hora.time().second}"
        recibo.insert(END, f"{numero_recibo}.        \t{insertar_fecha_hora}\n")
        recibo.insert(END, f"-"*55)
        recibo.insert(END, f"\nitems.\t       cantidad.\t \t  valor\n")
        recibo.insert(END, f"-"*55)
        
        for i, cantidad in enumerate(entrywidget_comidas):
            if int(cantidad.get()) > 0:
                recibo.insert(END,f"\n{comidas[i][1]}.\t  {cantidad.get()}\t\t${int(cantidad.get())*comidas[i][0]}\n")
                
        for i, cantidad in enumerate(entrywidget_bebidas):
            if int(cantidad.get()) > 0:
                recibo.insert(END,f"{bebidas[i][1]}.\t  {cantidad.get()}\t\t${int(cantidad.get())*bebidas[i][0]}\n")
                
        for i, cantidad in enumerate(entrywidget_postres):
            if int(cantidad.get()) > 0:
                recibo.insert(END,f"{postres[i][1]}.\t  {cantidad.get()}\t\t${int(cantidad.get())*postres[i][0]}\n")

        recibo.insert(END, f"-"*55)
        recibo.insert(END,f"\nSubtotal\t\t\t    {subtotal}\n")
        recibo.insert(END,f"Impuestos\t\t\t   {round(impuestos, 2)}\n")
        recibo.insert(END,f"Total\t\t\t {total}\n")
        recibo.insert(END, f"-"*55)
    except:
        pass


#Creando funcionanlidad para el boton "Guardar" 
# se guardará el contenido exitente en la pantalla del recibo como un archivo txt.
def guardar_recibo(recibo):
    
    """Permite guardar la información del recibo en un archivo "txt" """
    try:
        informacion = recibo.get(1.0, END)
        archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        archivo.write(informacion)
        archivo.close()
        
        messagebox.showinfo("info", "El recibo ha sido guardado correctamente") 
        
    except AttributeError:
        pass
    
    
#Creando funcionanlidad para el boton "Reset"             
def reset(recibo, diccionario):
    
    """Reestablece todos los valores de la interfaz"""
    
    #Estableciendo en "0" el valor de los entrywidgets:
    for texto in contenido_entrywidget_comida:
        texto.set("0")
    for texto in contenido_entrywidget_bebidas:
        texto.set("0")
    for texto in contenido_entrywidget_postres:
        texto.set("0")
    
    #Desahabilitando los entrywidgets    
    for ewid in entrywidget_comidas:
        ewid.config(state=DISABLED)
    for ewid in entrywidget_bebidas:
        ewid.config(state=DISABLED)
    for ewid in entrywidget_postres:
        ewid.config(state=DISABLED)
        
    #Desactivando los Check Buttons (estableciendo su valor en 0):
    for estado in valores_check_comidas:
        estado.set(0)
    for estado in valores_check_bebidas:
        estado.set(0) 
    for estado in valores_check_postres:
        estado.set(0)   
        
    #Eliminando contenido de la pantalla del recibo:                               
    recibo.delete(1.0, END)
    
    #Eliminado cotenido de las casillas de totales
    diccionario["total_comidas"].set("")
    diccionario["total_bebidas"].set("")
    diccionario["total_postres"].set("")
    diccionario["subtotal"].set("")
    diccionario["impuestos"].set("") 
    diccionario["total"].set("")   
        