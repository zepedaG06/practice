import pickle
from models.jugador import Jugador

class JugadorDAO:
    _archivo = "jugadores.bin"

    @classmethod
    def _cargar(cls):
        try:
            with open(cls._archivo, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return {}

    @classmethod
    def _guardar(cls, datos):
        with open(cls._archivo, "wb") as f:
            pickle.dump(datos, f)

    @classmethod
    def registrar(cls, entrenador: str):
        jugadores = cls._cargar()
        if entrenador not in jugadores:
            jugadores[entrenador] = {}

        cedula = input("Cédula: ").strip()
        if cedula in jugadores[entrenador]:
            print("❌ Cédula ya registrada")
            return

        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: ").strip())
        telefono = input("Teléfono: ").strip()
        peso = float(input("Peso: ").strip())
        altura = float(input("Altura: ").strip())
        antecedentes = input("Antecedentes médicos: ").strip()
        posicion = input("Posición: ").strip()

        jugador = Jugador(cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion)
        jugadores[entrenador][cedula] = jugador
        cls._guardar(jugadores)
        print("✅ Jugador registrado")

    @classmethod
    def buscar(cls, entrenador: str, criterio: str):
        jugadores = cls._cargar().get(entrenador, {})
        criterio = criterio.lower()
        # Buscar por cédula exacta
        if criterio in jugadores:
            return jugadores[criterio]
        # Buscar por nombre completo (nombre + apellido)
        for jugador in jugadores.values():
            nombre_completo = f"{jugador.nombre} {jugador.apellido}".lower()
            if nombre_completo == criterio:
                return jugador
        return None

    @classmethod
    def listar(cls, entrenador: str):
        jugadores = cls._cargar().get(entrenador, {})
        if not jugadores:
            print("❌ No hay jugadores registrados")
            return

        # Cargar asistencias
        try:
            with open("asistencias.bin", "rb") as f:
                asistencias = pickle.load(f)
        except (FileNotFoundError, EOFError):
            asistencias = {}

        print(f"\n=== JUGADORES DE {entrenador.upper()} ===")
        for cedula, jugador in jugadores.items():
            key = f"{entrenador}_{cedula}"
            if key in asistencias:
                jugador.asistencias = len(asistencias[key])
            else:
                jugador.asistencias = 0
            print(jugador)
            print("-" * 40)











