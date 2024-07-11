import os
import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos_trabajadores = []

def limpiar_pantalla():
    os.system("cls")

def menu_principal():
    limpiar_pantalla()
    print("Evaluacion Final Transversal")
    print("="*30)
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def asignar_sueldos_aleatorios():
    limpiar_pantalla()
    print("Asignar sueldos aleatorios a trabajadores")
    print("="*30)
    for i in range(len(trabajadores)):
        sueldo_aleatorio = random.randint(300000,2500000)
        sueldos_trabajadores.append(sueldo_aleatorio)
    print("\nSueldos asignados correctamente entre $300.000 y $2.500.000.\n")
    print("Trabajador\t\tSueldo")
    print("="*30)
    for i in range(len(trabajadores)):
        print(f"{trabajadores[i]:<20}\t${sueldos_trabajadores[i]}")
    
def clasificar_sueldos():
    print(sueldos_trabajadores)
    limpiar_pantalla()
    print("\nClasificacion de sueldos.")
    print("="*30)
    for i in range(len(trabajadores)):
        sueldo_aleatorio = sueldos_trabajadores[i]
        if sueldo_aleatorio < 800000:    
            clasificacion = "Sueldos menores a $800.000"
        elif sueldo_aleatorio <= 2000000:
            clasificacion = "Sueldos entre $800.000 y $2.000.000"
        else:
            clasificacion = "Sueldos superiores a $2.000.000"
        print(f"{trabajadores[i]:<20}: ${sueldo_aleatorio} - {clasificacion}")
        
def precio_mas_bajo(sueldos_trabajadores):
    menor=min(sueldos_trabajadores)
    return menor
def precio_mas_alto(sueldos_trabajadores):
    mayor=max(sueldos_trabajadores)
    return mayor
def promedio(sueldos_trabajadores):
    prom_sueldos=sum(sueldos_trabajadores)/len(sueldos_trabajadores)
    return prom_sueldos
def media_geometrica(sueldos_trabajadores):
    trabajador_sueldo=1
    for sueldo_aleatorio in sueldos_trabajadores:
        trabajador_sueldo *= sueldo_aleatorio
    return trabajador_sueldo **(1/len(sueldos_trabajadores))

def ver_estadisticas():
    limpiar_pantalla()
    print("Estadisticas de sueldos")
    print(f"Precio mas alto: ${precio_mas_alto(sueldos_trabajadores)}")
    print(f"Precio mas bajo: ${precio_mas_bajo(sueldos_trabajadores)}")
    print(f"Promedio de sueldos: ${promedio(sueldos_trabajadores)}")
    print(f"Medida geometrica de sueldos: ${media_geometrica(sueldos_trabajadores)}")
    
def generar_archivo(sueldos_trabajadores):
    csv_content = "Nombre empleado,Sueldo Base,Descuento Salud,Descuento AFP,Sueldo Líquido\n"
    for i in range(len(trabajadores)):
        sueldo_aleatorio = sueldos_trabajadores[i]
        descuento_salud = sueldo_aleatorio * 0.07
        descuento_AFP = sueldo_aleatorio * 0.12
        sueldo_liquido = sueldo_aleatorio - descuento_salud - descuento_AFP
        csv_content += f"{trabajadores[i]},{sueldo_aleatorio},{descuento_salud},{descuento_AFP},{sueldo_liquido}\n"
    return csv_content

def guardar_reporte():
    limpiar_pantalla()
    csv_content = generar_archivo(sueldos_trabajadores)
    with open('reporte_sueldos.csv', 'w') as file:
        file.write(csv_content)
    print("\nReporte de sueldos generado correctamente en 'reporte_sueldos.csv'")