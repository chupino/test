from functions.functions import *




while True:
    print("\nAdministrador de Tareas")
    print("-----------------------")
    print("1. Agregar tareas")
    print("2. Marcar tareas como completadas")
    print("3. Mostrar tareas pendientes")
    print("4. Mostrar última tarea completada")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        marcar_completada()
    elif opcion == "3":
        mostrar_pendientes()
    elif opcion == "4":
        mostrar_ultima_completada()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")