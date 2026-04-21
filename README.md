# Calculadora de Instalaciones AA - Proyecto Final

Este proyecto consiste en una aplicación desarrollada en Python para la gestión y presupuesto de instalaciones de aire acondicionado, aplicando conceptos de Programación Orientada a Objetos (POO).

## 1. Fase de Análisis y Planificación

### Alcance y Requisitos Funcionales
* **Alcance:** El sistema permite a un técnico o cliente obtener un presupuesto estimado automatizando el cálculo de materiales y mano de obra. Filtra trabajos de alta complejidad que requieren inspección presencial.
* **Requisitos:**
    * Selección de capacidad del equipo (frigorías).
    * Validación de seguridad (bloqueo por altura o equipos > 5000 frigorías).
    * Cálculo de costos adicionales por metros excedentes de cañería (más de 3m).
    * Sumatoria de opcionales como "Kit de Materiales" e "Instalación Eléctrica".

### Diagrama de Clases (UML)
El sistema se basa en la clase `CalculadoraANN` que encapsula la lógica de precios y validaciones.


## 2. Fase de Desarrollo

* **Lenguaje:** Python utilizando el paradigma de Programación Orientada a Objetos (POO).
* **Control de Versiones:** Repositorio gestionado en GitHub.
* **Pruebas Unitarias:** Se validó el código mediante pruebas de escritorio asegurando que los cálculos de adicionales y las restricciones de seguridad funcionen correctamente.

## 3. Fase de Documentación y Entrega

### Memoria Técnica
El diseño se centró en la **mantenibilidad**. Al utilizar atributos privados para los costos base, el sistema permite actualizaciones de precios rápidas sin riesgo de romper la lógica del programa. La estructura permite escalar el software para incluir otros servicios en el futuro.

### Instrucciones de uso
1. Ejecutar el script `calculadora.py`.
2. Ingresar los datos solicitados por la interfaz de consola.
3. El sistema devolverá el presupuesto final o la indicación de visita técnica obligatoria.
