'''ADMINISTRACION DE PROYECTOS: 
Eres un gerente de proyectos y necesitas un programa para administrar 
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
una descripción y un responsable asignado. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las 
tareas. El programa debe permitir agregar nuevas tareas, asignar 
responsables a las tareas existentes, actualizar las descripciones de las 
tareas y mostrar la lista completa de tareas y responsables. 
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de diccionarios) '''

# Diccionario de tareas
tareas = {}

# Agregar nuevas tareas
tareas["Cotizaciones"] = {"responsable": "Juan", "Descripcion": "Pedir cotizaciones para compra de materiales"}
tareas["Contrataciones"] = {"responsable": "Sergio", "Descripcion": "Buscar personal para obra y contratar"}
tareas["Personal"] = {"responsable": "Adela", "Descripcion": "Supervisar personal"}

# Asignar responsables a las tareas existentes
tareas["Cotizaciones"]["responsable"] = "Jaicker"
tareas["Personal"]["responsable"] = "Elyna"

# Actualizar descripción tareas
tareas["Contrataciones"]["descripcion"] = "Buscar personal para obra, empresas mantenedoras y contratar"

# Impresión de tareas y responsables
for tarea, detalle in tareas.items():
    print("Tarea: " + tarea)
    print("Descripción:", detalle["Descripcion"])
    print("Responsable: " + detalle["responsable"] + "\n")