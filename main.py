from funciones import *



while True:
    limpiar_pantalla()
    menu_principal()
    try:
        opcion=int(input("Ingresa una opcion:\n"))
        if opcion==1:
            asignar_sueldos_aleatorios()
            input("\nPresiona una tecla para volver al menu principal.")
        elif opcion==2:
            clasificar_sueldos()
            input("\nPresiona una tecla para volver al menu principal.")
        elif opcion==3:
            ver_estadisticas()
            input("\nPresiona una tecla para volver al menu principal.")
        elif opcion==4:
            guardar_reporte()
            input("\nPresiona una tecla para volver al menu principal.")

        elif opcion==5:
            print("Finalizando programa…")
            print("Desarrollado por Bastian Corona")
            print("RUT 18.602.778-7")
    except:
        print("Opcion ingresada no existe.")