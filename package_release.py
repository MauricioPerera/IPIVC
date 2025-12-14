import os
import zipfile
import datetime

def zip_project():
    version = "v1.1_HumanCentric"
    zip_filename = f"IPIVC_Team_Edition_{version}.zip"
    
    # Archivos y carpetas a incluir
    include_files = [
        "README.md",
        "AGENTS.md",
        "TEAM_WORKFLOW.md",
        "TESTING_GUIDE.md",
        "IMPROVEMENTS.md",
        "LokiVector_Integration_Plan.md",
        "security.spec.md",
        "install_standard.py"
    ]
    
    include_dirs = [
        "tools",
        "memory",
        "ai_instructions"
    ]
    
    print(f"📦 Empaquetando {zip_filename}...")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Agregar archivos raíz
        for file in include_files:
            if os.path.exists(file):
                print(f"  + {file}")
                zipf.write(file)
            else:
                print(f"  ⚠️ Falta {file}")
        
        # Agregar directorios
        for dir_name in include_dirs:
            if os.path.exists(dir_name):
                print(f"  + {dir_name}/")
                for root, dirs, files in os.walk(dir_name):
                    for file in files:
                        # Ignorar archivos temporales o de sistema
                        if file == "__pycache__" or file.endswith(".pyc") or file.endswith(".DS_Store"):
                            continue
                        
                        file_path = os.path.join(root, file)
                        print(f"    - {file}")
                        zipf.write(file_path)
            else:
                print(f"  ⚠️ Falta directorio {dir_name}")

    print(f"\n✅ Release creado exitosamente: {os.path.abspath(zip_filename)}")
    print("Este archivo está listo para ser distribuido a tu equipo.")

if __name__ == "__main__":
    zip_project()
