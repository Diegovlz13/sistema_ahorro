import random
from pathlib import Path

class SavingsPlan:
    """
    Genera un plan de ahorro repartiendo una cantidad total (ENTERA)
    en un número de días, y gestiona la extracción de montos.
    
    Esta versión genera montos ENTEROS y VARIADOS.
    """
    
    PLAN_FILE = "plan_amounts.txt"
    EXTRACTED_FILE = "extracted_amounts.txt"

    def __init__(self, days: int, amount: int):
        self.days = days      
        self.amount = amount # Ahora es un entero
        
        self.plan_file = Path(self.PLAN_FILE)
        self.extracted_file = Path(self.EXTRACTED_FILE)
        
        self.extracted_amounts = self.read_extracted_amounts()
        self.plan = self.load_or_generate_plan()

    def load_or_generate_plan(self):
        """
        Carga el plan desde el archivo si existe, sino, genera uno nuevo.
        Intenta leer enteros del archivo.
        """
        if self.plan_file.exists():
            try:
                content = self.plan_file.read_text().strip()
                if content:
                    float_list = list(map(float, content.splitlines()))
                    return list(map(int, map(round, float_list)))
            except Exception as e:
                print(f"Error leyendo plan existente, se generará uno nuevo: {e}")
        
        return self.generate_plan()

    def generate_plan(self) -> list[int]:
        """
        Genera una lista de montos ENTEROS y VARIADOS que suman
        exactamente el total.
        """
        
        # 1. Crea pesos aleatorios (esto crea la variedad)
        # Usamos random.random() que da valores de 0.0 a 1.0
        weights = [random.random() for _ in range(self.days)]
        total_weights = sum(weights)
        
        # 2. Calcula el plan ideal (en float) basado en los pesos
        calculated_plan = [(w / total_weights) * self.amount for w in weights]
        
        # 3. Redondea el plan a los enteros más cercanos
        plan = [int(round(value)) for value in calculated_plan]
        
        # 4. Corrige la diferencia de redondeo
        current_sum = sum(plan)
        difference = self.amount - current_sum
        
        # Prepara una lista de índices para barajar
        # Esto asegura que la diferencia se aplica a días aleatorios
        indices = list(range(self.days))
        random.shuffle(indices)
        
        i = 0
        while difference != 0:
            # Obtiene un índice aleatorio de la lista barajada
            idx_to_change = indices[i % self.days] 
            
            # Añade o resta 1
            plan[idx_to_change] += 1 if difference > 0 else -1
            difference += -1 if difference > 0 else 1
            i += 1

        # Barajamos el plan final por si acaso
        random.shuffle(plan)
        return plan
    
    
    def extract_random_amount(self):
        """Extrae una cantidad aleatoria (entera) del plan."""
        if self.plan:
            extracted = self.plan.pop(random.randint(0, len(self.plan) - 1))
            self.save_plan() 
            return extracted
        else:
            return None       
        
    
    def read_extracted_amounts(self) -> list[int]:
        """Lee las cantidades extraídas (enteras) desde un archivo."""
        if not self.extracted_file.exists():
            return []
        
        try:
            content = self.extracted_file.read_text().strip()
            if content:
                float_list = list(map(float, content.splitlines()))
                return list(map(int, map(round, float_list)))
            else:
                return []
        except Exception as e:
            print(f"Error al leer {self.EXTRACTED_FILE}: {e}")
            return []
    
    
    def save_extracted_amount(self, amount_to_save: int):
        """Guarda la cantidad entera extraída en el archivo."""
        if amount_to_save is None:
            return

        self.extracted_amounts.append(amount_to_save)
    
        try:
            content = '\n'.join(map(str, self.extracted_amounts))
            self.extracted_file.write_text(content)
        except Exception as e:
            print(f"Error al guardar en {self.EXTRACTED_FILE}: {e}")
        
    
    def save_plan(self):
        """Guarda el plan de ahorro actual (entero) en un archivo."""
        try:
            content = '\n'.join(map(str, self.plan))
            self.plan_file.write_text(content)
        except Exception as e:
            print(f"Error al guardar en {self.PLAN_FILE}: {e}")
              
         
    def get_total_saved(self) -> int:
        """Calcula el total ahorrado (entero)."""
        return sum(self.extracted_amounts)