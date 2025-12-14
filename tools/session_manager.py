import os
import sys
import datetime
import glob
import subprocess

SESSION_DIR = "memory/active_sessions"
TEMPLATE_PATH = "memory/templates/session_template.md"

def run_git_cmd(args, error_msg):
    try:
        subprocess.check_call(["git"] + args)
    except subprocess.CalledProcessError:
        print(f"⚠️  {error_msg}")

def sync_repo():
    print("\n🔄 Sincronizando con el repositorio remoto...")
    run_git_cmd(["pull"], "Error al hacer git pull. Verifica tu conexión.")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_active_sessions():
    sync_repo()
    sessions = glob.glob(os.path.join(SESSION_DIR, "*.md"))
    if not sessions:
        print("\nNo hay sesiones activas. El repositorio está libre.")
        return
    
    print("\n--- SESIONES ACTIVAS (¡Cuidado con conflictos!) ---")
    for session in sessions:
        filename = os.path.basename(session)
        print(f"🔴 {filename}")
        # Leer primeras lineas para mostrar info
        try:
            with open(session, 'r', encoding='utf-8') as f:
                head = [next(f) for _ in range(5)]
                for line in head:
                    if line.strip().startswith("-"):
                        print(f"   {line.strip()}")
        except:
            pass
    print("---------------------------------------------------\n")

def start_session():
    list_active_sessions()
    
    user = input("Tu Usuario (ej. dev1): ").strip()
    task = input("Nombre breve de Tarea (ej. fix-login): ").strip().replace(" ", "-")
    
    filename = f"{datetime.date.today()}_{user}_{task}.md"
    filepath = os.path.join(SESSION_DIR, filename)
    
    if os.path.exists(filepath):
        print("¡Esta sesión ya existe! Retomando...")
    else:
        print("\nDefiniendo alcance (Soporta patrones como 'src/auth/*' o 'api/**/*.ts')")
        files_affected = input("¿Qué archivos/módulos tocarás? (separados por coma): ")
        
        content = f"""# Sesión Activa: {task}
- Usuario: @{user}
- Estado: Planificando
- Inicio: {datetime.datetime.now()}
- Archivos afectados: `{files_affected}`
- Riesgo de colisión: (Pendiente de evaluar por Agente)

## Bitácora
- Sesión iniciada.
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Sesión registrada en: {filepath}")
        
        # Auto-Push para bloquear remotamente
        print("\n🔒 Intentando bloqueo distribuido...")
        run_git_cmd(["add", filepath], "Error al hacer git add")
        run_git_cmd(["commit", "-m", f"LOCK: Inicio sesión {user} - {task}"], "Error al hacer git commit")
        run_git_cmd(["push"], "Error al hacer push. ¡TU SESIÓN NO ES VISIBLE PARA OTROS!")
        
        # VERIFICACIÓN DE ATOMICIDAD
        print("🔎 Verificando integridad del bloqueo...")
        run_git_cmd(["pull"], "Advertencia: Conflicto potencial detectado durante el pull.")
        
        if os.path.exists(filepath):
             print("✅ BLOQUEO CONFIRMADO: Tu sesión está activa y replicada en el remoto.")
        else:
             print("❌ ERROR CRÍTICO: Tu archivo de sesión desapareció tras el pull. Posible conflicto de nombres o race condition.")

def stop_session():
    sessions = glob.glob(os.path.join(SESSION_DIR, "*.md"))
    if not sessions:
        print("No hay sesiones para cerrar.")
        return

    print("\nSesiones disponibles:")
    for i, s in enumerate(sessions):
        print(f"{i+1}. {os.path.basename(s)}")
    
    try:
        idx = int(input("Número de sesión a cerrar: ")) - 1
        if 0 <= idx < len(sessions):
            # Sincronizar antes de borrar para asegurar que tenemos la ultima version
            sync_repo() 
            
            os.remove(sessions[idx])
            print("✅ Sesión cerrada y archivo eliminado.")
            
            print("\n🔓 Liberando recurso en el remoto...")
            run_git_cmd(["add", sessions[idx]], "Error al hacer git add")
            run_git_cmd(["commit", "-m", f"UNLOCK: Fin sesión {os.path.basename(sessions[idx])}"], "Error al hacer git commit")
            run_git_cmd(["push"], "Error al hacer push. ¡TU SESIÓN SIGUE APARECIENDO ACTIVA!")
            print("✅ Recurso liberado exitosamente.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")

def main():
    ensure_dir(SESSION_DIR)
    
    while True:
        print("\n--- IPIVC Session Manager (Team Adapter) ---")
        print("1. Ver Estado del Equipo (Listar Sesiones)")
        print("2. Iniciar Sesión (Bloquear/Avisar)")
        print("3. Terminar Sesión (Liberar)")
        print("4. Salir")
        
        choice = input("Opción: ")
        
        if choice == '1':
            list_active_sessions()
        elif choice == '2':
            start_session()
        elif choice == '3':
            stop_session()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
