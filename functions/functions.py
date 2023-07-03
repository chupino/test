tareas = []
tareas_completadas = []

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def marcar_completada():
    if len(tareas) == 0:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas):
            print(f"|   {i+1}            | {tarea:<15}|")

        num_tarea = int(input("Ingrese el número de la tarea completada: "))
        if num_tarea < 1 or num_tarea > len(tareas):
            print("Número de tarea inválido.")
        else:
            tarea_completada = tareas.pop(num_tarea - 1)
            tareas_completadas.append(tarea_completada)
            print(f"La tarea '{tarea_completada}' ha sido marcada como completada.")

def mostrar_pendientes():
    if len(tareas) == 0:
        print("No hay tareas pendientes.")
    else:
        print(
          "]"
        )
        print("Tareas pendientes:")
        print("+------+-----------------+")
        print("| Número |      Tarea    |")
        print("+------+-----------------+")
        for i, tarea in enumerate(tareas):
            print(f"|   {i+1}   | {tarea:<15}|")
        print("+------+-----------------+")


def mostrar_ultima_completada():
    if len(tareas_completadas) == 0:
        print("No hay tareas completadas.")
    else:
        tarea_completada = tareas_completadas[-1]
        print("Última tarea completada:")
        print("+------+-----------------+")
        print("| Número |      Tarea      |")
        print("+------+-----------------+")
        print(f"|   1   | {tarea_completada:<15}|")
        print("+------+-----------------+")