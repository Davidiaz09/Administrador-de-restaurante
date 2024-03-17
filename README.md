Este proyecto consiste en el desarrollo de una aplicación de facturación y ventas para un restaurante creada a partir de las bibliotecas tkinter, random y datetime. 
El menú del restaurante está conformado por tres categorías de alimentos: comidas, bebidas y postres. Cada categoría cuenta con ocho elementos (platos/productos disponibles) que la conforman.
En la interfaz de la aplicación se muestran las categorías y sus elementos organizados en filas verticales. Cada elemento tiene asignando un cuadro de entrada en el que se pueden ingresar las cantidades que solicita el cliente, siempre y cuando el cuadro se encuentre activado. 
Al hacer click en el botón "Total", se efectúa el cálculo y se muestran en pantalla los valores del total para cada categoría, el subtotal, los impuestos y el total final del pedido (cuadros de entrada panel inferior costos).
La aplicación también cuenta con una calculadora de asistencia integrada que permite realizar operaciones básicas como suma, resta, multiplicación y división, así como un panel para la generación del recibo correspondiente a los datos de venta usando el botón "Recibo" y la opción de guardarlo como un archivo txt para mantener un registo o imprimirlo según convenga, a través del botón "Guardar".
Por ultimo el botón "Reset" permite reestablecer todos los valores de la interfaz a su estado inicial, implementado como una forma para tomar un nuevo pedido o comenzar de nuevo en caso de errores.

La aplicación se divide en siete módulos: botones_panel_der, calculadora, database, entrywid_checkb, func_interfaz, listas y ejecutar_interfaz:
El módulo botones_panel_der proporciona las funciones encargadas de crear los botones Total, Recibo, Guardar y Reset y establecer su funcionamiento.
Funciones: crear_botones_opciones, boton_total, boton_recibo, guardar_recibo, reset.

El módulo calculadora contiene una única función encargada de crear la calculadora. Incluye subfunciones para el rol que desempeña cada botón.
Funcion: calculadora.
subfunciones: click, limpiar_pantalla, obt_resultado.

database proporciona la base de datos de la aplicación. Aquí se encuentra almacenada la información sobre cada elemento/producto de las categorías en forma de listas. Dicha información refiere al nombre del elemento/producto y su precio en pesos colombianos.

entrywid_checkb proporciona funciones para crear los elementos de la interfaz gráfica y evaluar su estado. Estos elementos son los cuadros de entrada del panel inferior costos y los asociados a cada elemento/producto de las categorías, además de los check buttons para cada producto. 
Funciones: entry_widget_panel_inferior, entry_widget_categorias, checking, checkbuttons.

func_interfaz provee funciones para crear paneles base, subpaneles y etiquetas.
Funciones: crear_panel, crear_etiqueta, crear_subpanel.

El módulo listas almacena las listas que contienen los objetos de interfaz check buttons y entry widgets creados a partir del módulo entrywid_checkb, así como la entrada de información para cada entry widget.

ejecutar_interfaz es el módulo principal donde se crea la interfaz de la aplicación y se establecen parámetros de configuración. Aquí se define la estructura general de la aplicación, incluyendo el tamaño y posición de los paneles, la creación de entry widgets, botones, etiquetas, y la asignación de funciones de los demás módulos para casos específicos. a través de este módulo se ejecuta la aplicación.




