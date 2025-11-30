import json
import os


def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausar():
    input("Presione una tecla para continuar . . .\n")


def cargar_json(nombre_fichero: str) -> dict:
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")
    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")
    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")
    return None


def guardar_json(nombre_fichero: str, datos: dict):
    try:
        with open(nombre_fichero, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")
    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")
    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")


def mostrar_datos(datos: dict):
    if "usuarios" not in datos or not isinstance(datos["usuarios"], list) or len(datos["usuarios"]) == 0:
        print("ERROR El archivo JSON no contiene usuarios!")
        pausar()
        return

    lista_usuarios = datos["usuarios"]

    print("--- Contenido Actual del JSON ---")
    for usuario in lista_usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
    print("--- Fin del Contenido ---\n")

    pausar()


def inicializar_datos():
    # Rutas adaptadas a tu estructura: src/practica_json/
    ruta_origen = "src/practica_json/datos_usuarios_orig.json"
    ruta_destino = "src/practica_json/datos_usuarios.json"

    try:
        with open(ruta_origen, "r", encoding="utf-8") as archivo:
            datos_iniciales = json.load(archivo)
    except FileNotFoundError:
        print(f"ERROR El archivo origen '{ruta_origen}' no existe. No se realizó la copia.")
        return
    except json.JSONDecodeError:
        print(f"ERROR El archivo origen '{ruta_origen}' tiene un formato JSON inválido.")
        return

    with open(ruta_destino, "w", encoding="utf-8") as archivo:
        json.dump(datos_iniciales, archivo, indent=4, ensure_ascii=False)

    print(f"Datos inicializados desde '{ruta_origen}' a '{ruta_destino}'.\n")


def main():
    limpiar_consola()

    inicializar_datos()

    # Fichero JSON de trabajo, también en src/practica_json/
    nombre_fichero = "src/practica_json/datos_usuarios.json"

    datos = cargar_json(nombre_fichero)

    print("DEBUG datos cargados:", datos)

    if datos is None:
        datos = {"usuarios": []}

    mostrar_datos(datos)

    actualizar_usuario(datos, id_usuario=1, nueva_edad=31)
    mostrar_datos(datos)

    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)
    mostrar_datos(datos)

    eliminar_usuario(datos, id_usuario=2)
    mostrar_datos(datos)

    guardar_json(nombre_fichero, datos)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
