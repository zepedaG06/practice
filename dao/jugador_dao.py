import pickle
from models.jugador import Jugador
from models.validaciones import *

class JugadorDAO:
    _archivo = "jugadores.bin"

    @classmethod
    def _cargar(cls):
        """Carga todos los jugadores desde el archivo binario"""
        try:
            with open(cls._archivo, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return {}

    @classmethod
    def _guardar(cls, datos):
        """Guarda los datos en el archivo binario"""
        with open(cls._archivo, 'wb') as f:
            pickle.dump(datos, f)

    @classmethod
    def registrar(cls, entrenador: str):
        """Registra un nuevo jugador con validaciones estrictas"""
        jugadores = cls._cargar()
        
        if entrenador not in jugadores:
            jugadores[entrenador] = {}

        # Función para validar inputs con reintento
        def _validar_input(mensaje, funcion_validacion, tipo_conversion=str, error_msg="Dato inválido"):
            while True:
                valor = input(mensaje).strip()
                if valor and funcion_validacion(valor):
                    try:
                        return tipo_conversion(valor)
                    except ValueError:
                        print(f"❌ {error_msg}")
                else:
                    print(f"❌ {error_msg}")

        # Validación de cédula (única)
        cedula = _validar_input(
            "Cédula (001-XXXXXX-XXXXX): ",
            validar_cedula,
            error_msg="Formato: 001-1234567-A"
        )
        while cedula in jugadores[entrenador]:
            print("❌ Esta cédula ya está registrada")
            cedula = _validar_input("Cédula: ", validar_cedula)

        # Validación de campos
        nombre = _validar_input(
            "Nombre: ",
            validar_nombre,
            error_msg="Solo letras y espacios (2-50 caracteres)"
        )

        apellido = _validar_input(
            "Apellido: ",
            validar_nombre,
            error_msg="Solo letras y espacios (2-50 caracteres)"
        )

        edad = _validar_input(
            "Edad (15-50 años): ",
            validar_edad,
            tipo_conversion=int,
            error_msg="Debe ser número entre 15 y 50"
        )

        telefono = _validar_input(
            "Teléfono (8 dígitos): ",
            validar_telefono,
            error_msg="8 dígitos numéricos"
        )

        peso = _validar_input(
            "Peso (30-200 kg): ",
            validar_peso,
            tipo_conversion=float,
            error_msg="Número entre 30 y 200"
        )

        altura = _validar_input(
            "Altura (100-250 cm): ",
            validar_altura,
            tipo_conversion=float,
            error_msg="Número entre 100 y 250"
        )

        antecedentes = input("Antecedentes médicos: ").strip()

        # Guardar jugador
        jugadores[entrenador][cedula] = Jugador(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            telefono=telefono,
            peso=peso,
            altura=altura,
            antecedentes=antecedentes
        )
        cls._guardar(jugadores)
        print("\n✅ Jugador registrado exitosamente!")

    @classmethod
    def buscar(cls, entrenador: str, cedula: str) -> Jugador:
        """Busca un jugador por cédula"""
        jugadores = cls._cargar()
        return jugadores.get(entrenador, {}).get(cedula)

    @classmethod
    def listar(cls, entrenador: str):
        """Lista todos los jugadores de un entrenador"""
        jugadores = cls._cargar().get(entrenador, {})
        
        if not jugadores:
            print("\n❌ No hay jugadores registrados")
            return

        print(f"\n=== JUGADORES DE {entrenador.upper()} ===")
        for jugador in jugadores.values():
            print(jugador)
            print("─" * 40)

    @classmethod
    def modificar(cls, entrenador: str):
        """Modifica TODOS los campos del jugador con validaciones"""
        jugadores = cls._cargar()
        
        if entrenador not in jugadores or not jugadores[entrenador]:
            print("\n❌ No hay jugadores registrados")
            return

        # Mostrar jugadores disponibles
        print("\n=== JUGADORES REGISTRADOS ===")
        for cedula in jugadores[entrenador]:
            print(f"- {cedula}")

        # Seleccionar jugador
        cedula = input("\nIngrese cédula del jugador: ").strip()
        if cedula not in jugadores[entrenador]:
            print("\n❌ Jugador no encontrado")
            return

        jugador = jugadores[entrenador][cedula]
        print("\nDATOS ACTUALES:")
        print(jugador)

        # Función para validar inputs editados
        def _input_validado(mensaje, valor_actual, funcion_validacion, tipo_conversion=str):
            while True:
                nuevo_valor = input(f"{mensaje} ({valor_actual}): ").strip()
                if not nuevo_valor:  # Mantener valor actual si está vacío
                    return valor_actual
                if funcion_validacion(nuevo_valor):
                    try:
                        return tipo_conversion(nuevo_valor)
                    except ValueError:
                        print("❌ Formato incorrecto")
                else:
                    print("❌ Valor inválido")

        print("\nEDITAR (dejar vacío para mantener el valor actual):")
        jugador.nombre = _input_validado("Nombre", jugador.nombre, validar_nombre)
        jugador.apellido = _input_validado("Apellido", jugador.apellido, validar_nombre)
        jugador.edad = _input_validado("Edad", jugador.edad, validar_edad, int)
        jugador.telefono = _input_validado("Teléfono", jugador.telefono, validar_telefono)
        
        # Peso y altura (recalculan IMC)
        nuevo_peso = _input_validado("Peso (kg)", jugador.peso, validar_peso, float)
        nueva_altura = _input_validado("Altura (cm)", jugador.altura, validar_altura, float)
        
        if nuevo_peso != jugador.peso or nueva_altura != jugador.altura:
            jugador.peso = nuevo_peso
            jugador.altura = nueva_altura
            jugador._calcular_imc()
            print("¡IMC actualizado!")

        jugador.antecedentes = input(f"Antecedentes ({jugador.antecedentes}): ").strip() or jugador.antecedentes

        cls._guardar(jugadores)
        print("\n✅ Todos los cambios fueron guardados!")

    @classmethod
    def eliminar(cls, entrenador: str):
        """Elimina un jugador del sistema"""
        jugadores = cls._cargar()
        
        if entrenador not in jugadores or not jugadores[entrenador]:
            print("\n❌ No hay jugadores registrados")
            return

        cedula = input("Ingrese cédula del jugador: ").strip()
        if cedula not in jugadores[entrenador]:
            print("\n❌ Jugador no encontrado")
            return

        confirmacion = input(f"¿Eliminar a {jugadores[entrenador][cedula].nombre}? (s/n): ").lower()
        if confirmacion == 's':
            del jugadores[entrenador][cedula]
            cls._guardar(jugadores)
            print("\n✅ Jugador eliminado!")
            





