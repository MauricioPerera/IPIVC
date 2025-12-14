# Flujo de Trabajo del Equipo (Human-Driven)

Este documento explica cómo coordinarse cuando **tú (humano)** estás usando múltiples IAs para modificar el repositorio compartido.

## Principio Fundamental: "Tú eres el Proxy"
Tus IAs no tienen permiso de escritura directo en el repositorio compartido (main branch). Tú eres el único que puede hacer commit/push. Por tanto, tú eres el filtro de calidad y seguridad.

## Paso a Paso para el Integrante del Equipo

### 1. Inicio de Tarea (Tu Responsabilidad)
1.  **Verifica Terreno**: Ejecuta `python tools/session_manager.py` (Opción 1).
    *   El script hará `git pull` automático.
    *   ¿Alguien más está tocando el módulo que necesitas?
    *   *Si sí*: Habla con ese humano.
    *   *Si no*: Procede.
2.  **Reserva**: Ejecuta `python tools/session_manager.py` (Opción 2).
    *   Crea tu sesión: `@tu_usuario - Feature X`.
    *   El script hará `git commit` y `git push` automáticamente.
    *   *Ahora el resto del equipo remoto sabe que esa zona es tuya.*

### 2. Orquestación de IAs (Tu Magia)
Ahora que tienes el "bloqueo", puedes soltar a tus IAs.
*   **Genera Contexto**: Ejecuta `python tools/context_generator.py`.
*   **Alimenta a tus IAs**: Pega el contenido de `CURRENT_CONTEXT.prompt.md` en:
    *   Tu chat con GPT-4 (para ideas/arquitectura).
    *   Tu IDE Cursor/Trae (para código).
    *   Tu Agente de Terminal (para scripts).
*   **Instrucción de Seguridad**: Pega también el contenido de `ai_instructions/agent_mandate.md` para alinear a todas tus IAs con las reglas del proyecto.

### 3. Integración (Tu Filtro)
Tus IAs te darán código. Quizás una te da una función y otra te da los tests.
1.  Unifica el código en tu rama local.
2.  Verifica que funciona.
3.  Verifica que NO tocaste archivos fuera de tu "Reserva".

### 4. Cierre (Tu Entrega)
1.  Cuando todo esté verde (tests pasan):
2.  Ejecuta `python tools/session_manager.py` (Opción 3) para borrar tu sesión.
3.  Haz el commit final con tu código + la eliminación de la sesión.
4.  `git push`.

## Gestión de Conflictos
Si necesitas tocar un archivo que ya está reservado por otro humano:
1.  **No le pidas a tu IA que lo sobrescriba.**
2.  Contacta al humano dueño de la sesión.
3.  Acuerden quién hace qué.
