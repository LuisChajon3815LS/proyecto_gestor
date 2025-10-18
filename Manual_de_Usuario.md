# Manual de Usuario - Gestor de Notas Académicas

## 🧩 Descripción General
El **Gestor de Notas Académicas** es un programa en **Python** que permite registrar, organizar y analizar cursos universitarios usando estructuras de datos y algoritmos básicos.

Funciona completamente en consola y no necesita conexión a internet ni librerías adicionales.

---

## ⚙️ Instalación
No requiere instalación.  
Solo asegúrate de tener **Python 3.x** instalado en tu computadora.

Puedes verificarlo con:
```bash
python --version
```

---

## ▶️ Cómo ejecutar
1. Guarda el archivo con el nombre `gestor_notas.py`.
2. Abre la terminal o símbolo del sistema.
3. Navega hasta la carpeta donde guardaste el archivo.
4. Escribe:
```bash
python gestor_notas.py
```

---

## 📋 Opciones del Menú

### 1. Registrar nuevo curso
Agrega un curso con:
- **Código:** Identificador único (ej. MAT101)
- **Nombre:** Nombre del curso (ej. Matemáticas I)
- **Nota:** Entre 0 y 100
- **Créditos:** Entre 1 y 6  

> El sistema valida todos los campos antes de guardar.

---

### 2. Mostrar todos los cursos y notas
Muestra una tabla con todos los cursos registrados:
- ID  
- Código  
- Nombre  
- Nota  
- Créditos  

---

### 3. Calcular promedio general
Calcula el **promedio ponderado** según las notas y los créditos.

**Fórmula:**  
\[
\text{Promedio} = \frac{\sum(\text{nota} \times \text{créditos})}{\text{total de créditos}}
\]

---

### 4. Contar cursos aprobados y reprobados
Muestra:
- Cursos aprobados (nota ≥ 61)
- Cursos reprobados (nota < 61)

---

### 5. Buscar curso por nombre
Permite buscar un curso escribiendo su nombre completo o parcial.  
Usa **búsqueda lineal**.

- **Uso:** Ideal para listas pequeñas o sin ordenar.  
- **Complejidad:** O(n)

---

### 6. Buscar curso por código
Busca un curso por su código usando **búsqueda binaria**, mucho más rápida.  
La lista se ordena automáticamente antes de buscar.

- **Uso:** Para búsqueda exacta por código.  
- **Complejidad:** O(log n)

---

### 7. Actualizar nota de un curso
Cambia la nota de un curso existente, validando el nuevo valor entre 0 y 100.  
Guarda la acción en el historial.

---

### 8. Eliminar un curso
Elimina un curso de la lista principal de manera permanente.  
La acción también se guarda en el historial.

---

### 9. Ordenar cursos por nota (Burbuja)
Ordena los cursos de **menor a mayor nota** usando el algoritmo **Burbuja**.  
- **Uso:** Mostrar cursos en orden de rendimiento.
- **Complejidad:** O(n²)

---

### 10. Ordenar cursos por nombre (Inserción)
Ordena los cursos alfabéticamente por nombre.  
Usa el algoritmo **Inserción**, eficiente para listas pequeñas.

- **Complejidad:** O(n²)

---

### 11. Ordenar cursos por código (Selección)
Ordena los cursos alfabéticamente por código de curso.  
Usa el algoritmo **Selección**.

- **Complejidad:** O(n²)

---

### 12. Agregar curso a revisión (Cola)
Agrega un curso a la **cola de revisión**.  
Esta estructura funciona como una **Cola FIFO** (First In, First Out).

- **append()** → agrega al final  
- **pop(0)** → atiende el primero agregado  

---

### 13. Atender revisión
Atiende el **primer curso en la cola**, lo elimina y muestra su información.

---

### 14. Mostrar historial de acciones (Pila)
Muestra el historial de acciones realizadas por el usuario.  
Funciona como una **Pila LIFO** (Last In, First Out).  

- **append()** → agrega acción al final  
- **pop()** → elimina la última acción  

Las más recientes se muestran primero.

---

### 15. Salir
Finaliza el programa y cierra la ejecución.

---

## 🧠 Estructura de Datos

### Curso
Cada curso se guarda como un diccionario:
```python
{
    "id": 1,
    "codigo": "008",
    "nombre": "Matemáticas I",
    "nota": 85.5,
    "creditos": 5
}
```

### Listas principales
- `cursos`: Lista de todos los cursos registrados.  
- `historial`: Pila que guarda las acciones.  
- `cola_revision`: Cola de cursos pendientes de revisión.

---

## 🔍 Algoritmos Implementados

| Algoritmo        | Uso                | Complejidad | Descripción                     |
|------------------|--------------------|-------------|---------------------------------|
| Búsqueda Lineal  | Buscar por nombre  | O(n)        | Revisa cada elemento            |
| Búsqueda Binaria | Buscar por código  | O(log n)    | Divide la lista por la mitad    |
| Burbuja          | Ordenar por nota   | O(n²)       | Compara elementos vecinos       |
| Inserción        | Ordenar por nombre | O(n²)       | Inserta en la posición correcta |
| Selección        | Ordenar por código | O(n²)       | Encuentra el mínimo y lo mueve  |

---

## ✅ Validaciones
El programa valida todos los datos ingresados:

| Campo              |          Regla        |
|--------------------|-----------------------|
| **Nota**           | Entre 0 y 100         |
| **Créditos**       | Entre 1 y 6           |
| **Código**         | No vacío y único      |
| **Nombre**         | Al menos 3 caracteres |
| **Opción de menú** | Entre 1 y 15          |

---

## 🧾 Requisitos
- **Python 3.x**
- No requiere librerías externas
- Sistema operativo: Windows, Linux o macOS

---

## 💡 Recomendaciones
- Guarda el archivo `.py` en una carpeta fácil de acceder.  
- No cierres la consola mientras el programa esté ejecutándose.  
- Revisa el historial para mantener control de tus acciones.  

---

© 2025 - Gestor de Notas Académicas
