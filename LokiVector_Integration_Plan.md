# Plan de Integración: LokiVector para IPIVC V2

## ¿Por qué LokiVector?
En lugar de usar Redis (que requiere infraestructura externa compleja) o Git (que es lento para tiempo real), usaremos **LokiVector** porque:
1.  **Embedded & Lightweight**: Se instala con `npm install`, perfecto para el enfoque "sin infraestructura" de IPIVC.
2.  **Vector Search (HNSW)**: Nos permite no solo bloquear por *nombre de archivo*, sino por *semántica*.
    *   *Ejemplo*: Si alguien bloquea "Gestión de Usuarios", LokiVector sabe que eso entra en conflicto con "UserLogin" aunque los archivos se llamen diferente.
3.  **HTTP Server Nativo**: Viene con una API REST lista para usar, resolviendo la comunicación remota.
4.  **Crash-Safe**: Garantiza que si el servidor se cae, los bloqueos no se pierden ni se corrompen.

## Arquitectura Propuesta

### 1. El Servidor de Semáforo (Central)
Una instancia de LokiVector corriendo en un servidor ligero (o en la máquina del Tech Lead).
*   **Colección**: `active_sessions`
*   **Schema**:
    ```json
    {
      "user": "@Alice",
      "task": "Fix Login",
      "files_locked": ["src/auth/*"],
      "embedding": [0.12, 0.98, ...] // Vector generado de la descripción de la tarea
    }
    ```

### 2. Detección de Conflictos Semánticos
Cuando `@Bob` intenta iniciar una sesión:
1.  Su herramienta genera un embedding de su tarea: "Refactorizar autenticación".
2.  Consulta a LokiVector: `active_sessions.findNearest(embedding_bob)`.
3.  **Resultado**: LokiVector detecta similitud con la tarea de `@Alice` ("Fix Login") y alerta del conflicto aunque los archivos no sean idénticos.

### 3. Implementación
1.  **Dependencia**: `@lokivector/core`
2.  **Auth**: API Keys simples para cada miembro del equipo.
3.  **Persistencia**: Adaptador de sistema de archivos (se guarda en `memory/loki.db`).

## Pasos de Migración
1.  Crear script `server/start_lokivector.js`.
2.  Actualizar `session_manager.py` para hacer peticiones HTTP en lugar de `git push`.
3.  Entrenar/Configurar un modelo de embeddings ligero (ej. ONNX) para generar vectores localmente.
