from tkinter import * 
from func_interfaz import *
from entrywid_checkb import *
import calculadora
from botones_panel_der import *
from database import *
from variables import *


#Iniciando "tkinter"
app = Tk()


#Tamaño pantalla:
#"geometry" recibe como parametros el tamaño en pixeles de la pantalla (850x500) y su ubicacion en la pantalla del
# dispositivo (+0+0 esquina superior izquierda):
app.geometry("1000x450+80+30")

#impidiendo reajuste de tamaño:
app.resizable(0,0)

#Cambiando color de pantalla (admite nombres de colores en inglés o sus valores en "RGB")
app.config(bg= "blue")

#Estbleciendo el titulo de la aplicación:
app.title("Sistema de facturación")


#Variables que contienen el contenido de los entry widgets del panel inferior
entrywidget_total_comidas= StringVar()
entrywidget_total_bebidas= StringVar()
entrywidget_total_postres= StringVar()
entrywidget_subtotal= StringVar()
entrywidget_impuestos= StringVar()
entrywidget_total = StringVar()

entradas_panel_inferior = {
    "total_comidas": entrywidget_total_comidas,
    "total_bebidas": entrywidget_total_bebidas,
    "total_postres": entrywidget_total_postres,
    "subtotal": entrywidget_subtotal,
    "impuestos": entrywidget_impuestos,
    "total": entrywidget_total
}



#Creando panel superior:
def panel_superior():
    panel_superior = crear_panel(app, 2, "ridge")
    panel_superior.pack(side = TOP)
    
    #Definiendo etiqueta del titulo:
    def etiqueta_titulo():
        etiqueta_titulo = Label(panel_superior, text="Sistema de facturación", fg = "white", bg = "blue3",
                           font = ("arial", 28), width = 45)
        #Determinando el espacio del panel que ocupará la etiqueta del titulo (ocupará todo el panel):
        etiqueta_titulo.grid(row= 0, column= 0)

    etiqueta_titulo()


#Creando panel izquierdo:
def panel_izquierdo():
    
    #Creando base del panel izquierdo
    panel_izquierdo_principal = crear_panel(app, 2, "flat")
    panel_izquierdo_principal.pack(side = LEFT)
                      
         
    #Panel inferior (costos y campos de entrada):
    panel_costos = Frame(panel_izquierdo_principal, bd = 2, relief= "flat", bg="blue3", padx=51)
    panel_costos.pack(side=BOTTOM) 
    
    
    #Contenido subpanel izquierdo (categorias):
    sub_panel_comidas = crear_subpanel(panel_izquierdo_principal, 2, "flat", "Comidas", ("arial", 14), "white", "blue3")
    sub_panel_comidas.pack(side = LEFT)
    
    sub_panel_bebidas= crear_subpanel(panel_izquierdo_principal, 2, "flat", "Bebidas", ("arial", 14), "white", "blue3")
    sub_panel_bebidas.pack(side=LEFT)
    
    sub_panel_postres= crear_subpanel(panel_izquierdo_principal, 2, "flat", "Postres", ("arial", 14), "white", "blue3")
    sub_panel_postres.pack(side=RIGHT)
    
    
    #Creando etiquetas del subpanel inferior costos:    
    crear_etiqueta(panel_costos, "Costo comidas", 0, 0, 41)
    crear_etiqueta(panel_costos, "Costo bebidas", 1, 0, 41)   
    crear_etiqueta(panel_costos, "Costo postres", 2, 0, 41)
    crear_etiqueta(panel_costos, "Subtotal", 0, 3, 41)
    crear_etiqueta(panel_costos, "Impuestos", 1, 3, 41)
    crear_etiqueta(panel_costos, "Total", 2, 3, 41)
    
    #Creando entradas de subpanel inferior costos:
    entry_widget_panel_inferior(panel_costos, "readonly", 0, 2, entradas_panel_inferior["total_comidas"])
    entry_widget_panel_inferior(panel_costos, "readonly", 1, 2, entradas_panel_inferior["total_bebidas"])
    entry_widget_panel_inferior(panel_costos, "readonly", 2, 2, entradas_panel_inferior["total_postres"])
    entry_widget_panel_inferior(panel_costos, "readonly", 0, 4, entradas_panel_inferior["subtotal"])
    entry_widget_panel_inferior(panel_costos, "readonly", 1, 4, entradas_panel_inferior["impuestos"])
    entry_widget_panel_inferior(panel_costos, "readonly", 2, 4, entradas_panel_inferior["total"])
                    
    #Creando check buttons para cada elemento de las categorias:        
    checkb_comidas = checkbuttons(comidas, sub_panel_comidas, valores_check_comidas, entrywidget_comidas, contenido_entrywidget_comida)
    checkb_bebidas = checkbuttons(bebidas, sub_panel_bebidas, valores_check_bebidas, entrywidget_bebidas, contenido_entrywidget_bebidas)    
    checkb_postres = checkbuttons(postres, sub_panel_postres, valores_check_postres, entrywidget_postres, contenido_entrywidget_postres)
    
    
#Creando panel derecho:    
def panel_derecho():
    
    #Creando base del panel derecho : 
    panel_derecho_principal = crear_panel(app, 3, "flat")
    panel_derecho_principal.pack(side = RIGHT)
    
    
    #Subpaneles del panel derecho:        
        
    #Panel calculadora: 
    panel_principal_calculadora= crear_panel(panel_derecho_principal, 1, "flat", "blue3")
    panel_principal_calculadora.pack()
    
    #Llamando a la funcion que define la calculadora:
    calculadora.calculadora(panel_principal_calculadora)


    #Panel recibo:
    panel_principal_recibo= crear_panel(panel_derecho_principal, 2, "flat", "blue3")
    panel_principal_recibo.pack()
    #Cuadro de texto para el recibo:
    recibo = Text(panel_principal_recibo, font=("arial", 12), width=31, height=11, bd=2)
    recibo.grid(row=0, column=0)
    
    
    #Panel botones opciones (Total, Recibo, Guardar, Reset):
    panel_botones_opciones= crear_panel(panel_derecho_principal, 3, "flat", "white")
    panel_botones_opciones.pack()
    
    #Llamando a la funcion encargada de crear los botones y activar sus funcionalidades:
    crear_botones_opciones(panel_botones_opciones, contenido_entrywidget_comida, contenido_entrywidget_bebidas, 
                           contenido_entrywidget_postres, recibo, entradas_panel_inferior)

            
            
#Llamando funciones que componen a la aplicación:
panel_superior()
panel_izquierdo()
panel_derecho()
        

#Manteniendo pantalla:
app.mainloop()
