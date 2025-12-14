import sys

def calculate_risk():
    print("--- Vibecoding IPIVC Risk Calculator ---")
    
    try:
        print("\nEvaluar Impacto (1-5):")
        print("1. Menor (Cambios cosméticos, docs)")
        print("2. Bajo (Bugfix simple, refactor local)")
        print("3. Medio (Nueva feature, cambios en lógica core)")
        print("4. Alto (Cambios en seguridad, DB, pagos)")
        print("5. Crítico (Arquitectura completa, prod outage)")
        impact = int(input("Ingrese impacto (1-5): "))

        print("\n¿Afecta componentes compartidos o bloqueados por otros?")
        print("0. No")
        print("1. Sí (+5 al riesgo)")
        conflict = int(input("Ingrese (0/1): "))
        
        print("\nEvaluar Expertise del Agente (1-5):")
        print("1. Principiante (Modelo base, sin contexto)")
        print("2. Competente (Con contexto básico)")
        print("3. Experto (Contexto completo, herramientas adecuadas)")
        print("4. Especialista (Fine-tuned, validado)")
        print("5. Maestro (Historial perfecto en tarea similar)")
        expertise = int(input("Ingrese expertise (1-5): "))
        
        # Invertir expertise para el cálculo (mayor expertise = menor riesgo)
        # Risk = Impact * (6 - Expertise)
        # Si expertise es 5 (Maestro), multiplicador es 1.
        # Si expertise es 1 (Principiante), multiplicador es 5.
        
        risk_score = impact * (6 - expertise)
        if conflict == 1:
            risk_score += 5
        
        print(f"\nScore de Riesgo: {risk_score}")
        
        if risk_score <= 5:
            level = "BAJO"
            action = "Proceder con revisión estándar."
        elif risk_score <= 10:
            level = "MEDIO"
            action = "Requerido: security.spec.md y revisión humana."
        elif risk_score <= 15:
            level = "ALTO"
            action = "Requerido: security.spec.md, tests exhaustivos y aprobación de senior."
        else:
            level = "CRÍTICO"
            action = "STOP. Requiere planificación detallada y supervisión constante."
            
        print(f"Nivel de Riesgo: {level}")
        print(f"Acción: {action}")
        
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    calculate_risk()
