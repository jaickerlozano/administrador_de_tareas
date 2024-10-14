from abc import ABC, abstractmethod

# Abstraccion  para el servicio de gestionamiento de tareas ( interface )
class GestionadorTareas(ABC):
    @abstractmethod
    def agregar_tarea(self, tarea_nueva: str, responsable: str, descripcion: str):
        pass

    @abstractmethod
    def cambiar_responsable_tarea(self, tarea: str, nuevo_responsable: str):
        pass

    @abstractmethod
    def actualizar_descripcion_tarea(self, tarea: str, descripcion_actualizada: str):
        pass

class MostradorTareas(ABC):
    @abstractmethod
    def imprimir_lista_tareas(self, lista_tareas):
        pass

# Implementación del gestor de tareas
class GestionamientoTareas(GestionadorTareas):
    def __init__(self):
        self.tareas = {} # Inicializamos el diccionario de tareas

    def agregar_tarea(self, tarea_nueva: str, responsable: str, descripcion: str):
        self.tareas[tarea_nueva] = {'responsable' : responsable, 'descripcion': descripcion}

    def cambiar_responsable_tarea(self, tarea: str, nuevo_responsable: str):
        if tarea in self.tareas:
            self.tareas[tarea]['responsable'] = nuevo_responsable

    def actualizar_descripcion_tarea(self, tarea: str, descripcion_actualizada: str):
        if tarea in self.tareas:
            self.tareas[tarea]['descripcion'] = descripcion_actualizada

    def obtener_tareas(self):
        return self.tareas

# Implementacion para imprimir lista de tareas
class MostrarListaTareas(MostradorTareas):
    def imprimir_lista_tareas(self, lista_tareas):
        for tarea, detalle in lista_tareas.items():
            print("Tarea: " + tarea)
            print("descripcion:", detalle["descripcion"])
            print("responsable: " + detalle["responsable"] + "\n")
            #print(f"La lista de tareas es: {lista_tareas}")

# Gestor principal que coordina la gestión y la impresión de tareas
class GestorTarea:
    def __init__(self, gestionamiento: GestionamientoTareas, impresion: MostrarListaTareas):
        self.gestionamiento = gestionamiento
        self.impresion = impresion

    def agregar_tarea(self, tarea_nueva: str, responsable: str, descripcion: str):
        self.gestionamiento.agregar_tarea(tarea_nueva, responsable, descripcion)

    def cambiar_responsable_tarea(self, tarea: str, nuevo_responsable: str):
        self.gestionamiento.cambiar_responsable_tarea(tarea, nuevo_responsable)

    def actualizar_descripcion_tarea(self, tarea: str, descripcion_actualizada: str):
        self.gestionamiento.actualizar_descripcion_tarea(tarea, descripcion_actualizada)

    def imprimir_lista_tareas(self):
        tareas = self.gestionamiento.obtener_tareas()
        self.impresion.imprimir_lista_tareas(tareas)

# Modo de uso

# Instanciamos las clases necesarias
gestionamiento = GestionamientoTareas()
mostrarLista = MostrarListaTareas()
tarea1 = GestorTarea(gestionamiento, mostrarLista)
tarea2 = GestorTarea(gestionamiento, mostrarLista)

# Usamos los métodos
tarea1.agregar_tarea('cotizar', 'Jaicker', 'solicitar precios ssd')
tarea2.agregar_tarea('contrataciones', 'Elyna', 'contratar personal')
tarea1.imprimir_lista_tareas()

