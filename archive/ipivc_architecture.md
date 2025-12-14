# Arquitectura del Protocolo IPIVC y Sistema de Memoria Vectorial

## 1. Introducción al Protocolo IPIVC

El protocolo IPIVC (Investiga, Planifica, Implementa, Verifica, Corrige) es una evolución del modelo IPI (Investiga, Planifica, Implementa), diseñado para estandarizar y regular el flujo de trabajo de agentes de codificación en un entorno de desarrollo colaborativo (`vibecoding`). La adición de las fases de **Verificación** y **Corrección** formaliza el proceso de aseguramiento de calidad y retroalimentación, creando un ciclo de desarrollo más robusto y resiliente.

El objetivo principal de IPIVC es asegurar que cada cambio enviado a un repositorio de código siga un proceso ordenado, basado en especificaciones claras, y validado a través de un sistema de memoria persistente y contextual. Esto minimiza la introducción de errores, mejora la mantenibilidad del código y alinea el trabajo del agente con los objetivos del proyecto y las expectativas del usuario.

## 2. Fases del Protocolo IPIVC

Cada fase del protocolo tiene un propósito definido, con entradas, actividades y salidas claras.

| Fase | Propósito | Actividades Clave | Salidas | Herramientas/Skills | 
| :--- | :--- | :--- | :--- | :--- | 
| **Investiga** | Comprender el problema y los requisitos | - Análisis de requisitos del usuario<br>- Búsqueda de información y soluciones existentes<br>- Consulta de la memoria de proyecto (L2) | - Resumen de hallazgos<br>- Identificación de Gaps de conocimiento | `search`, `browser`, `file` | 
| **Planifica** | Crear un plan de acción detallado | - Desglose de tareas<br>- Creación de especificaciones formales (SDD)<br>- Definición de casos de prueba | - Plan de implementación<br>- Archivos de especificación (`specs.md`)<br>- Checklists de validación | `plan`, `file` | 
| **Implementa** | Escribir y ejecutar el código | - Generación de código a partir de specs<br>- Desarrollo de funcionalidades<br>- Ejecución de pruebas unitarias | - Código fuente<br>- Resultados de pruebas unitarias | `file`, `shell` | 
| **Verifica** | Asegurar la calidad y el cumplimiento | - Revisión de código (peer review simulado)<br>- Ejecución de pruebas de integración y validación<br>- Comparación con las especificaciones | - Reporte de verificación<br>- Lista de discrepancias y bugs | `match`, `shell` | 
| **Corrige** | Solucionar los problemas encontrados | - Depuración de código<br>- Aplicación de correcciones<br>- Re-ejecución de pruebas | - Código corregido<br>- Parches y commits | `file`, `shell` | 

## 3. Arquitectura del Sistema de Memoria de Dos Niveles

El sistema de memoria es fundamental para la autonomía y el aprendizaje continuo del agente. Se divide en dos niveles jerárquicos, donde el Nivel 1 (L1) tiene mayor peso y persistencia.

### Nivel 1: Memoria de Proyecto (Largo Plazo)

Esta memoria es la "bóveda de conocimiento" del proyecto. Es persistente a través de múltiples sesiones y agentes que trabajen en el mismo proyecto. Su función es almacenar el conocimiento consolidado y las "verdades" del proyecto.

- **Contenido**:
    - **Arquitectura del software**: Diagramas, decisiones de diseño.
    - **Estándares de código**: Guías de estilo, patrones de diseño.
    - **Especificaciones**: Requisitos funcionales y no funcionales consolidados.
    - **Conocimiento del dominio**: Terminología, reglas de negocio.
    - **Procedimientos**: Pasos para tareas comunes (despliegues, tests).
- **Implementación**: Se implementará utilizando **LokiVector**, almacenando los embeddings de los documentos de conocimiento y permitiendo búsquedas semánticas.

### Nivel 2: Memoria Agente-Usuario (Corto Plazo)

Esta es la memoria de trabajo o "scratchpad" del agente para la interacción actual con el usuario. Es volátil y se reinicia con cada nueva tarea o sesión, aunque puede ser promovida selectivamente al Nivel 1.

- **Contenido**:
    - **Contexto de la conversación**: Historial del chat, preguntas del usuario.
    - **Archivos y datos de la sesión**: Archivos subidos, resultados intermedios.
    - **Preferencias inmediatas**: 
Estilos de respuesta solicitados.
- **Estado de la tarea actual**: Pasos completados, próximos pasos.
- **Implementación**: Se gestionará en memoria durante la sesión activa, utilizando una instancia temporal de LokiJS para búsquedas rápidas.

### Flujo de Interacción entre Niveles de Memoria

El flujo de información entre los dos niveles de memoria es crucial para el aprendizaje y la adaptación del agente.

1.  **Consulta Inicial**: Al iniciar una tarea, el agente consulta primero la **Memoria de Proyecto (L1)** para obtener el contexto, estándares y especificaciones relevantes.
2.  **Operación en L2**: Durante la interacción con el usuario, el agente opera principalmente en la **Memoria Agente-Usuario (L2)**, almacenando el contexto de la conversación y los artefactos de la sesión.
3.  **Promoción a L1**: Al finalizar una fase o tarea, el agente identifica conocimiento nuevo y valioso en L2 (ej. una nueva preferencia del usuario, una solución a un problema recurrente) y lo promueve a L1. Este proceso requiere una validación para asegurar que la información es precisa y generalizable.
4.  **Actualización de L1**: La información promovida se convierte en embeddings y se almacena en LokiVector, enriqueciendo la base de conocimiento del proyecto para futuras tareas y otros agentes.

## 4. Implementación con LokiVector

LokiVector, una evolución de LokiJS, es la tecnología central para el sistema de memoria. Su naturaleza embebida y su capacidad de búsqueda vectorial lo hacen ideal para este propósito.

- **Almacenamiento**: Los documentos de conocimiento (especificaciones, guías de estilo, etc.) se dividirán en fragmentos (chunks), se convertirán en embeddings y se almacenarán en una colección de LokiVector.
- **Búsqueda Semántica**: Cuando el agente necesite consultar la memoria, generará un embedding de su consulta y realizará una búsqueda de similitud en LokiVector para encontrar los fragmentos de conocimiento más relevantes.
- **Persistencia**: La base de datos de LokiVector para la Memoria de Proyecto (L1) se persistirá en el sistema de archivos, asegurando su durabilidad entre sesiones.

## 5. Diagrama de Flujo del Proceso IPIVC

```mermaid
graph TD
    A[Start] --> B{1. Investiga};
    B --> C{2. Planifica};
    C --> D{3. Implementa};
    D --> E{4. Verifica};
    E -- Discrepancias --> F{5. Corrige};
    F --> D;
    E -- OK --> G[End];

    subgraph Memoria
        M1[L1: Memoria Proyecto<br>(LokiVector)];
        M2[L2: Memoria Agente-Usuario<br>(LokiJS en memoria)];
    end

    B -- Consulta --> M1;
    B -- Almacena --> M2;
    C -- Consulta --> M1;
    C -- Almacena --> M2;
    D -- Consulta --> M2;
    E -- Consulta --> M1;
    F -- Consulta --> M2;
    G -- Promueve --> M1;
```
