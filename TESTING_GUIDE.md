# Guía de Pruebas: Simulación de Equipo IPIVC

Esta guía explica cómo probar que el sistema de coordinación realmente funciona, simulando múltiples usuarios en tu propia máquina.

## Escenario de Prueba: "El Conflicto del Login"
Vamos a simular que el Usuario A (`@Alice`) está arreglando el login, y tú (Usuario B) intentas trabajar en lo mismo.

### Paso 1: Simular al Usuario A (Bloqueo)
Abre una terminal y ejecuta el siguiente comando para crear manualmente una sesión activa (como si Alice hubiera hecho push desde su casa):

```bash
# En Windows (Powershell)
echo "# Sesión Activa: Fix Login`n- Usuario: @Alice`n- Archivos afectados: src/auth/login.ts" > memory/active_sessions/2024-01-01_Alice_Login.md

# En Mac/Linux
echo -e "# Sesión Activa: Fix Login\n- Usuario: @Alice\n- Archivos afectados: src/auth/login.ts" > memory/active_sessions/2024-01-01_Alice_Login.md
```

### Paso 2: Tu Turno (Generación de Contexto)
Ahora, tú eres el Usuario B. Quieres empezar a trabajar.
Ejecuta el generador de contexto:

```bash
python tools/context_generator.py
```

### Paso 3: Verificar la Protección
Abre el archivo generado `CURRENT_CONTEXT.prompt.md`.
Verás algo como esto en la sección "Estado del Equipo":

```markdown
## 2. Estado del Equipo (Active Sessions)
--- Sesión: 2024-01-01_Alice_Login.md ---
# Sesión Activa: Fix Login
- Usuario: @Alice
- Archivos afectados: src/auth/login.ts
```

Y al final, verás las instrucciones de `AGENTS.md` diciéndole a tu IA:
> "CHECK LOCKS: If files_affected includes your target, STOP."

### Paso 4: Prueba con tu IA
Copia el contenido de `CURRENT_CONTEXT.prompt.md` y pégalo en ChatGPT/Trae.
Dile: *"Quiero refactorizar src/auth/login.ts"*.

**Resultado Esperado**: La IA debería decirte: *"No puedo hacerlo ahora, @Alice tiene bloqueado ese archivo. Por favor coordina con ella."*

### Paso 5: Limpieza
Borra el archivo de sesión simulada para liberar el bloqueo:
```bash
rm memory/active_sessions/2024-01-01_Alice_Login.md
```
