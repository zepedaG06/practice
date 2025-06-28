import pickle
from datetime import datetime
from dao.jugador_dao import JugadorDAO

class AsistenciaDAO:
    _archivo = "asistencias.bin"

    @classmethod
    def registrar(cls, entrenador: str, cedula: str):
        """Registra asistencia y actualiza contador"""
        asistencias = cls._cargar()
        key = f"{entrenador}_{cedula}"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        if key in asistencias:
            asistencias[key].append(fecha)
        else:
            asistencias[key] = [fecha]

        # Actualizar contador en Jugador
        jugadores = JugadorDAO._cargar()
        if entrenador in jugadores and cedula in jugadores[entrenador]:
            jugadores[entrenador][cedula].asistencias = len(asistencias[key])
            JugadorDAO._guardar(jugadores)

        cls._guardar(asistencias)
        print(f"✅ Asistencia registrada (Total: {len(asistencias[key])})")

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



