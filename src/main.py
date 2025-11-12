from interface import show_header
from savings_plan import SavingsPlan


def get_positive_int(prompt: str) -> int:
    """Solicita un entero positivo al usuario y valida la entrada."""
    while True:
        try:
            value_str = input(prompt)
            value_int = int(value_str)
            if value_int > 0:
                return value_int
            else:
                print("El número debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def get_positive_float(prompt: str) -> float:
    """Solicita un float positivo al usuario y valida la entrada."""
    while True:
        try:
            value_str = input(prompt)
            value_float = float(value_str)
            if value_float > 0.0:
                return value_float
            else:
                print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número (ej: 150.75).")


def main():
    """Función principal que ejecuta el programa de plan de ahorro."""
    show_header()
    
    days = get_positive_int("Ingrese el número de días para el plan de ahorro: ")
    amount = get_positive_float("Ingrese la cantidad total a ahorrar (ej: 1000.50): ")
    
    plan = SavingsPlan(days, amount)
    
    plan.save_plan()
    print(f"Plan de ahorro generado y guardado en '{plan.plan_file.name}'.")
    print(f"Total ahorrado hasta ahora: {plan.get_total_saved():.2f}")
    
    while True:
        # Verificamos si quedan montos en el plan antes de preguntar
        if not plan.plan:
            print("¡Felicidades! Ha extraído todas las cantidades del plan.")
            break
            
        action = input("\n¿Desea extraer una cantidad aleatoria del plan? (s/n): ").strip().lower()
        
        if action == 's':
            # 1. Extraemos la cantidad UNA SOLA VEZ
            extracted_amount = plan.extract_random_amount()
            
            if extracted_amount is not None:
                print(f"Cantidad extraída: {extracted_amount:.2f}")
                
                # 2. Guardamos la cantidad que acabamos de extraer
                plan.save_extracted_amount(extracted_amount)
                
                print(f"Total ahorrado hasta ahora: {plan.get_total_saved():.2f}")
                print(f"Quedan {len(plan.plan)} cantidades por extraer.")
            else:
                # Este 'else' ahora es redundante gracias a la verificación de arriba,
                # pero lo mantenemos como doble seguridad.
                print("No quedan cantidades por extraer.")
                break
        
        elif action == 'n':
            print("Saliendo del programa. ¡Sigue ahorrando!")
            break
        
        else:
            print("Entrada no válida. Por favor, ingrese 's' o 'n'.")

if __name__ == '__main__':
    main()