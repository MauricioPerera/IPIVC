# El Estándar de Vibecoding en Equipo: Protocolo IPIVC

**Versión 1.0**

**Autor: Manus AI**

## Resumen Ejecutivo

Este documento presenta el **Estándar de Vibecoding en Equipo**, un marco de trabajo integral diseñado para regular y optimizar la colaboración entre agentes de codificación de inteligencia artificial en proyectos de software complejos. El estándar introduce el **Protocolo IPIVC (Investiga, Planifica, Implementa, Verifica, Corrige)**, una metodología de ciclo de vida de desarrollo que formaliza el aseguramiento de la calidad y la mejora continua. Se complementa con una **arquitectura de memoria de dos niveles** basada en una base de datos vectorial embebida (LokiVector), un sistema de **especificaciones formales** inspirado en el Spec-Driven Development (SDD), y un ecosistema de **skills y tools estandarizados** para garantizar la consistencia y la reutilización de procesos.

El objetivo de este estándar es proporcionar un flujo de trabajo ordenado y regulado que permita a cualquier agente de codificación integrarse en un proyecto, comprender su contexto y contribuir de manera segura y predecible, minimizando errores y maximizando la eficiencia del desarrollo colaborativo.

## 1. Fundamentos del Estándar

La creciente complejidad del desarrollo de software asistido por IA requiere de marcos de trabajo que vayan más allá de la simple generación de código. El `vibecoding` en equipo, o la colaboración entre múltiples agentes de IA en un mismo proyecto, presenta desafíos únicos en cuanto a consistencia, calidad y comunicación. Este estándar se basa en la investigación de las mejores prácticas de la industria en ingeniería de software y las adapta al paradigma de los agentes de IA.

### 1.1. Principios Clave

- **Mejora Continua**: Inspirado en las prácticas de revisión de código de Google, el estándar favorece la aprobación de cambios que representen una mejora neta para la salud del código, incluso si no son perfectos [1].
- **Desarrollo Orientado a Especificaciones (SDD)**: El desarrollo se guía por especificaciones formales y explícitas que describen el comportamiento del software, reduciendo la ambigüedad y las alucinaciones del modelo [2].
- **Memoria Persistente y Contextual**: Los agentes deben tener la capacidad de recordar y aprender de interacciones pasadas, utilizando una arquitectura de memoria que distingue entre el conocimiento del proyecto a largo plazo y el contexto de la sesión a corto plazo [3].
- **Estandarización y Reutilización**: Los procesos comunes se encapsulan en *skills* y *tools* estandarizados, promoviendo la consistencia y la eficiencia en todo el equipo de agentes.

---


## 2. Arquitectura del Protocolo IPIVC y Sistema de Memoria Vectorial

### 2.1. Introducción al Protocolo IPIVC

El protocolo IPIVC (Investiga, Planifica, Implementa, Verifica, Corrige) es una evolución del modelo IPI (Investiga, Planifica, Implementa), diseñado para estandarizar y regular el flujo de trabajo de agentes de codificación en un entorno de desarrollo colaborativo (`vibecoding`). La adición de las fases de **Verificación** y **Corrección** formaliza el proceso de aseguramiento de calidad y retroalimentación, creando un ciclo de desarrollo más robusto y resiliente.

El objetivo principal de IPIVC es asegurar que cada cambio enviado a un repositorio de código siga un proceso ordenado, basado en especificaciones claras, y validado a través de un sistema de memoria persistente y contextual. Esto minimiza la introducción de errores, mejora la mantenibilidad del código y alinea el trabajo del agente con los objetivos del proyecto y las expectativas del usuario.

### 2.2. Fases del Protocolo IPIVC

Cada fase del protocolo tiene un propósito definido, con entradas, actividades y salidas claras.

| Fase | Propósito | Actividades Clave | Salidas | Herramientas/Skills | 
| :--- | :--- | :--- | :--- | :--- | 
| **Investiga** | Comprender el problema y los requisitos | - Análisis de requisitos del usuario<br>- Búsqueda de información y soluciones existentes<br>- Consulta de la memoria de proyecto (L2) | - Resumen de hallazgos<br>- Identificación de Gaps de conocimiento | `search`, `browser`, `file` | 
| **Planifica** | Crear un plan de acción detallado | - Desglose de tareas<br>- Creación de especificaciones formales (SDD)<br>- Definición de casos de prueba | - Plan de implementación<br>- Archivos de especificación (`specs.md`)<br>- Checklists de validación | `plan`, `file` | 
| **Implementa** | Escribir y ejecutar el código | - Generación de código a partir de specs<br>- Desarrollo de funcionalidades<br>- Ejecución de pruebas unitarias | - Código fuente<br>- Resultados de pruebas unitarias | `file`, `shell` | 
| **Verifica** | Asegurar la calidad y el cumplimiento | - Revisión de código (peer review simulado)<br>- Ejecución de pruebas de integración y validación<br>- Comparación con las especificaciones | - Reporte de verificación<br>- Lista de discrepancias y bugs | `match`, `shell` | 
| **Corrige** | Solucionar los problemas encontrados | - Depuración de código<br>- Aplicación de correcciones<br>- Re-ejecución de pruebas | - Código corregido<br>- Parches y commits | `file`, `shell` | 

