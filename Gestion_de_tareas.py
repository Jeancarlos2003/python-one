class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"

    def __str__(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print("Tarea agregada con éxito.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        for tarea in self.tareas:
            print(tarea)

    def buscar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(tarea)
                return
        print("Tarea no encontrada.")

    def actualizar_estado(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.estado = "completada"
                print("Estado actualizado a 'completada'.")
                return
        print("Tarea no encontrada.")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                self.tareas.remove(tarea)
                print("Tarea eliminada.")
                return
        print("Tarea no encontrada.")


def main():
    gestor = GestorTareas()
    
    while True:
        print("1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Buscar tarea por título")
        print("4. Actualizar estado de una tarea")
        print("5. Eliminar tarea por título")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        try:
            if opcion == "1":
                titulo = input("Título de la tarea: ")
                descripcion = input("Descripción de la tarea: ")
                gestor.agregar_tarea(titulo, descripcion)
            elif opcion == "2":
                gestor.mostrar_tareas()
            elif opcion == "3":
                titulo = input("Título de la tarea a buscar: ")
                gestor.buscar_tarea(titulo)
            elif opcion == "4":
                titulo = input("Título de la tarea a actualizar: ")
                gestor.actualizar_estado(titulo)
            elif opcion == "5":
                titulo = input("Título de la tarea a eliminar: ")
                gestor.eliminar_tarea(titulo)
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("ocurrio un error")
           


