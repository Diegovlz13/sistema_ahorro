import random

from pathlib import Path

class SavingsPlan:
    """Genera un plan de ahorro repartiendo una cantidad total en varios días."""

    def __init__(self, days, amount):
        self.days = days      
        self.amount = amount
        self.plan = self.generate_plan()  


    def generate_plan(self):
        """Genera una lista de montos diarios que suman exactamente el total."""
        plan = self._calculate_random_plan()
        return self._fix_rounding_difference(plan)
    
    
    def extract_random_value(self):
        """Extrae un valor aleatorio del plan de ahorro, eliminandolo de la lista."""
        if not self.plan:
            print("Felicitaciones! Has completado tu plan de ahorro.")
            # 🚨 Aqui agregare un función que le indique al usuario la cantidad total ahorrada y un resumen de las cantidades cada día
            # 🚨 No lose, si lo hare solo por numero o tambien con fechas
        else:
            return self.plan.pop(random.randint(0, len(self.plan) - 1))
    
    
    def save_plan(self, filename="plan_values.txt"):
        """Guarda el plan de ahorro en un archivo de texto"""
        path = Path(filename)
        path.write_text('\n'.join(map(str, self.plan)))
         
        
    def _calculate_random_plan(self):
        """Crea una distribución proporcional basada en pesos aleatorios."""
        weights = [random.random() for _ in range(self.days)]
        total_weights = sum(weights)

        return [(w / total_weights) * self.amount for w in weights]


    def _fix_rounding_difference(self, calculated):
        """Corrige el efecto del redondeo para asegurar que el total sea exacto."""
        plan = [int(round(value)) for value in calculated]
        difference = self.amount - sum(plan)

        i = 0
        while difference != 0:
            plan[i] += 1 if difference > 0 else -1
            difference += -1 if difference > 0 else 1
            i = (i + 1) % self.days

        return plan

    
    
        