### 2.3. Arquitectura del Sistema de Memoria de Dos Niveles

El sistema de memoria es fundamental para la autonomía y el aprendizaje continuo del agente. Se divide en dos niveles jerárquicos, donde el Nivel 1 (L1) tiene mayor peso y persistencia.

#### Nivel 1: Memoria de Proyecto (Largo Plazo)

Esta memoria es la "bóveda de conocimiento" del proyecto. Es persistente a través de múltiples sesiones y agentes que trabajen en el mismo proyecto. Su función es almacenar el conocimiento consolidado y las "verdades" del proyecto.

- **Contenido**:
    - **Arquitectura del software**: Diagramas, decisiones de diseño.
    - **Estándares de código**: Guías de estilo, patrones de diseño.
    - **Especificaciones**: Requisitos funcionales y no funcionales consolidados.
    - **Conocimiento del dominio**: Terminología, reglas de negocio.
    - **Procedimientos**: Pasos para tareas comunes (despliegues, tests).
- **Implementación**: Se implementará utilizando **LokiVector**, almacenando los embeddings de los documentos de conocimiento y permitiendo búsquedas semánticas.

#### Nivel 2: Memoria Agente-Usuario (Corto Plazo)

Esta es la memoria de trabajo o "scratchpad" del agente para la interacción actual con el usuario. Es volátil y se reinicia con cada nueva tarea o sesión, aunque puede ser promovida selectivamente al Nivel 1.

- **Contenido**:
    - **Contexto de la conversación**: Historial del chat, preguntas del usuario.
    - **Archivos y datos de la sesión**: Archivos subidos, resultados intermedios.
    - **Preferencias inmediatas**: Estilos de respuesta solicitados.
    - **Estado de la tarea actual**: Pasos completados, próximos pasos.
- **Implementación**: Se gestionará en memoria durante la sesión activa, utilizando una instancia temporal de LokiJS para búsquedas rápidas.

### 2.4. Flujo de Interacción entre Niveles de Memoria

El flujo de información entre los dos niveles de memoria es crucial para el aprendizaje y la adaptación del agente.

1.  **Consulta Inicial**: Al iniciar una tarea, el agente consulta primero la **Memoria de Proyecto (L1)** para obtener el contexto, estándares y especificaciones relevantes.
2.  **Operación en L2**: Durante la interacción con el usuario, el agente opera principalmente en la **Memoria Agente-Usuario (L2)**, almacenando el contexto de la conversación y los artefactos de la sesión.
3.  **Promoción a L1**: Al finalizar una fase o tarea, el agente identifica conocimiento nuevo y valioso en L2 (ej. una nueva preferencia del usuario, una solución a un problema recurrente) y lo promueve a L1. Este proceso requiere una validación para asegurar que la información es precisa y generalizable.
4.  **Actualización de L1**: La información promovida se convierte en embeddings y se almacena en LokiVector, enriqueciendo la base de conocimiento del proyecto para futuras tareas y otros agentes.

### 2.5. Implementación con LokiVector

LokiVector, una evolución de LokiJS, es la tecnología central para el sistema de memoria. Su naturaleza embebida y su capacidad de búsqueda vectorial lo hacen ideal para este propósito.

- **Almacenamiento**: Los documentos de conocimiento (especificaciones, guías de estilo, etc.) se dividirán en fragmentos (chunks), se convertirán en embeddings y se almacenarán en una colección de LokiVector.
- **Búsqueda Semántica**: Cuando el agente necesite consultar la memoria, generará un embedding de su consulta y realizará una búsqueda de similitud en LokiVector para encontrar los fragmentos de conocimiento más relevantes.
- **Persistencia**: La base de datos de LokiVector para la Memoria de Proyecto (L1) se persistirá en el sistema de archivos, asegurando su durabilidad entre sesiones.

### 2.6. Diagrama de Flujo del Proceso IPIVC

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

