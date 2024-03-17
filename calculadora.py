from tkinter import Entry, END, Button   
        
#Modelando diseño de la calculadora y habilitando sus funcionalidades:
def calculadora(panel_principal_calculadora):
    
    """
    Crea una calculadora dentro del panel proporcionado, permitiendo al usuario realizar operaciones
    aritméticas básicas (suma, resta, multiplicación y división) con los números ingresados.
    La calculadora muestra una pantalla de entrada para ingresar números y botones para las operaciones,
    y actualiza la pantalla con el resultado cuando se presiona el botón de igual.
    
    No Args.
    No Returns.
    """

    #Creando la pantalla de la calculadora:
    pantalla = Entry(panel_principal_calculadora, font=("arial", 12), bd=2, width=31, relief="flat")
    pantalla.grid(row=0, column=0, columnspan=4)
    
    #Función activar la función de los botones al clickearlos
    def click(contenido_boton):
        operador = contenido_boton
        pantalla.insert(END, operador)
        
    #Funcion borrar contenido pantalla calculadora (tecla: Borrar):
    def limpiar_pantalla():
        pantalla.delete(0, END)
        
    #funcion para obtener resultado (=):
    def obt_resultado():
        obt_resultado = str(eval(pantalla.get()))
        pantalla.delete(0, END)
        pantalla.insert(0, obt_resultado)    

    #Botones calculadora:
    fila = 1
    columna = 0
    objetos_botones= []
    lista_botones = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*","=", "BORRAR", "0", "/"]
    for boton in lista_botones:
        b = Button(panel_principal_calculadora, font=("arial", 12), text=boton.title(), bg="white", fg= "black", width=7,
                    bd=1, relief="sunken")
        b.grid(row=fila, column=columna) 
        
        objetos_botones.append(b)
        
        columna += 1
        if columna == 4:
            columna = 0
            fila+= 1
        
    #Activando botones (asignandolos a cada botón de la calculadora):
    objetos_botones[0].config(command=lambda : click("7"))        
    objetos_botones[1].config(command=lambda : click("8"))  
    objetos_botones[2].config(command=lambda : click("9"))  
    objetos_botones[3].config(command=lambda : click("+"))  
    objetos_botones[4].config(command=lambda : click("4"))        
    objetos_botones[5].config(command=lambda : click("5"))  
    objetos_botones[6].config(command=lambda : click("6"))  
    objetos_botones[7].config(command=lambda : click("-"))
    objetos_botones[8].config(command=lambda : click("1"))        
    objetos_botones[9].config(command=lambda : click("2"))  
    objetos_botones[10].config(command=lambda : click("3"))  
    objetos_botones[11].config(command=lambda : click("*"))  
    objetos_botones[12].config(command=obt_resultado)        
    objetos_botones[13].config(command=limpiar_pantalla)  
    objetos_botones[14].config(command=lambda : click("0"))  
    objetos_botones[15].config(command=lambda : click("/"))  
