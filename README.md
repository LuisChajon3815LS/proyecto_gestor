# 🚀 GESTOR ACADÉMICO PRO: Control Total de Calificaciones en Consola

***

## 🎯 El Desafío Académico

La vida universitaria exige un constante **malabarismo**. Múltiples asignaturas, tareas variadas, exámenes con distintos pesos y **ponderaciones** hacen que llevar un control manual sea tedioso y propenso a errores. Esta falta de claridad sobre el rendimiento real dificulta saber dónde enfocar el esfuerzo y genera incertidumbre.

---

## ✨ Nuestra Solución: El Gestor de Notas Académicas (GNA)

El **Gestor de Notas Académicas** es una herramienta esencial, desarrollada íntegramente en **Python**, diseñada para terminar con la incertidumbre. Este programa ligero y rápido te permite:

* ✅ **Registrar** cursos y todas sus evaluaciones con **ponderaciones exactas**.
* ✅ **Calcular** automáticamente el **promedio general ponderado** y el de cada materia.
* ✅ **Generar reportes** de rendimiento limpios y concisos.

**¿El resultado?** Un **control total y transparente** de tu avance académico, accesible directamente desde la **consola**, permitiéndote identificar rápidamente tus puntos fuertes y las áreas que requieren mayor dedicación.

***

## ⚙️ Especificaciones Clave del Sistema

### 📋 Requisitos Funcionales (¿Qué puede hacer?):

El sistema se opera a través de un **menú intuitivo** que debe incluir, como mínimo, estas funciones:

1.  **Registro Único:** Añadir nuevos cursos y sus respectivas evaluaciones (Nombre, Tipo de Evaluación, Nota Obtenida y Ponderación).
2.  **Vista Global:** Mostrar todas las notas y evaluaciones registradas de manera clara y ordenada.
3.  **Cálculo Maestro:** Calcular y presentar el **promedio general ponderado** de todas las asignaturas.
4.  **Consulta Detallada:** Buscar notas por curso específico para ver el detalle de avance.

### 🛠️ Requisitos Técnicos (¿Cómo está construido?):

* **Tecnología:** Desarrollo exclusivo en **Python**.
* **Interfaz:** Ejecución 100% en **línea de comandos (consola)**.
* **Restricciones de Código:** **Prohibido** el uso de librerías o módulos externos; solo se permite el uso de estructuras y funciones nativas de Python.
* **Estructura Base:** Implementación obligatoria de **bucles** y **condicionales** conforme al diseño de pseudocódigo.

***

## 🚀 Avance del Proyecto (Versión Inicial)

En esta fase de desarrollo, se implementaron sólidos fundamentos para garantizar la escalabilidad y el mantenimiento del código:

### 🗂 Estructuras y Datos

* **Uso de Listas Dinámicas:** Se empleó una estructura de **lista principal** para almacenar los cursos. Esto permite la gestión eficiente y dinámica de la información (**agregar**, **mostrar** y **eliminar**).

### ⚙️ Organización y Modularidad

* **Organización Lógica con Funciones:** El código fue segmentado en **funciones reutilizables** (ej. `agregar_curso()`, `mostrar_cursos()`, `eliminar_curso()`), mejorando la **legibilidad** y el **mantenimiento**.
* **Modularización:** El proyecto se organizó en **módulos** separados, dividiendo la lógica de gestión de datos de la interfaz principal de ejecución.
* **Gestión de Cursos:** Se añadió la funcionalidad para **Eliminación de cursos** registrados, manteniendo la base de datos limpia y precisa.
