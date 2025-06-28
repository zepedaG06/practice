from dao.entrenador_dao import EntrenadorDAO
from dao.jugador_dao import JugadorDAO
from dao.asistencia_dao import AsistenciaDAO
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    usuario = None
    while True:
        limpiar_pantalla()
        if not usuario:
            print("=== ELITEBASKET ===")
            print("1. Iniciar sesión")
            print("2. Registrar entrenador")
            print("3. Salir")
            opcion = input("Opción: ").strip()

            if opcion == "1":
                usuario = EntrenadorDAO.iniciar_sesion()
            elif opcion == "2":
                EntrenadorDAO.registrar()
            elif opcion == "3":
                print("¡Hasta pronto!")
                break
        else:
            print(f"=== MENÚ ({usuario}) ===")
            print("1. Registrar jugador")
            print("2. Buscar jugador")
            print("3. Modificar jugador")  # Implementar modificar luego
            print("4. Registrar asistencia")
            print("5. Listar jugadores")
            print("6. Eliminar jugador")  # Implementar eliminar luego
            print("7. Cerrar sesión")

            opcion = input("Opción: ").strip()
            if opcion == "1":
                JugadorDAO.registrar(usuario)
            elif opcion == "2":
                criterio = input("Ingrese cédula o nombre completo: ").strip()
                jugador = JugadorDAO.buscar(usuario, criterio)  # Implementar buscar luego
                if jugador:
                    print(jugador)
                else:
                    print("❌ No encontrado")
            elif opcion == "3":
                print("Funcionalidad en construcción")
            elif opcion == "4":
                cedula = input("Cédula del jugador: ").strip()
                AsistenciaDAO.registrar(usuario, cedula)
            elif opcion == "5":
                JugadorDAO.listar(usuario)
            elif opcion == "6":
                print("Funcionalidad en construcción")
            elif opcion == "7":
                usuario = None

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
