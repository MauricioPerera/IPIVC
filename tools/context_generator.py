import os
import glob

def get_file_content(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def generate_context():
    output = []
    output.append("# CONTEXTO DE PROYECTO (IPIVC STANDARD)")
    output.append("Generado automáticamente para sincronización de Agentes Heterogéneos.\n")
    
    # 1. Project Truth
    output.append("## 1. Verdad del Proyecto (L1 Memory)")
    output.append(get_file_content("memory/L1_project.md"))
    output.append("\n")
    
    # 2. Active Sessions (Team Awareness)
    output.append("## 2. Estado del Equipo (Active Sessions)")
    sessions = glob.glob("memory/active_sessions/*.md")
    if not sessions:
        output.append("No hay otros agentes trabajando activamente.")
    else:
        for s in sessions:
            output.append(f"--- Sesión: {os.path.basename(s)} ---")
            output.append(get_file_content(s))
            output.append("-------------------------------------\n")
            
    # 3. Security Specs
    output.append("## 3. Reglas de Seguridad")
    output.append(get_file_content("security.spec.md"))
    
    # 4. Agent Instructions (Auto-Append)
    output.append("\n## 4. INSTRUCCIONES PARA EL AGENTE (LEER CON ATENCIÓN)")
    output.append(get_file_content("AGENTS.md"))
    output.append("\n--- ROLES DISPONIBLES (El humano te asignará uno) ---")
    output.append(">>> ARQUITECTO:\n" + get_file_content("ai_instructions/roles/architect_agent.md"))
    output.append(">>> CODER:\n" + get_file_content("ai_instructions/roles/coder_agent.md"))
    output.append(">>> QA:\n" + get_file_content("ai_instructions/roles/qa_agent.md"))
    
    # Write to file
    with open("CURRENT_CONTEXT.prompt.md", "w", encoding='utf-8') as f:
        f.write("\n".join(output))
    
    print("✅ Archivo 'CURRENT_CONTEXT.prompt.md' generado.")
    print("📋 INSTRUCCIÓN: Copia el contenido de este archivo y pégalo en tu chat con la IA (ChatGPT, Claude, etc.) al inicio de la sesión.")

if __name__ == "__main__":
    generate_context()
