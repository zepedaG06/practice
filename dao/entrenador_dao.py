import pickle
from models.validaciones import validar_nombre

class EntrenadorDAO:
    _archivo = "entrenadores.bin"

    @classmethod
    def registrar(cls):
        """Registra nuevo entrenador"""
        entrenadores = cls._cargar()
        usuario = input("Usuario: ").strip()
        
        while not validar_nombre(usuario) or usuario in entrenadores:
            print("❌ Usuario inválido o ya existe")
            usuario = input("Usuario: ").strip()

        entrenadores[usuario] = input("Contraseña: ").strip()
        cls._guardar(entrenadores)
        print("✅ Entrenador registrado")

    @classmethod
    def iniciar_sesion(cls):
        """Inicia sesión y retorna usuario"""
        entrenadores = cls._cargar()
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()

        if usuario in entrenadores and entrenadores[usuario] == contraseña:
            print(f"✅ Bienvenido, {usuario}!")
            return usuario
        print("❌ Credenciales incorrectas")
        return None

    @classmethod
    def _cargar(cls):
        try:
            with open(cls._archivo, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return {}

    @classmethod
    def _guardar(cls, datos):
        with open(cls._archivo, 'wb') as f:
            pickle.dump(datos, f)