## 3. Especificaciones Formales, Skills y Tools Estandarizados

### 3.1. Introducción a la Estandarización

Para que el protocolo IPIVC sea efectivo en un entorno de `vibecoding` en equipo, es crucial estandarizar los artefactos y procesos que utilizan los agentes de codificación. La estandarización asegura que todos los agentes, independientemente de su implementación subyacente, operen bajo las mismas reglas, produzcan resultados consistentes y colaboren de manera predecible. Este documento define tres pilares de estandarización: **Especificaciones Formales**, **Skills Estandarizados** y **Tools Estandarizados**.

### 3.2. Especificaciones Formales (Orientadas a Specs)

Inspirado en el **Spec-Driven Development (SDD)**, el protocolo IPIVC utiliza especificaciones formales como la principal fuente de verdad para la fase de **Implementa**. Una especificación bien definida reduce la ambigüedad, guía la generación de código y sirve como base para la fase de **Verifica**.

#### Estructura del Archivo de Especificación (`spec.md`)

Cada tarea de desarrollo debe comenzar con la creación de un archivo `spec.md`. Este archivo debe seguir una estructura clara para ser fácilmente interpretable tanto por agentes como por humanos.

```markdown
# Especificación: [Nombre del Feature o Tarea]

## 1. Resumen de Requisitos (Qué y Por Qué)

- **Requisito de Negocio**: Descripción en lenguaje natural del objetivo de negocio.
- **Usuario Objetivo**: A quién afecta este cambio.
- **Valor Aportado**: El beneficio esperado tras la implementación.

## 2. Especificaciones Técnicas (Cómo)

- **Stack Tecnológico**: Lenguajes, frameworks, librerías involucradas.
- **Contratos de Interfaz**: Endpoints de API, esquemas de datos (JSON Schema), firmas de funciones.
- **Restricciones Arquitectónicas**: Patrones de diseño a seguir (ej. Singleton, Factory), capas de la aplicación a modificar.
- **Invariantes**: Condiciones que deben mantenerse siempre ciertas.

## 3. Criterios de Aceptación (Given/When/Then)

Descripción del comportamiento esperado utilizando el formato BDD (Behavior-Driven Development).

**Escenario 1: [Nombre del Escenario]**
- **Given**: El estado inicial del sistema.
- **When**: La acción o evento que se produce.
- **Then**: El resultado esperado y verificable.

**Escenario 2: [Nombre del Escenario]**
- ...
```

### 3.3. Skills y Tools Estandarizados

Para promover la reutilización y la consistencia, se define una jerarquía de **Skills** y **Tools**. Los *Tools* son acciones atómicas y de bajo nivel, mientras que los *Skills* son orquestaciones de *Tools* para realizar tareas complejas.

#### Tools: Bloques de Construcción Atómicos

Un *Tool* es un script o comando que realiza una única tarea. Deben ser independientes y tener una interfaz de entrada/salida bien definida. Se almacenan en un directorio `tools/` del proyecto.

| Tool | Descripción | Ejemplo de Invocación | 
| :--- | :--- | :--- | 
| `tool_linter` | Ejecuta un linter (ej. ESLint) sobre un archivo o directorio. | `python tools/linter.py --file=src/component.js` | 
| `tool_formatter` | Formatea el código según las reglas del proyecto (ej. Prettier). | `python tools/formatter.py --file=src/component.js` | 
| `tool_test_runner` | Ejecuta un conjunto de pruebas específicas (ej. Jest, Pytest). | `python tools/test_runner.py --test-file=tests/test_auth.py` | 
| `tool_commit` | Crea un commit siguiendo la convención de Conventional Commits. | `python tools/commit.py --type=feat --scope=auth --message="Implementa login"` | 

#### Skills: Orquestación de Tareas Complejas

Un *Skill* es un script que define una secuencia de llamadas a *Tools* para lograr un objetivo de alto nivel. Los *Skills* encapsulan las mejores prácticas y los flujos de trabajo del equipo. Se almacenan en un directorio `skills/`.

### 3.4. Integración en el Flujo IPIVC

Las especificaciones, skills y tools se integran de forma natural en el ciclo de vida de IPIVC.

- **Investiga**: El agente consulta la memoria L1 para encontrar `spec.md` y `skills/` relevantes de tareas pasadas.
- **Planifica**: El agente crea o actualiza el `spec.md` para la tarea actual.
- **Implementa**: El agente genera código que cumple con el `spec.md`.
- **Verifica**: El agente utiliza el `skill_validate_code` (que a su vez usa `tool_linter`, `tool_test_runner`, etc.) para verificar el código contra los criterios de aceptación del `spec.md`.
- **Corrige**: Si la verificación falla, el agente depura y corrige el código, y vuelve a ejecutar el skill de validación hasta que pase.
- **Finalización**: Una vez verificado, el agente utiliza el `skill_commit_and_push` para integrar el cambio en el repositorio.

