## Matriz de Riesgos y Validaciones de Seguridad por Fase en IPIVC

### 1. Introducción a la Gestión de Riesgos en Equipos Heterogéneos

En un equipo de `vibecoding` con agentes de diferentes niveles de expertise, no todos los cambios pueden ser tratados de la misma manera. Un cambio en el sistema de autenticación por parte de un agente junior conlleva un riesgo inherentemente mayor que una modificación de estilos CSS por parte de un agente senior. Para gestionar esta complejidad, introducimos una **Matriz de Riesgos** y un sistema de **Validaciones de Seguridad por Fase**.

El objetivo es adaptar el rigor del protocolo IPIVC al nivel de riesgo de cada tarea, asegurando que los cambios más críticos reciban la supervisión y validación adecuadas, sin ralentizar innecesariamente las tareas de bajo riesgo.

### 2. Matriz de Clasificación de Riesgos

Antes de iniciar la fase de **Planifica**, cada tarea se clasifica según su nivel de riesgo potencial. El nivel de riesgo se determina evaluando dos ejes principales: **Impacto del Cambio** y **Nivel de Expertise del Agente**.

#### Eje 1: Impacto del Cambio (IC)

Se evalúa en una escala de 1 a 3, considerando los siguientes factores:

- **Criticidad del Componente**: ¿Afecta a un componente central (ej. autenticación, pagos, core de la aplicación)?
- **Sensibilidad de los Datos**: ¿Manipula datos sensibles (PII, credenciales, datos financieros)?
- **Exposición de la Superficie de Ataque**: ¿Introduce nuevos endpoints públicos o modifica los existentes?

| Nivel de IC | Descripción | Ejemplos |
| :--- | :--- | :--- |
| **3 (Alto)** | Modifica componentes críticos, maneja datos altamente sensibles o expande significativamente la superficie de ataque. | - Cambios en el flujo de login<br>- Implementación de una pasarela de pago<br>- Modificación de permisos de administrador |
| **2 (Medio)** | Afecta a funcionalidades de negocio importantes o maneja datos internos no críticos. | - Creación de un nuevo endpoint interno<br>- Modificación de la lógica de un carrito de compras<br>- Cambios en el perfil de usuario (sin PII) |
| **1 (Bajo)** | Cambios menores, no afectan la lógica de negocio crítica ni manejan datos sensibles. | - Correcciones de UI/UX<br>- Refactorización de código sin cambio de comportamiento<br>- Actualización de documentación |

#### Eje 2: Nivel de Expertise del Agente (NEA)

Se clasifica al agente asignado a la tarea.

| Nivel de NEA | Descripción |
| :--- | :--- |
| **Junior** | Agente con experiencia limitada o nuevo en el proyecto. Requiere supervisión. |
| **Senior** | Agente con amplia experiencia y conocimiento profundo del proyecto y de seguridad. |

#### Determinación del Nivel de Riesgo de la Tarea (NRT)

El Nivel de Riesgo de la Tarea se calcula combinando ambos ejes:

| | **IC: 1 (Bajo)** | **IC: 2 (Medio)** | **IC: 3 (Alto)** |
| :--- | :--- | :--- | :--- |
| **NEA: Senior** | **Bajo** | **Medio** | **Alto** |
| **NEA: Junior** | **Medio** | **Alto** | **Crítico** |

- **Crítico**: Requiere aprobación explícita de un agente senior (o un "Security Champion") antes de la implementación y una revisión exhaustiva en la fase de **Verifica**.

### 3. Validaciones de Seguridad por Fase (Security Gates)

El Nivel de Riesgo de la Tarea (NRT) determina el rigor de las validaciones de seguridad en cada fase del protocolo IPIVC.

| Fase IPIVC | Nivel de Riesgo: Bajo | Nivel de Riesgo: Medio | Nivel de Riesgo: Alto | Nivel de Riesgo: Crítico |
| :--- | :--- | :--- | :--- | :--- |
| **Planifica** | `spec.md` opcional. | `spec.md` requerido. | `spec.md` y `security.spec.md` requeridos. | `security.spec.md` debe ser revisado y aprobado por un agente senior. |
| **Implementa** | Implementación directa. | Seguir `spec.md`. | Seguir `spec.md` y `security.spec.md`. | Implementación en un `feature branch` aislado. Prohibido el merge directo a `main`. |
| **Verifica** | Linter y tests unitarios. | SAST automatizado. | SAST + Revisión manual de `security.spec.md` por un peer. | SAST + DAST (si aplica) + Revisión manual obligatoria por un agente senior. |
| **Corrige** | Corrección directa. | Corrección y re-verificación. | Corrección y re-verificación completa. | Corrección supervisada. Cada intento de corrección es revisado. |

### 4. Protocolo de Escalamiento y Decisión

Para gestionar los riesgos en equipos heterogéneos, es fundamental tener un protocolo de escalamiento claro.

- **Disparadores de Escalamiento**:
  - Una tarea es clasificada como de riesgo **Crítico**.
  - Un agente (sin importar su nivel) falla en la fase de **Verifica** más de 2 veces consecutivas en una tarea de riesgo **Alto**.
  - Un agente junior se encuentra con una amenaza en el `security.spec.md` que no sabe cómo mitigar.

- **Proceso de Escalamiento**:
  1. El agente que encuentra el problema detiene su trabajo y marca la tarea como `blocked:security_escalation`.
  2. El agente notifica a un **Agente Security Champion** (un rol predefinido, usualmente un agente senior con especialización en seguridad).
  3. El Security Champion revisa el `spec.md`, el `security.spec.md`, el código y los resultados de la verificación.
  4. El Security Champion puede tomar una de las siguientes acciones:
     - **Proporcionar Guía**: Ofrecer una solución o un enfoque para que el agente original pueda continuar.
     - **Realizar Pair Programming (Pair Vibecoding)**: Trabajar junto al agente original para resolver el problema.
     - **Tomar Posesión de la Tarea**: Si el riesgo es demasiado alto, el Security Champion puede reasignarse la tarea a sí mismo.

- **Registro de Decisiones**:
  - Todas las decisiones de escalamiento y sus resultados se registran en la **Memoria de Proyecto (L1)**. Esto enriquece la base de conocimiento, permitiendo que el equipo aprenda de los desafíos de seguridad y mejore las futuras SSF y checklists.
