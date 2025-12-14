# IPIVC Protocol Roadmap (Improvements)

Este documento detalla las mejoras planificadas para evolucionar el protocolo de la versión actual (V1.0 Git-Based) a una versión Enterprise (V2.0).

## Áreas de Mejora Identificadas

### 1. Latencia y Atomicidad (Critical)
*   **Problema**: Git no es una base de datos en tiempo real. Existe un delay entre el `push` de A y el `pull` de B.
*   **Solución V2 (LokiVector)**:
    *   Reemplazar el backend de Git por **LokiVector** (Embedded + HTTP Server).
    *   **Ventaja**: Persistencia local a prueba de fallos (Crash-Safe) y capacidad de búsqueda vectorial para conflictos semánticos.
    *   **Arquitectura**: Una instancia central de LokiVector actúa como "Semáforo" accesible vía API REST por todos los agentes remotos.
*   **Mitigación Actual**: `session_manager.py` ahora realiza una verificación "Post-Push" para confirmar que el bloqueo persistió.

### 2. Experiencia de Usuario (Friction)
*   **Problema**: Copiar y pegar contextos manualmente es tedioso.
*   **Solución V2**:
    *   **VS Code Extension**: Un panel lateral que muestra las sesiones activas y permite bloquear con un clic.
    *   **CLI Auto-Copy**: Scripts que inyectan el contexto directamente en el portapapeles (`pyperclip`).

### 3. Integración CI/CD (Enforcement)
*   **Problema**: Nada impide físicamente que un humano ignore el protocolo y haga push.
*   **Solución V2**:
    *   **GitHub Action**: Un workflow que revisa si los archivos modificados en el PR estaban "reservados" por el autor en `memory/active_sessions/`. Si no, falla el check.

### 4. Granularidad Inteligente
*   **Problema**: Definir archivos uno por uno es lento.
*   **Solución V2**:
    *   Soporte nativo para "Feature Flags" en el bloqueo.
    *   Análisis de dependencia automático (Si tocas `User`, bloquea `UserAuth` automáticamente).

---
*Documento generado por el equipo de Arquitectura IPIVC.*