## 4. Guía de Implementación y Prototipo

Para demostrar la viabilidad del estándar, se ha desarrollado un prototipo funcional en JavaScript que simula la arquitectura de memoria de dos niveles utilizando `lokijs` como base para el conceptual `LokiVector`.

### 4.1. Estructura del Proyecto del Prototipo

```
/ipivc_prototype
|-- /memory
|   |-- lokivector_memory.js       # Implementación de la Memoria L1 (Proyecto)
|   |-- agent_user_memory.js       # Implementación de la Memoria L2 (Agente-Usuario)
|   |-- example_usage.js           # Ejemplo de flujo IPIVC
|-- package.json                   # Dependencias y scripts
```

### 4.2. Memoria de Proyecto (L1) - `lokivector_memory.js`

Este módulo simula la memoria persistente del proyecto. Aunque utiliza `lokijs`, implementa una función de búsqueda de similitud de coseno para emular la capacidad de búsqueda vectorial de `LokiVector`.

**Características Clave:**
- **Persistencia**: La base de datos se guarda en el sistema de archivos.
- **Búsqueda Semántica (Simulada)**: Incluye un método `searchSimilar` que calcula la similitud de coseno entre un vector de consulta y los embeddings almacenados.
- **Gestión de Conocimiento**: Permite almacenar, actualizar, eliminar y recuperar fragmentos de conocimiento (specs, skills, etc.).

```javascript
// Ejemplo de búsqueda en lokivector_memory.js
searchSimilar(queryEmbedding, type = null, topK = 5) {
  // ...
  const results = candidates.map(doc => ({
    ...doc,
    similarity: this._cosineSimilarity(queryEmbedding, doc.embedding),
  }));
  results.sort((a, b) => b.similarity - a.similarity);
  return results.slice(0, topK);
}
```

### 4.3. Memoria Agente-Usuario (L2) - `agent_user_memory.js`

Este módulo gestiona el estado de la sesión actual. Es una clase en memoria que almacena el historial de la conversación, archivos subidos, progreso de tareas y preferencias del usuario para la sesión activa.

**Características Clave:**
- **Volatilidad**: La información se mantiene solo durante la sesión activa.
- **Estado Completo de la Sesión**: Captura todos los artefactos relevantes de la interacción.
- **Exportación e Importación**: Permite guardar y restaurar el estado de la sesión, útil para auditorías o para reanudar tareas.

```javascript
// Ejemplo de exportación de estado en agent_user_memory.js
exportState() {
  return {
    conversationHistory: this.conversationHistory,
    uploadedFiles: this.uploadedFiles,
    taskProgress: this.taskProgress,
    userPreferences: this.getAllUserPreferences(),
    sessionMetadata: this.getSessionMetadata(),
  };
}
```

## 5. Conclusión

El Estándar de Vibecoding en Equipo IPIVC proporciona un marco robusto y extensible para el desarrollo de software colaborativo por parte de agentes de IA. Al formalizar el ciclo de vida del desarrollo, estandarizar los artefactos y procesos, y proporcionar un sistema de memoria inteligente, este estándar sienta las bases para la creación de equipos de agentes de codificación más eficientes, predecibles y seguros.

La implementación de este estándar no solo mejorará la calidad y la mantenibilidad del código generado por IA, sino que también facilitará la colaboración y la transferencia de conocimiento entre diferentes agentes y en diferentes proyectos, marcando un paso importante hacia la industrialización del desarrollo de software asistido por inteligencia artificial.

## 6. Referencias

[1] Google. (s.f.). *The Standard of Code Review*. Google Engineering Practices. Recuperado de https://google.github.io/eng-practices/review/reviewer/standard.html

[2] Thoughtworks. (2025, 4 de diciembre). *Spec-driven development: Unpacking one of 2025’s key new AI-assisted engineering practices*. Recuperado de https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices

[3] Lozovsky, D. (2025, 14 de octubre). *How to Build AI That Actually Remembers: Your Complete Guide to Long-Term Memory in Agentic AI*. Medium. Recuperado de https://medium.com/@daniel.lozovsky/how-to-build-ai-that-actually-remembers-your-complete-guide-to-long-term-memory-in-agentic-ai-a233971ae5a8
