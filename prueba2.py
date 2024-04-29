import tkinter as tk


class Ingrediente:
    def __init__(self, producto, presentacion, precio, cantidad_usada):
        self.producto = producto
        self.presentacion = presentacion
        self.precio = precio
        self.cantidad_usada = cantidad_usada

    def calcular_costo_ing(self):
        if self.presentacion == "kilo":
            cantidad_usada_kg = self.cantidad_usada / 1000  # Convertir gramos a kilos
            costo_ingr = (self.precio / self.kilos_paquete) * cantidad_usada_kg
        elif self.presentacion == "unidad":
            costo_ingr = self.precio * self.cantidad_usada
        elif self.presentacion == "maple":
            costo_ingr = (self.precio / 30) * self.cantidad_usada
        else:
            costo_ingr = 0

        return costo_ingr


def agregar_ingrediente():
    producto = nombre_entry.get()
    presentacion = presentacion_var.get()
    precio = float(precio_entry.get())
    cantidad_usada = float(cantidad_entry.get())

    ingredientes.append(Ingrediente(producto, presentacion, precio, cantidad_usada))
    if presentacion == "kilo":
        ingredientes[-1].kilos_paquete = float(kilos_entry.get())

    limpiar_entradas()


def limpiar_entradas():
    nombre_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)
    if presentacion_var.get() == "kilo":
        kilos_entry.delete(0, tk.END)


def finalizar():
    # Tomar los datos del último ingrediente ingresado
    producto = nombre_entry.get()
    presentacion = presentacion_var.get()
    precio = float(precio_entry.get())
    cantidad_usada = float(cantidad_entry.get())

    # Crear el objeto Ingrediente con los datos ingresados
    nuevo_ingrediente = Ingrediente(producto, presentacion, precio, cantidad_usada)
    if presentacion == "kilo":
        nuevo_ingrediente.kilos_paquete = float(kilos_entry.get())

    # Eliminar el último elemento de la lista si ya existe (evitar duplicados)
    if ingredientes and ingredientes[-1] == nuevo_ingrediente:
        del ingredientes[-1]

    # Agregar el nuevo ingrediente a la lista
    ingredientes.append(nuevo_ingrediente)

    # Mostrar los costos
    for i, ingrediente in enumerate(ingredientes):
        costo_ingr = ingrediente.calcular_costo_ing()
        label = tk.Label(frame, text=f"Costo de {ingrediente.producto}: ${costo_ingr:.2f}")
        label.grid(row=i + 8, columnspan=2, sticky="w")

    costo_total = sum(ingrediente.calcular_costo_ing() for ingrediente in ingredientes)
    total_label.config(text=f"Costo total de la receta: ${costo_total:.2f}")


def comenzar():
    agregar_ingrediente_button.config(state=tk.NORMAL)
    finalizar_button.config(state=tk.NORMAL)
    nombre_entry.config(state=tk.NORMAL)
    presentacion_menu.config(state=tk.NORMAL)
    precio_entry.config(state=tk.NORMAL)
    cantidad_entry.config(state=tk.NORMAL)
    if presentacion_var.get() == "kilo":
        kilos_entry.config(state=tk.NORMAL)


ventana = tk.Tk()
ventana.title("CALCULADORA DE COSTOS")

frame = tk.Frame(ventana, width=400, height=300)
frame.pack()

ingredientes = []

nombre_label = tk.Label(frame, text="Nombre del ingrediente:", padx=10, pady=10)
nombre_label.grid(row=0, column=0, sticky="w")
nombre_entry = tk.Entry(frame,  state=tk.DISABLED)
nombre_entry.grid(row=0, column=1, padx=80, pady=10)

presentacion_label = tk.Label(frame, text="Presentación del ingrediente:")
presentacion_label.grid(row=1, column=0, sticky="w")
presentacion_var = tk.StringVar()
presentacion_menu = tk.OptionMenu(frame, presentacion_var, "kilo", "unidad", "maple")
presentacion_menu.grid(row=1, column=1, sticky="w")
presentacion_menu.config(state=tk.DISABLED)

precio_label = tk.Label(frame, text="Precio:")
precio_label.grid(row=2, column=0, sticky="w")
precio_entry = tk.Entry(frame, state=tk.DISABLED)
precio_entry.grid(row=2, column=1)

cantidad_label = tk.Label(frame, text="Cantidad utilizada:")
cantidad_label.grid(row=3, column=0, sticky="w")
cantidad_entry = tk.Entry(frame, state=tk.DISABLED)
cantidad_entry.grid(row=3, column=1)

kilos_label = tk.Label(frame, text="Kilos del paquete:")
kilos_entry = tk.Entry(frame, state=tk.DISABLED)
presentacion_var.trace_add('write', lambda *args: kilos_entry.config(
    state=tk.NORMAL) if presentacion_var.get() == 'kilo' else kilos_entry.config(state=tk.DISABLED))
kilos_label.grid(row=4, column=0, sticky="w")
kilos_entry.grid(row=4, column=1)

agregar_ingrediente_button = tk.Button(frame, text="Agregar Ingrediente", command=agregar_ingrediente,
                                       state=tk.DISABLED)
agregar_ingrediente_button.grid(row=5, column=0)

finalizar_button = tk.Button(frame, text="Finalizar", command=finalizar, state=tk.DISABLED)
finalizar_button.grid(row=5, column=1)

comenzar_button = tk.Button(frame, text="Comenzar", command=comenzar)
comenzar_button.grid(row=6, columnspan=2)

total_label = tk.Label(frame, text="")
total_label.grid(row=7, columnspan=2)

ventana.mainloop()
