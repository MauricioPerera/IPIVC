# Vibecoding IPIVC Standard v2.0 (Human-Centric Team)

Este repositorio define el estándar de colaboración para un **Equipo de X Humanos** (Desarrolladores, Arquitectos, QA) que trabajan sobre el mismo código base asistidos por IA.

> 🌐 **Documentación Completa**: [https://mauricioperera.github.io/IPIVC/](https://mauricioperera.github.io/IPIVC/)

## ¿Cómo funciona esto en la práctica? (Concepto Operativo)

**Es una estructura de carpetas y scripts que vive DENTRO de tu repositorio Git.**

### Arquitectura Híbrida v2.0
IPIVC v2.0 combina dos capas de seguridad:
1.  **Git (Persistencia)**: Bloqueo de archivos visible para todos.
2.  **LokiVector (Semántica)**: Un "Oráculo Central" que detecta conflictos de intención (ej. "Arreglar Auth" vs "Login Refactor") en tiempo real.

### Tu configuración de trabajo diaria:
1.  **Ventana 1 (Tu IDE + IA)**: Donde tú y tu Agente (Trae, Cursor, etc.) escriben código.
2.  **Ventana 2 (Terminal Dedicada)**: Donde ejecutas las herramientas de coordinación.

---

## El Protocolo IPIVC como "Contrato Humano"

### 1. Investiga (Sync)
*   Ejecuta `python tools/session_manager.py`.
*   El sistema consulta a **Git** y a **LokiVector** para ver quién está trabajando en qué.

### 2. Planifica (Lock & Spec)
*   Reservas tu zona de trabajo.
*   **CRÍTICO**: Defines las **Especificaciones Funcionales** en tu archivo de sesión.
    *   *Ejemplo*: "El login debe bloquear tras 3 intentos fallidos".
*   El sistema bloquea esos recursos para el resto del equipo.

### 3. Implementa (AI Execution)
*   Generas el contexto con `python tools/context_generator.py`.
*   Alimentas a tu IA con ese contexto + `AGENTS.md`.
*   Tu IA trabaja sabiendo qué archivos puede tocar y cuáles no.

### 4. Verifica (Auto-Audit)
*   Ejecuta `python tools/verify_task.py`.
*   El script verifica:
    1.  **Scope**: ¿Tu IA tocó archivos prohibidos?
    2.  **Specs**: ¿Se cumplen los requisitos funcionales?
    3.  **Tests**: ¿Pasan las pruebas automáticas?
*   Genera un reporte `AI_FEEDBACK_REPORT.md` para tu IA.

### 5. Corrige (Loop)
*   Entregas el reporte a tu IA.
*   Repites el ciclo hasta que todo esté verde (✅).
*   Liberas el bloqueo y haces push.

## Estructura del Proyecto
- `server/`: Servidor LokiVector para detección de conflictos semánticos.
- `tools/`:
    - `session_manager.py`: Cliente de coordinación.
    - `verify_task.py`: Auditor de calidad y alcance.
    - `context_generator.py`: Puente para la IA.
- `memory/`: Base de datos de conocimiento del proyecto.
- `AGENTS.md`: Estándar abierto de instrucciones para Agentes.
