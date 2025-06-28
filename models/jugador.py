class Jugador:
    def __init__(self, cedula: str, nombre: str, apellido: str, edad: int,
                 telefono: str, peso: float, altura: float, antecedentes: str):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.peso = peso
        self.altura = altura
        self.antecedentes = antecedentes
        self.asistencias = 0
        self._calcular_imc()

    def _calcular_imc(self):
        """Calcula el IMC automáticamente"""
        altura_metros = self.altura / 100
        self.imc = round(self.peso / (altura_metros ** 2), 2)

    def __str__(self):
        return (f"\n=== DATOS DEL JUGADOR ===\n"
                f"Cédula: {self.cedula}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad} años | Teléfono: {self.telefono}\n"
                f"Peso: {self.peso}kg | Altura: {self.altura}cm\n"
                f"IMC: {self.imc} | Asistencias: {self.asistencias}\n"
                f"Antecedentes: {self.antecedentes}\n"
                "=" * 30)