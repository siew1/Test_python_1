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
    return sueldos_trabajadores
    
def clasificar_sueldos():
    limpiar_pantalla()
    print("\nClasificacion de sueldos.")
    print("="*30)
    rango_sueldo1=[]
    rango_sueldo2=[]
    rango_sueldo3=[]
    for i in range(len(trabajadores)):
        sueldo_aleatorio = sueldos_trabajadores[i]
        if sueldo_aleatorio < 800000:    
            rango_sueldo1.append((trabajadores[i], sueldo_aleatorio))
        elif sueldo_aleatorio <= 2000000:
            rango_sueldo2.append((trabajadores[i], sueldo_aleatorio))
        else:
            rango_sueldo3.append((trabajadores[i], sueldo_aleatorio))

    print(f"Sueldos menores a $800.000 TOTAL {len(rango_sueldo1)}")
    print("Trabajador\t\tSueldo")
    for trabajador, sueldo_aleatorio in rango_sueldo1:
        print(f"{trabajador:<25}: ${sueldo_aleatorio}")
    if not rango_sueldo1:
        print("No hay sueldos menores a $800.000")
                    
    print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL {len(rango_sueldo2)}")
    print("Trabajador                Sueldo")
    for trabajador, sueldo_aleatorio in rango_sueldo2:
        print(f"{trabajador:<25}: ${sueldo_aleatorio}")
    if not rango_sueldo2:
        print("No hay sueldos entre $800.000 a $2.000.000")
        
    print(f"\nSueldos mayores a $2.000.000 TOTAL {len(rango_sueldo3)}")
    print("Trabajador                Sueldo")
    for trabajador, sueldo_aleatorio in rango_sueldo3:
        print(f"{trabajador:<25}: ${sueldo_aleatorio}")
    if not rango_sueldo3:
        print("No hay sueldos superior a $2.000.000")


def precio_mas_bajo(sueldos_trabajadores):
    menor = int(min(sueldos_trabajadores))
    return menor

def precio_mas_alto(sueldos_trabajadores):
    mayor = int(max(sueldos_trabajadores))
    return mayor

def promedio(sueldos_trabajadores):
    prom_sueldos = int(sum(sueldos_trabajadores) / len(sueldos_trabajadores))
    return prom_sueldos

def media_geometrica(sueldos_trabajadores):
    trabajador_sueldo = 1
    for sueldo_aleatorio in sueldos_trabajadores:
        trabajador_sueldo *= sueldo_aleatorio
    return int(trabajador_sueldo ** (1 / len(sueldos_trabajadores)))

def ver_estadisticas():
    limpiar_pantalla()
    print("Estadisticas de sueldos")
    print(f"Precio mas alto: ${precio_mas_alto(sueldos_trabajadores)}")
    print(f"Precio mas bajo: ${precio_mas_bajo(sueldos_trabajadores)}")
    print(f"Promedio de sueldos: ${promedio(sueldos_trabajadores)}")
    print(f"Medida geometrica de sueldos: ${media_geometrica(sueldos_trabajadores)}")
    
def generar_archivo():
    csv_content = "Nombre empleado,Sueldo Base,Descuento Salud,Descuento AFP,Sueldo Liquido\n"
    for i in range(len(trabajadores)):
        sueldo_aleatorio = sueldos_trabajadores[i]
        descuento_salud = sueldo_aleatorio * 0.07
        descuento_AFP = sueldo_aleatorio * 0.12
        sueldo_liquido = sueldo_aleatorio - descuento_salud - descuento_AFP 
        csv_content += f"{trabajadores[i]},{sueldo_aleatorio},{descuento_salud},{descuento_AFP},{sueldo_liquido}\n"
    return csv_content

def guardar_reporte():
    limpiar_pantalla()
    csv_content = generar_archivo()
    with open('reporte_sueldos.csv', 'w') as file:
        file.write(csv_content)
    print("\nReporte de sueldos generado correctamente en 'reporte_sueldos.csv'")