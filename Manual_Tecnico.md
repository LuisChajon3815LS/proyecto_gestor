# 🧾 Manual Técnico - Gestor de Notas Académicas

## 📘 Descripción General
El **Gestor de Notas Académicas** es un programa de consola desarrollado en **Python 3.x** que permite administrar materias, calificaciones y créditos, aplicando estructuras de datos (listas, pilas, colas) y algoritmos clásicos de búsqueda y ordenamiento.

---

## ⚙️ Tecnología

- **Lenguaje:** Python 3.x  
- **Tipo:** Aplicación de consola (interactiva)  
- **Dependencias:** Ninguna librería externa  
- **Ejecución:**  
  ```bash
  python gestor_notas.py
  ```

---

## 🧩 Organización del Código
El código se divide en **10 secciones principales**:

1. Variables globales  
2. Funciones de validación  
3. Funciones de menú  
4. Funciones principales (CRUD)  
5. Funciones de búsqueda  
6. Funciones de actualización  
7. Algoritmos de ordenamiento  
8. Funciones de cola (FIFO)  
9. Funciones de pila (LIFO)  
10. Programa principal  

---

## 📂 Variables Globales
```python
cursos = []          # Lista principal de materias registradas
historial = []       # Pila (LIFO) que guarda las acciones realizadas
cola_revision = []   # Cola (FIFO) de materias pendientes de revisión
contador_cursos = 0  # Contador global para IDs únicos
```

---

## 🧱 Estructura de un Curso
Cada curso se almacena como un diccionario:
```python
{
    "id": 1,                # ID único asignado automáticamente
    "codigo": "MAT101",     # Código o identificador del curso
    "nombre": "Matemáticas I",
    "nota": 85.5,           # Valor entre 0 y 100
    "creditos": 4           # Valor entre 1 y 6
}
```

---

## 🧮 Funciones de Validación

### `validar_nota(nota)`
- Verifica que la nota esté entre **0 y 100**.  
- Retorna: `True` o `False`

### `validar_creditos(creditos)`
- Verifica que los créditos estén entre **1 y 10** (aunque en el ingreso solo se permite 1–6).  
- Retorna: `True` o `False`

### `validar_opcion_menu(opcion)`
- Verifica que la opción del menú esté entre **1 y 15**.  
- Retorna: `True` o `False`

---

## 🔍 Búsqueda Lineal

```python
def buscar_por_nombre():
    for i in range(len(cursos)):
        if cursos[i]['nombre'].lower() == nombre_buscar.lower():
            # Encontrado
```

- **Complejidad:** O(n)  
- Recorre la lista completa elemento por elemento  
- Funciona con listas **no ordenadas**  
- **Desventaja:** lenta con grandes volúmenes de datos  

---

## ⚡ Búsqueda Binaria

```python
def buscar_por_codigo_binaria():
    ordenar_seleccion_por_codigo()  # Ordena primero por código
    
    izquierda = 0
    derecha = len(cursos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if cursos[medio]['codigo'] == codigo_buscar:
            # Encontrado
            break
```

- **Complejidad:** O(log n)  
- Divide la lista en mitades sucesivas  
- Requiere lista **ordenada** previamente  
- **Ventaja:** mucho más rápida que la búsqueda lineal  

---

## 🔢 Algoritmos de Ordenamiento

### 🫧 Ordenamiento Burbuja
```python
def ordenar_burbuja():
    for i in range(n - 1):
        for j in range(n - i - 1):
            if cursos[j]['nota'] > cursos[j + 1]['nota']:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
```
- **Ordena por:** nota (menor a mayor)  
- **Complejidad:** O(n²)  
- Intercambia elementos vecinos si están en el orden incorrecto  

---

### 🧩 Ordenamiento por Inserción
```python
def ordenar_insercion():
    for i in range(1, n):
        key = cursos[i]
        j = i - 1
        while j >= 0 and cursos[j]['nombre'].lower() > key['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = key
```
- **Ordena por:** nombre alfabéticamente  
- **Complejidad:** O(n²)  
- Similar a organizar cartas en la mano  

---

### 🔠 Ordenamiento por Selección
```python
def ordenar_seleccion_por_codigo():
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if cursos[j]['codigo'].lower() < cursos[min_idx]['codigo'].lower():
                min_idx = j
        if min_idx != i:
            cursos[i], cursos[min_idx] = cursos[min_idx], cursos[i]
```
- **Ordena por:** código alfabéticamente  
- **Complejidad:** O(n²)  
- Busca el menor elemento y lo coloca en su posición correcta  

---

## 🧱 Pila (LIFO)
Utilizada para el **historial de acciones**.

```python
historial = []

# Agregar
historial.append("Acción 1")
historial.append("Acción 2")

# Mostrar en orden inverso
for i in range(len(historial) - 1, -1, -1):
    print(historial[i])
```

- **Último en entrar, primero en salir**  
- `append()` agrega al final  
- `pop()` saca el último  
- Ideal para bitácoras o deshacer acciones  

---

## 🚦 Cola (FIFO)
Utilizada para la **cola de revisión**.

```python
cola_revision = []

# Agregar
cola_revision.append(curso1)
cola_revision.append(curso2)

# Atender el primero
curso = cola_revision.pop(0)
```

- **Primero en entrar, primero en salir**  
- `append()` agrega al final  
- `pop(0)` elimina del inicio  
- Simula una fila de espera  

---

## 🔁 Flujo del Programa

1. Mostrar menú principal  
2. Leer la opción ingresada  
3. Validar la opción  
4. Ejecutar la función correspondiente  
5. Mostrar resultados  
6. Esperar que el usuario presione **ENTER**  
7. Volver al paso 1  

El bucle continúa hasta que el usuario elige la opción **15 (Salir del programa)**.

---

## 📊 Complejidad de Algoritmos

| Algoritmo              | Complejidad | Descripción                             |
|------------------------|-------------|-----------------------------------------|
| Búsqueda Lineal        | O(n)        | Recorre todos los elementos             |
| Búsqueda Binaria       | O(log n)    | Divide la lista por mitades sucesivas   |
| Ordenamiento Burbuja   | O(n²)       | Compara elementos adyacentes            |
| Ordenamiento Inserción | O(n²)       | Inserta cada elemento en su posición    |
| Ordenamiento Selección | O(n²)       | Encuentra el mínimo y lo reubica        |

---

## 🧠 Funciones Principales (CRUD y Control)

| Función                         |                    Descripción                    |
|---------------------------------|---------------------------------------------------|
| `registrar_curso()`             | Agrega un nuevo curso validando datos             |
| `mostrar_cursos()`              | Muestra todos los cursos en tabla                 |
| `calcular_promedio()`           | Calcula el promedio ponderado                     |
| `contar_aprobados_reprobados()` | Cuenta materias ganadas (≥61) y perdidas (<61)    |
| `buscar_por_nombre()`           | Busca un curso por nombre (lineal)                |
| `buscar_por_codigo_binaria()`   | Busca un curso por código (binaria)               |
| `actualizar_nota()`             | Permite cambiar la nota de una materia            |
| `eliminar_curso()`              | Elimina una materia registrada                    |
| `ordenar_burbuja()`             | Ordena por nota de menor a mayor                  |
| `ordenar_insercion()`           | Ordena por nombre alfabéticamente                 |
| `ordenar_seleccion_por_codigo()`| Ordena por código (A–Z)                           |
| `agregar_revision()`            | Envía una materia a la cola de revisión           |
| `atender_revision()`            | Atiende la primera materia en la cola             |
| `mostrar_historial()`           | Muestra el historial (últimas acciones)           |
