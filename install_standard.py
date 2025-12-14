import os
import shutil
import sys

def install_standard():
    print("--- Instalador del Estándar IPIVC ---")
    print("Este script copiará la estructura IPIVC a tu proyecto actual.")
    
    target_dir = input("Ingresa la ruta de tu proyecto (Enter para carpeta actual): ").strip()
    if not target_dir:
        target_dir = os.getcwd()
        
    if not os.path.exists(target_dir):
        print(f"Error: La ruta {target_dir} no existe.")
        return

    print(f"\nInstalando en: {target_dir}...")
    
    # Definir qué copiar
    folders_to_copy = ["tools", "memory", "ai_instructions"]
    files_to_copy = ["TEAM_WORKFLOW.md", "security.spec.md"]
    
    # Copiar carpetas
    for folder in folders_to_copy:
        src = os.path.join(os.getcwd(), folder)
        dst = os.path.join(target_dir, folder)
        if os.path.exists(src):
            try:
                if os.path.exists(dst):
                    print(f"⚠️  La carpeta {folder} ya existe. Saltando...")
                else:
                    shutil.copytree(src, dst)
                    print(f"✅ Carpeta {folder} copiada.")
            except Exception as e:
                print(f"❌ Error copiando {folder}: {e}")
    
    # Copiar archivos
    for file in files_to_copy:
        src = os.path.join(os.getcwd(), file)
        dst = os.path.join(target_dir, file)
        if os.path.exists(src):
            try:
                shutil.copy2(src, dst)
                print(f"✅ Archivo {file} copiado.")
            except Exception as e:
                print(f"❌ Error copiando {file}: {e}")

    print("\n--- Instalación Completa ---")
    print("Pasos siguientes:")
    print("1. Entra a tu proyecto.")
    print("2. Ejecuta 'git add tools memory ai_instructions TEAM_WORKFLOW.md security.spec.md'")
    print("3. Ejecuta 'git commit -m \"Chore: Adopt IPIVC Standard\"'")
    print("4. ¡Tu equipo ya está sincronizado!")

if __name__ == "__main__":
    install_standard()
