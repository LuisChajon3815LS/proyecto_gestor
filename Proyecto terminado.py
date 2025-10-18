
# Listas principales
cursos = []
historial = []        # Pila (LIFO) para el historial de acciones
cola_revision = []    # Cola (FIFO) para cursos pendientes de revisión
contador_cursos = 0   # Contador global para asignar IDs únicos

# --------------------------------
# Funciones de validacion
# --------------------------------

def validar_nota(nota):
    """Verifica que la nota esté en el rango de 0 a 100."""
    return 0 <= nota <= 100

def validar_creditos(creditos):
    """Verifica que los créditos estén en el rango de 1 a 10."""
    return 1 <= creditos <= 10

def validar_opcion_menu(opcion):
    """Verifica que la opción del menú sea válida (1 a 15)."""
    return 1 <= opcion <= 15

# --------------------------------
# Funciones de menu
# --------------------------------

def imprimir_menu():
    """Muestra el menú principal con el formato de 'MI GESTOR DE NOTAS' y el estado actual."""
    print("\n" + "*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(" 🌟 MI GESTOR DE NOTAS 🌟 ")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f" 📑 Cursos registrados: {len(cursos)}")
    print(f" 📚 Historial de acciones: {len(historial)}")
    print(f" 🕒 Cursos en revision: {len(cola_revision)}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(" 1. Agregar materia nueva")
    print(" 2. Mostrar todas las notas")
    print(" 3. Sacar mi promedio general")
    print(" 4. ¿Cuántas materias gané/perd?")
    print(" 5. Buscar materia por nombre (Lineal)")
    print(" 6. Buscar materia por codigo (Binaria)")
    print(" 7. Cambiar nota de una materia")
    print(" 8. Quitar una materia")
    print(" 9. Ordenar notas de menor a mayor (Burbuja)")
    print("10. Ordenar por nombre (Insercion)")
    print("11. Ordenar por codigo (Seleccion)")
    print("12. Enviar materia a Revisión (Cola)")
    print("13. Atender primera Revisión")
    print("14. Ver Historial de Acciones (Pila)")
    print("15. Salir del programa")

def leer_opcion():
    """Lee y valida la opción del menú seleccionada por el usuario."""
    entrada = input("Elige una opción (1-15): ")
    try:
        opcion = int(entrada)
        if validar_opcion_menu(opcion):
            return opcion
        return -1
    except ValueError:
        return -1

# --------------------------------
# Funciones principales
# --------------------------------

def registrar_curso():
    """Permite al usuario ingresar los datos de un nuevo curso."""
    global contador_cursos
    
    print("\n--- AGREGAR MATERIA NUEVA ---")
    
    codigo = input("Identificador de la materia (ej: 008): ").strip()
    if not codigo:
        print("❌ Error: El identificador no puede estar vacio")
        return
    
    # Validar código único
    for curso in cursos:
        if curso['codigo'].lower() == codigo.lower():
            print("❌ Error: Ya existe una materia con ese identificador")
            return
    
    nombre = input("Nombre de la materia: ").strip()
    if len(nombre) < 3:
        print("❌ Error: El nombre debe tener al menos 3 caracteres")
        return
    
    try:
        nota = float(input("Nota obtenida (0-100): "))
        if not validar_nota(nota):
            print("❌ Error: La nota tiene que ir de 0 a 100")
            return
    except ValueError:
        print("❌ Error: Por favor, escribe un número válido para la nota")
        return
    
    try:
        creditos = int(input("Créditos de la materia (1-6): "))
        if not validar_creditos(creditos):
            print("❌ Error: Los créditos deben ser entre 1 y 6")
            return
    except ValueError:
        print("❌ Error: Por favor, escribe un número válido para los créditos")
        return
    
    contador_cursos += 1
    
    curso = {
        "id": contador_cursos,
        "codigo": codigo.upper(),
        "nombre": nombre,
        "nota": nota,
        "creditos": creditos
    }
    
    cursos.append(curso)
    historial.append(f"Registrada materia: {nombre} ({codigo})")
    print("✅ ¡Materia agregada con éxito!")

def mostrar_cursos():
    """Muestra todos los cursos registrados en formato de tabla."""
    if len(cursos) == 0:
        print("No tienes materias registradas aún. ¡Empieza por la opción 1!")
        return
    
    print("\n--- TUS MATERIAS Y NOTAS ---")
    print(f"{'ID':<5} {'Código':<10} {'Materia':<25} {'Nota':<8} {'Créditos':<10}")
    print("-" * 63)
    
    for curso in cursos:
        print(f"{curso['id']:<5} {curso['codigo']:<10} {curso['nombre']:<25} {curso['nota']:<8.2f} {curso['creditos']:<10}")

def calcular_promedio():
    """Calcula el promedio ponderado de todos los cursos."""
    if len(cursos) == 0:
        print("No hay notas para calcular. ¡Agrega tus materias primero!")
        return
    
    suma_ponderada = 0
    total_creditos = 0
    
    for curso in cursos:
        suma_ponderada += curso['nota'] * curso['creditos']
        total_creditos += curso['creditos']
    
    if total_creditos == 0:
        print("No hay créditos válidos para calcular el promedio.")
        return
        
    promedio = suma_ponderada / total_creditos
    print(f"📈 Tu promedio ponderado es: {promedio:.2f}")
    historial.append("Calculado promedio general")

def contar_aprobados_reprobados():
    """Cuenta y muestra la cantidad de cursos aprobados (>= 61) y reprobados."""
    if len(cursos) == 0:
        print("No hay notas para hacer el conteo.")
        return
    
    aprobados = sum(1 for curso in cursos if curso['nota'] >= 61)
    reprobados = len(cursos) - aprobados
    
    print(f"🎉 Materias Aprobadas (Ganadas): {aprobados}")
    print(f"😔 Materias Reprobadas (Perdidas): {reprobados}")

# --------------------------------
# Funciones de busqueda
# --------------------------------

def buscar_por_nombre():
    """Busca un curso por nombre usando búsqueda Lineal."""
    if len(cursos) == 0:
        print("No hay materias registradas para buscar.")
        return
    
    nombre_buscar = input("\nEscribe el nombre de la materia que buscas: ").strip()
    encontrado = False
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"\n✅ ¡Materia encontrada! Detalles:")
            print(f"ID: {cursos[i]['id']}")
            print(f"Código: {cursos[i]['codigo']}")
            print(f"Nombre: {cursos[i]['nombre']}")
            print(f"Nota: {cursos[i]['nota']}")
            print(f"Créditos: {cursos[i]['creditos']}")
            encontrado = True
            historial.append(f"Busqueda lineal: {nombre_buscar}")
            break
    
    if not encontrado:
        print("Materia no encontrada. ¡Revisa la ortografía!")

def buscar_por_codigo_binaria():
    """Busca un curso por código usando búsqueda Binaria (requiere lista ordenada)."""
    if len(cursos) == 0:
        print("No hay materias registradas para buscar.")
        return
    
    # Se asegura que la lista esté ordenada por código antes de la búsqueda binaria
    print("Ordenando materias por código para búsqueda binaria...")
    ordenar_seleccion_por_codigo()
    
    codigo_buscar = input("\nIngrese el código de la materia a buscar: ").strip().upper()
    
    izquierda = 0
    derecha = len(cursos) - 1
    encontrado = False
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if cursos[medio]['codigo'] == codigo_buscar:
            print(f"\n✅ ¡Materia encontrada! Detalles:")
            print(f"ID: {cursos[medio]['id']}")
            print(f"Código: {cursos[medio]['codigo']}")
            print(f"Nombre: {cursos[medio]['nombre']}")
            print(f"Nota: {cursos[medio]['nota']}")
            print(f"Créditos: {cursos[medio]['creditos']}")
            encontrado = True
            historial.append(f"Busqueda binaria: {codigo_buscar}")
            break
        elif cursos[medio]['codigo'] < codigo_buscar:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    if not encontrado:
        print("Materia no encontrada. ¡Revisa el código!")

# --------------------------------
# Funciones de actualizacion
# --------------------------------

def actualizar_nota():
    """Busca un curso por nombre y permite cambiar su nota."""
    if len(cursos) == 0:
        print("No hay materias registradas para actualizar.")
        return
    
    nombre_buscar = input("\nEscribe el nombre de la materia a la que quieres cambiar la nota: ").strip()
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            print(f"\nMateria: {cursos[i]['nombre']} (Nota actual: {cursos[i]['nota']:.2f})")
            
            try:
                nueva_nota = float(input("Ingresa la nueva nota (0-100): "))
                if not validar_nota(nueva_nota):
                    print("❌ Error: La nota debe estar entre 0 y 100.")
                    return
                
                nota_anterior = cursos[i]['nota']
                cursos[i]['nota'] = nueva_nota
                historial.append(f"Actualizada nota de {cursos[i]['nombre']}: {nota_anterior:.2f} -> {nueva_nota:.2f}")
                print("✅ ¡Nota actualizada con éxito!")
                return
            except ValueError:
                print("❌ Error: Ingresa un número válido.")
                return
    
    print("Materia no encontrada.")

def eliminar_curso():
    """Busca un curso por nombre y lo elimina de la lista."""
    if len(cursos) == 0:
        print("No hay materias registradas para eliminar.")
        return
    
    nombre_buscar = input("\nEscribe el nombre de la materia que quieres eliminar: ").strip()
    
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            curso_eliminado = cursos[i]
            historial.append(f"Eliminada materia: {curso_eliminado['nombre']} ({curso_eliminado['codigo']})")
            del cursos[i]
            print("🗑️ ¡Materia eliminada con éxito!")
            return
    
    print("Materia no encontrada.")

# --------------------------------
# Algoritmos de ordenamiento
# --------------------------------

def ordenar_burbuja():
    """Ordena los cursos por nota de menor a mayor usando Bubble Sort."""
    n = len(cursos)
    if n == 0:
        print("No hay materias registradas")
        return
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if cursos[j]['nota'] > cursos[j + 1]['nota']:
                # Intercambio
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    
    print("\n✅ Materias ordenadas por nota (menor a mayor)")
    historial.append("Ordenamiento burbuja por nota")

def ordenar_insercion():
    """Ordena los cursos por nombre alfabéticamente usando Insertion Sort."""
    n = len(cursos)
    if n == 0:
        print("No hay materias registradas")
        return
    
    for i in range(1, n):
        key = cursos[i]
        j = i - 1
        # Mueve los elementos mayores que key, a una posición adelante
        while j >= 0 and cursos[j]['nombre'].lower() > key['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
    
    print("\n✅ Materias ordenadas alfabéticamente por nombre")
    historial.append("Ordenamiento insercion por nombre")

def ordenar_seleccion_por_codigo():
    """Ordena los cursos por código alfabéticamente usando Selection Sort."""
    n = len(cursos)
    if n == 0:
        return
    
    for i in range(n - 1):
        min_idx = i
        # Encuentra el elemento mínimo
        for j in range(i + 1, n):
            if cursos[j]['codigo'].lower() < cursos[min_idx]['codigo'].lower():
                min_idx = j
        
        # Intercambia el elemento mínimo encontrado con el primer elemento no ordenado
        if min_idx != i:
            cursos[i], cursos[min_idx] = cursos[min_idx], cursos[i]
    
    print("\n✅ Materias ordenadas por código (alfabéticamente)")
    historial.append("Ordenamiento seleccion por codigo")

# --------------------------------
# Funciones de cola (FIFO)
# --------------------------------

def agregar_revision():
    """Agrega un curso a la cola de revisión (FIFO)."""
    if len(cursos) == 0:
        print("No hay materias registradas")
        return
    
    nombre = input("\nEscribe el nombre de la materia a enviar a revisión: ").strip()
    
    for curso in cursos:
        if curso['nombre'].lower() == nombre.lower():
            # Evitar duplicados en la cola de revisión
            for c in cola_revision:
                if c['id'] == curso['id']:
                    print("Esta materia ya está en la cola de revisión")
                    return
            
            cola_revision.append(curso)
            print(f"Curso '{nombre}' enviado a la cola de revisión")
            historial.append(f"Agregado a revision: {nombre}")
            return
    
    print("Materia no encontrada")

def atender_revision():
    """Saca y muestra el primer curso de la cola de revisión (FIFO)."""
    if len(cola_revision) == 0:
        print("No hay materias esperando en la cola de revisión.")
        return
    
    # .pop(0) remueve y retorna el primer elemento (el que lleva más tiempo esperando)
    curso = cola_revision.pop(0)
    print(f"➡️ Atendiendo la primera revisión: {curso['nombre']}")
    print(f"Código: {curso['codigo']}")
    print(f"Nota actual: {curso['nota']:.2f}")
    historial.append(f"Atendida revision: {curso['nombre']}")

# --------------------------------
# Funciones de pila (LIFO)
# --------------------------------

def mostrar_historial():
    """Muestra el historial de acciones (Pila), mostrando la más reciente primero."""
    if len(historial) == 0:
        print("El historial (bitácora) de acciones está vacío.")
        return
    
    print("\n--- BITÁCORA DE ACCIONES (Lo más reciente primero) ---")
    
    # Recorre la lista de atrás hacia adelante para simular el LIFO
    for i in range(len(historial) - 1, -1, -1):
        print(f" - {historial[i]}")

# --------------------------------
# Programa principal
# --------------------------------

def main():
    """Función principal que inicia y controla el flujo del programa."""
    print("\n" + "================================================")
    print("  🌟 ¡BIENVENIDO A TU GESTOR DE NOTAS PERSONAL! 🌟")
    print("================================================")
    
    while True:
        imprimir_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            registrar_curso()
        elif opcion == 2:
            mostrar_cursos()
        elif opcion == 3:
            calcular_promedio()
        elif opcion == 4:
            contar_aprobados_reprobados()
        elif opcion == 5:
            buscar_por_nombre()
        elif opcion == 6:
            buscar_por_codigo_binaria()
        elif opcion == 7:
            actualizar_nota()
        elif opcion == 8:
            eliminar_curso()
        elif opcion == 9:
            ordenar_burbuja()
        elif opcion == 10:
            ordenar_insercion()
        elif opcion == 11:
            ordenar_seleccion_por_codigo()
        elif opcion == 12:
            agregar_revision()
        elif opcion == 13:
            atender_revision()
        elif opcion == 14:
            mostrar_historial()
        elif opcion == 15:
            print("👋 ¡Adiós! Volveremos pronto a revisar esas notas.")
            break
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del menú.")
        
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()