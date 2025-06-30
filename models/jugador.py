# models/jugador.py

class Jugador:
    def __init__(self, cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.peso = peso          # en kilogramos, tipo float
        self.altura = altura      # en centímetros, tipo float
        self.antecedentes = antecedentes
        self.posicion = posicion
        self.imc = self.calcular_imc()  # Calcula IMC al crear la instancia

    def calcular_imc(self):
        altura_m = self.altura / 100  # Convertir cm a metros
        if altura_m > 0:
            return self.peso / (altura_m ** 2)
        else:
            return 0.0

    def __str__(self):
        return (f"\n=== DATOS DEL JUGADOR ===\n"
                f"Cédula: {self.cedula}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad} años | Teléfono: {self.telefono}\n"
                f"Peso: {self.peso}kg | Altura: {self.altura}cm\n"
                f"Posición: {self.posicion}\n"
                f"IMC: {self.imc:.2f}\n"
                f"Antecedentes: {self.antecedentes}\n"
                + "=" * 30)





