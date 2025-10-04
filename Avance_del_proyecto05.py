materias = []
bitacora = []         # Pila 
peticiones_cola = []  # Cola

def ver_menu():
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(" 🌟 MI GESTOR DE NOTAS 🌟 ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(" 1. Agregar materia nueva")
    print(" 2. Mostrar todas las notas")
    print(" 3. Sacar mi promedio general")
    print(" 4. ¿Cuántas materias gané/perd?")
    print(" 5. Buscar materia por nombre")
    print(" 6. Cambiar nota de una materia")
    print(" 7. Quitar una materia")
    print(" 8. Ordenar notas de menor a mayor (Burbuja)")
    print(" 9. Ordenar por nombre (Inserción)")
    print("10. Enviar materia a Revisión (Cola)")
    print("11. Atender primera Revisión")
    print("12. Ver Historial de Acciones (Pila)")
    print("13. Salir del programa")

def leer_eleccion():
    entrada = input("Elige una opción (1-13): ")
    try:
        eleccion = int(entrada)
        if eleccion in range(1, 14):
            return eleccion
        return -1
    except ValueError:
        return -1

# -------------------------------
#    FUNCIONES PRINCIPALES
# -------------------------------

def ingresar_materia():
    print("\n--- AGREGAR MATERIA NUEVA ---")
    
    id_materia = input("Identificador de la materia: ")
    nombre_materia = input("Nombre de la materia: ")
    
    try:
        nota_final = float(input("Nota obtenida (0-100): "))
        if nota_final < 0 or nota_final > 100:
            print("❌ Error: La nota tiene que ir de 0 a 100")
            return
    except ValueError:
        print("❌ Error: Por favor, escribe un número válido para la nota")
        return
    
    try:
        peso_credito = int(input("Créditos de la materia (1-10): "))
        if peso_credito < 1 or peso_credito > 10:
            print("❌ Error: Los créditos deben ser entre 1 y 10")
            return
    except ValueError:
        print("❌ Error: Por favor, escribe un número válido para los créditos")
        return
    
    info_materia = {
        "id": id_materia,
        "nombre": nombre_materia,
        "nota": nota_final,
        "creditos": peso_credito
    }
    
    materias.append(info_materia)
    bitacora.append(f"Registrada materia: {nombre_materia}")
    print("✅ ¡Materia agregada con éxito!")

def listar_materias():
    if len(materias) == 0:
        print("No tienes materias registradas aún. ¡Empieza por la opción 1!")
        return
    
    print("\n--- TUS MATERIAS Y NOTAS ---")
    print(f"{'ID':<10} {'Materia':<25} {'Nota':<8} {'Créditos':<10}")
    print("-" * 55)
    
    for materia in materias:
        print(f"{materia['id']:<10} {materia['nombre']:<25} {materia['nota']:<8} {materia['creditos']:<10}")

def calcular_promedio_total():
    if len(materias) == 0:
        print("No hay notas para calcular. ¡Agrega tus materias primero!")
        return
    
    suma_total_ponderada = 0
    creditos_totales = 0
    
    for materia in materias:
        suma_total_ponderada += materia['nota'] * materia['creditos']
        creditos_totales += materia['creditos']
    
    if creditos_totales == 0:
         print("No hay créditos válidos para calcular el promedio.")
         return
         
    promedio_final = suma_total_ponderada / creditos_totales
    print(f"📈 Tu promedio ponderado es: {promedio_final:.2f}")

def contar_resultados():
    if len(materias) == 0:
        print("No hay notas para hacer el conteo.")
        return
    
    ganadas = sum(1 for materia in materias if materia['nota'] >= 61)
    perdidas = len(materias) - ganadas
    
    print(f"🎉 Materias Aprobadas (Ganadas): {ganadas}")
    print(f"😔 Materias Reprobadas (Perdidas): {perdidas}")

def buscar_materia_por_nombre():
    if len(materias) == 0:
        print("No hay materias registradas para buscar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia que buscas: ")
    hallado = False
    
    for i in range(len(materias)):
        if materias[i]['nombre'].lower() == nombre_buscado.lower():
            print(f"\n✅ ¡Materia encontrada! Detalles:")
            print(f"Identificador: {materias[i]['id']}")
            print(f"Nombre: {materias[i]['nombre']}")
            print(f"Nota: {materias[i]['nota']}")
            print(f"Créditos: {materias[i]['creditos']}")
            hallado = True
            break
    
    if not hallado:
        print("Materia no encontrada. ¡Revisa la ortografía!")

def cambiar_nota():
    if len(materias) == 0:
        print("No hay materias registradas para actualizar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia a la que quieres cambiar la nota: ")
    
    for i in range(len(materias)):
        if materias[i]['nombre'].lower() == nombre_buscado.lower():
            print(f"Materia: {materias[i]['nombre']} (Nota actual: {materias[i]['nota']})")
            
            try:
                nueva_nota = float(input("Ingresa la nueva nota (0-100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("❌ Error: La nota debe estar entre 0 y 100.")
                    return
                
                materias[i]['nota'] = nueva_nota
                bitacora.append(f"Actualizada nota de: {materias[i]['nombre']}")
                print("✅ ¡Nota actualizada con éxito!")
                return
            except ValueError:
                print("❌ Error: Ingresa un número válido.")
                return
    
    print("Materia no encontrada.")

def quitar_materia():
    if len(materias) == 0:
        print("No hay materias registradas para eliminar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia que quieres eliminar: ")
    
    for i in range(len(materias)):
        if materias[i]['nombre'].lower() == nombre_buscado.lower():
            bitacora.append(f"Eliminada materia: {materias[i]['nombre']}")
            del materias[i]
            print("🗑️ ¡Materia eliminada con éxito!")
            return
            
    print("Materia no encontrada.")

# -------------------------------
#    ORDENAMIENTOS
# -------------------------------

def ordenar_por_nota():
    n = len(materias)
    if n == 0:
        print("No hay materias registradas")
        return
    
    for i in range(n-1):
        for j in range(n-i-1):
            if materias[j]['nota'] > materias[j+1]['nota']:
                materias[j], materias[j+1] = materias[j+1], materias[j]
    print("✅ Materias ordenadas por nota (menor a mayor)")

def ordenar_por_nombre():
    n = len(materias)
    if n == 0:
        print("No hay materias registradas")
        return
    
    for i in range(1, n):
        key = materias[i]
        j = i - 1
        while j >= 0 and materias[j]['nombre'].lower() > key['nombre'].lower():
            materias[j + 1] = materias[j]
            j -= 1
        materias[j + 1] = key
    print("✅ Materias ordenadas alfabéticamente por nombre")

# -------------------------------
#    COLA (Peticiones de Revisión)
# -------------------------------

def enviar_a_revision():
    if len(materias) == 0:
        print("No hay materias registradas")
        return
    
    nombre = input("Escribe el nombre de la materia a enviar a revisión: ")
    for materia in materias:
        if materia['nombre'].lower() == nombre.lower():
            peticiones_cola.append(materia)
            print(f"Curso '{nombre}' enviado a la cola de revisión")
            return
    print("Materia no encontrada")

def atender_revision():
    if len(peticiones_cola) == 0:
        print("No hay materias esperando en la cola de revisión.")
        return
    
    # .pop(0) quita el primer elemento (el que llegó primero)
    materia_atendida = peticiones_cola.pop(0)
    print(f"➡️ Atendiendo la primera revisión: {materia_atendida['nombre']}")

# -------------------------------
#    PILA (Bitácora de Acciones)
# -------------------------------

def ver_bitacora():
    if len(bitacora) == 0:
        print("El historial (bitácora) de acciones está vacío.")
        return
    
    print("\n--- BITÁCORA DE ACCIONES (Lo más reciente primero) ---")
    # Mostrar del último al primero (comportamiento de Pila)
    for accion in reversed(bitacora):
        print(f" - {accion}")

# -------------------------------
#    PROGRAMA PRINCIPAL
# -------------------------------

def iniciar_programa():
    while True:
        ver_menu()
        eleccion = leer_eleccion()
        
        if eleccion == 1:
            ingresar_materia()
        elif eleccion == 2:
            listar_materias()
        elif eleccion == 3:
            calcular_promedio_total()
        elif eleccion == 4:
            contar_resultados()
        elif eleccion == 5:
            buscar_materia_por_nombre()
        elif eleccion == 6:
            cambiar_nota()
        elif eleccion == 7:
            quitar_materia()
        elif eleccion == 8:
            ordenar_por_nota()
        elif eleccion == 9:
            ordenar_por_nombre()
        elif eleccion == 10:
            enviar_a_revision()
        elif eleccion == 11:
            atender_revision()
        elif eleccion == 12:
            ver_bitacora()
        elif eleccion == 13:
            print("👋 ¡Adiós! Volveremos pronto a revisar esas notas.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del menú.")

if __name__ == "__main__":

    iniciar_programa()
