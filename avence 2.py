Cursos = []

def ver_menu():
    """Muestra el menú principal de opciones."""
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
    print("13. Salir del programa")

def leer_eleccion():
    """Pide al usuario que elija una opción del menú."""
    entrada = input("Elige una opción (1-7, 13): ")
    try:
        eleccion = int(entrada)
        if eleccion in [1, 2, 3, 4, 5, 6, 7, 13]:
            return eleccion
        return -1
    except ValueError:
        return -1

def ingresar_materia():
    """Permite al usuario registrar una nueva materia con sus datos."""
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
    print("✅ ¡Materia agregada con éxito!")

def listar_materias():
    """Muestra una lista de todas las materias y notas registradas."""
    if len(materias) == 0:
        print("No tienes materias registradas aún. ¡Empieza por la opción 1!")
        return
    
    print("\n--- TUS MATERIAS Y NOTAS ---")
    print(f"{'ID':<10} {'Materia':<25} {'Nota':<8} {'Créditos':<10}")
    print("-" * 55)
    
    for materia in materias:
        print(f"{materia['id']:<10} {materia['nombre']:<25} {materia['nota']:<8} {materia['creditos']:<10}")

def calcular_promedio_total():
    """Calcula y muestra el promedio ponderado de todas las materias."""
    if len(materias) == 0:
        print("No hay notas para calcular. ¡Agrega tus materias primero!")
        return
    
    suma_total_ponderada = 0
    creditos_totales = 0
    
    for materia in materias:
        # Nota * Créditos (Ponderación)
        suma_total_ponderada += materia['nota'] * materia['creditos']
        creditos_totales += materia['creditos']
    
    if creditos_totales == 0:
         print("No hay créditos válidos para calcular el promedio.")
         return
         
    promedio_final = suma_total_ponderada / creditos_totales
    print(f"📈 Tu promedio ponderado es: {promedio_final:.2f}")

def contar_resultados():
    """Cuenta cuántas materias están aprobadas (>= 61) y reprobadas."""
    if len(materias) == 0:
        print("No hay notas para hacer el conteo.")
        return
    
    ganadas = 0
    perdidas = 0
    
    for materia in materias:
        if materia['nota'] >= 61:
            ganadas += 1
        else:
            perdidas += 1
    
    print(f"🎉 Materias Aprobadas (Ganadas): {ganadas}")
    print(f"😔 Materias Reprobadas (Perdidas): {perdidas}")

def buscar_materia_por_nombre():
    """Busca y muestra la información de una materia por su nombre."""
    if len(materias) == 0:
        print("No hay materias registradas para buscar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia que buscas: ")
    hallado = False
    
    for info in materias:
        if info['nombre'].lower() == nombre_buscado.lower():
            print(f"\n✅ ¡Materia encontrada! Detalles:")
            print(f"Identificador: {info['id']}")
            print(f"Nombre: {info['nombre']}")
            print(f"Nota: {info['nota']}")
            print(f"Créditos: {info['creditos']}")
            hallado = True
            break
    
    if not hallado:
        print("Materia no encontrada. ¡Revisa la ortografía!")

def cambiar_nota():
    """Permite al usuario actualizar la nota final de una materia."""
    if len(materias) == 0:
        print("No hay materias registradas para actualizar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia a la que quieres cambiar la nota: ")
    hallado = False
    
    for i in range(len(materias)):
        if materias[i]['nombre'].lower() == nombre_buscado.lower():
            print(f"Materia: {materias[i]['nombre']} (Nota actual: {materias[i]['nota']})")
            
            try:
                nueva_nota = float(input("Ingresa la nueva nota (0-100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print("❌ Error: La nota debe estar entre 0 y 100.")
                    return
                
                materias[i]['nota'] = nueva_nota
                print("✅ ¡Nota actualizada con éxito!")
                hallado = True
                break
            except ValueError:
                print("❌ Error: Ingresa un número válido.")
                return
    
    if not hallado:
        print("Materia no encontrada.")

def quitar_materia():
    """Elimina una materia de la lista por su nombre."""
    if len(materias) == 0:
        print("No hay materias registradas para eliminar.")
        return
    
    nombre_buscado = input("Escribe el nombre de la materia que quieres eliminar: ")
    
    for i in range(len(materias)):
        if materias[i]['nombre'].lower() == nombre_buscado.lower():
            del materias[i]
            print("🗑️ ¡Materia eliminada con éxito!")
            return
            
    print("Materia no encontrada.")

def iniciar_programa():
    """Función principal que ejecuta el bucle del programa."""
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
        elif eleccion == 13:
            print("👋 ¡Adiós! Volveremos pronto a revisar esas notas.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del menú.")

if __name__ == "__main__":
    iniciar_programa()
