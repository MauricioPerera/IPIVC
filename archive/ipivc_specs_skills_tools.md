# Especificaciones Formales, Skills y Tools Estandarizados para IPIVC

## 1. Introducción a la Estandarización

Para que el protocolo IPIVC sea efectivo en un entorno de `vibecoding` en equipo, es crucial estandarizar los artefactos y procesos que utilizan los agentes de codificación. La estandarización asegura que todos los agentes, independientemente de su implementación subyacente, operen bajo las mismas reglas, produzcan resultados consistentes y colaboren de manera predecible. Este documento define tres pilares de estandarización: **Especificaciones Formales**, **Skills Estandarizados** y **Tools Estandarizados**.

## 2. Especificaciones Formales (Orientadas a Specs)

Inspirado en el **Spec-Driven Development (SDD)**, el protocolo IPIVC utiliza especificaciones formales como la principal fuente de verdad para la fase de **Implementa**. Una especificación bien definida reduce la ambigüedad, guía la generación de código y sirve como base para la fase de **Verifica**.

### Estructura del Archivo de Especificación (`spec.md`)

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

### Ejemplo de `spec.md`

```markdown
# Especificación: Autenticación de Usuario con Email y Contraseña

## 1. Resumen de Requisitos

- **Requisito de Negocio**: Permitir que los usuarios inicien sesión en la plataforma utilizando su correo electrónico y una contraseña.
- **Usuario Objetivo**: Usuarios registrados.
- **Valor Aportado**: Acceso seguro a las funcionalidades personalizadas de la plataforma.

## 2. Especificaciones Técnicas

- **Stack Tecnológico**: Node.js, Express, LokiVector (para perfiles de usuario).
- **Contratos de Interfaz**: 
  - **Endpoint**: `POST /api/auth/login`
  - **Request Body**: `{ "email": "user@example.com", "password": "securepassword123" }`
  - **Response Success (200)**: `{ "token": "jwt_token" }`
  - **Response Error (401)**: `{ "error": "Credenciales inválidas" }`
- **Restricciones Arquitectónicas**: El servicio de autenticación debe ser un módulo separado. La contraseña debe ser hasheada con bcrypt antes de la comparación.
- **Invariantes**: El token JWT debe contener el `userId` y expirar en 24 horas.

## 3. Criterios de Aceptación

**Escenario 1: Login exitoso con credenciales válidas**
- **Given**: Un usuario existe en la base de datos con el email `test@example.com` y una contraseña hasheada.
- **When**: Se envía una petición `POST` a `/api/auth/login` con las credenciales correctas.
- **Then**: El servidor responde con un código de estado 200 y un cuerpo JSON que contiene un token JWT.

**Escenario 2: Login fallido con contraseña incorrecta**
- **Given**: Un usuario existe en la base de datos.
- **When**: Se envía una petición `POST` a `/api/auth/login` con una contraseña incorrecta.
- **Then**: El servidor responde con un código de estado 401 y un mensaje de error.
```

## 3. Skills y Tools Estandarizados

Para promover la reutilización y la consistencia, se define una jerarquía de **Skills** y **Tools**. Los *Tools* son acciones atómicas y de bajo nivel, mientras que los *Skills* son orquestaciones de *Tools* para realizar tareas complejas.

### Tools: Bloques de Construcción Atómicos

Un *Tool* es un script o comando que realiza una única tarea. Deben ser independientes y tener una interfaz de entrada/salida bien definida. Se almacenan en un directorio `tools/` del proyecto.

| Tool | Descripción | Ejemplo de Invocación | 
| :--- | :--- | :--- | 
| `tool_linter` | Ejecuta un linter (ej. ESLint) sobre un archivo o directorio. | `python tools/linter.py --file=src/component.js` | 
| `tool_formatter` | Formatea el código según las reglas del proyecto (ej. Prettier). | `python tools/formatter.py --file=src/component.js` | 
| `tool_test_runner` | Ejecuta un conjunto de pruebas específicas (ej. Jest, Pytest). | `python tools/test_runner.py --test-file=tests/test_auth.py` | 
| `tool_commit` | Crea un commit siguiendo la convención de Conventional Commits. | `python tools/commit.py --type=feat --scope=auth --message="Implementa login"` | 

### Skills: Orquestación de Tareas Complejas

Un *Skill* es un script que define una secuencia de llamadas a *Tools* para lograr un objetivo de alto nivel. Los *Skills* encapsulan las mejores prácticas y los flujos de trabajo del equipo. Se almacenan en un directorio `skills/`.

**Ejemplo de `skill_validate_and_commit.py`:**

```python
# skills/validate_and_commit.py
import subprocess

def run_skill(file_path):
    # 1. Formatear el código
    subprocess.run(["python", "tools/formatter.py", f"--file={file_path}"], check=True)
    
    # 2. Linting para asegurar calidad
    subprocess.run(["python", "tools/linter.py", f"--file={file_path}"], check=True)
    
    # 3. Ejecutar pruebas relacionadas
    # (Lógica para encontrar tests relevantes omitida por brevedad)
    subprocess.run(["python", "tools/test_runner.py", "--related-to", file_path], check=True)
    
    # 4. Crear el commit
    # (Lógica para obtener mensaje de commit omitida)
    subprocess.run(["python", "tools/commit.py", "--type=feat", "--message=..."], check=True)

    print("Skill 'validate_and_commit' completado exitosamente.")
```

## 4. Integración en el Flujo IPIVC

Las especificaciones, skills y tools se integran de forma natural en el ciclo de vida de IPIVC.

- **Investiga**: El agente consulta la memoria L1 para encontrar `spec.md` y `skills/` relevantes de tareas pasadas.
- **Planifica**: El agente crea o actualiza el `spec.md` para la tarea actual.
- **Implementa**: El agente genera código que cumple con el `spec.md`.
- **Verifica**: El agente utiliza el `skill_validate_code` (que a su vez usa `tool_linter`, `tool_test_runner`, etc.) para verificar el código contra los criterios de aceptación del `spec.md`.
- **Corrige**: Si la verificación falla, el agente depura y corrige el código, y vuelve a ejecutar el skill de validación hasta que pase.
- **Finalización**: Una vez verificado, el agente utiliza el `skill_commit_and_push` para integrar el cambio en el repositorio.
