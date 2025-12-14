# Vibecoding IPIVC Standard (Human-Centric Team)

Este repositorio define el estándar de colaboración para un **Equipo de X Humanos** (Desarrolladores, Arquitectos, QA) que trabajan sobre el mismo código base.

## ¿Cómo funciona esto en la práctica? (Concepto Operativo)

**No es un software complejo** que instalas en tu sistema operativo.
**Es una estructura de carpetas y scripts que vive DENTRO de tu repositorio Git.**

### 1. ¿Es una plantilla?
**SÍ.**
Para usarlo, copias las carpetas `tools/`, `memory/` y los archivos `.md` a la raíz de tu proyecto (sea Python, Node, Java, etc.).

Tu proyecto se verá así:
```text
/mi-proyecto-web
├── /src              <-- Tu código fuente normal
├── /tests            <-- Tus tests
├── /tools            <-- (IPIVC) Scripts de coordinación
├── /memory           <-- (IPIVC) Base de datos de conocimiento
├── TEAM_WORKFLOW.md  <-- (IPIVC) Las reglas del juego
└── README.md
```

### 2. ¿Se ejecuta en paralelo?
**NO** como un servicio en segundo plano que consume RAM.
**SÍ** en el sentido de que lo usas *mientras* programas.

**Tu configuración de trabajo diaria:**
1.  **Ventana 1 (Tu IDE + IA)**: Donde tú y tu Agente (Trae, Cursor, etc.) escriben código (`src/`).
2.  **Ventana 2 (Terminal Dedicada)**: Donde ejecutas `python tools/session_manager.py` para hablar con el equipo remoto.
    *   *Ejemplo*: "¡Atención equipo, voy a editar `UserAuth.ts`, bloqueo activado!" (El script hace el git push por ti).

### 3. El Mecanismo "Mágico"
El sistema usa **tu propio repositorio Git** como servidor de coordinación.
*   Cuando ejecutas una herramienta de IPIVC, esta lee/escribe archivos pequeños en `memory/` y hace `git push/pull` automáticamente.
*   **Resultado**: Sin servidores extra, todo el equipo sabe en tiempo real qué está haciendo el resto.

---

## El Modelo de Trabajo
1.  **El Humano es el Responsable**: Cada integrante es un humano.
2.  **Asistencia AI Ilimitada**: Cada humano puede utilizar **N** herramientas de IA (Agentes, LLMs, Scripts, IDEs inteligentes) para realizar su trabajo.
    *   *Ejemplo*: Un humano puede usar ChatGPT para investigar, GitHub Copilot para autocompletar y un Agente Autónomo para refactorizar, todo en la misma tarea.
3.  **Heterogeneidad**:
    *   Distintos roles (Frontend, Backend, Security).
    *   Distintos niveles de expertise (Junior, Senior).
    *   Distintos toolsets de IA.

## El Problema
Cuando X humanos despliegan múltiples IAs sobre un mismo repo, el riesgo de colisión y degradación de arquitectura es masivo. Las IAs no se "hablan" entre ellas; los humanos sí deben hacerlo.

## El Protocolo IPIVC como "Contrato Humano"

El protocolo regula la interacción del **Humano** con el repositorio compartido.

### 1. Investiga (Human Awareness)
*   El humano usa `tools/session_manager.py` para ver qué zonas del código están bloqueadas por otros humanos.
*   **Automáticamente** el script hace `git pull` para asegurar que ves el estado real del remoto.
*   El humano decide qué herramientas de IA usará según la tarea.

### 2. Planifica (Human Strategy)
*   El humano define el alcance y **BLOQUEA** los archivos en `memory/active_sessions/`.
*   **Automáticamente** el script hace `git push` del archivo de bloqueo.
*   *Importante*: Al bloquear, el humano se hace responsable de que **ninguna** de sus IAs rompa ese bloqueo.

### 3. Implementa (AI Execution / Human Supervision)
*   El humano orquesta a sus agentes.
*   Carga el contexto del proyecto (`tools/context_generator.py`) en sus herramientas.
*   Supervisa que el código generado cumpla con `security.spec.md`.

### 4. Verifica (Human Gatekeeper)
*   Antes de subir cambios, el humano valida que el trabajo combinado de sus IAs funcione.
*   El humano ejecuta los tests y linters.

### 5. Corrige
*   El humano itera con sus IAs hasta cumplir los estándares.

## Estructura de Soporte
- `memory/active_sessions/`: Tablero de control donde los **Humanos** marcan su territorio.
- `tools/`: Scripts para que el humano gestione el contexto que le da a sus IAs.
