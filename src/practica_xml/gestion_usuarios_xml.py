import os
import xml.etree.ElementTree as ET

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausar():
    input('Presione una tecla para continuar . . .\n')

def cargar_xml(nombre_fichero: str):
    try:
        tree = ET.parse(nombre_fichero)
        return tree
    except FileNotFoundError:
        print(f'*ERROR* El archivo {nombre_fichero} no existe.')
    except ET.ParseError:
        print('*ERROR* El archivo XML tiene un formato incorrecto.')
    except Exception as e:
        print(f'*ERROR* Problemas al cargar el XML: {e}')
    return None


def guardar_xml(tree: ET.ElementTree, nombre_fichero: str):
    try:
        tree.write(nombre_fichero, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f'*ERROR* Problemas al guardar el XML: {e}')


def actualizar_usuario(root: ET.Element, id_usuario: int, nueva_edad: int):
    for usuario in root.findall('usuario'):
        id_texto = usuario.find('id').text
        if int(id_texto) == id_usuario:
            usuario.find('edad').text = str(nueva_edad)
            print(f'Usuario con ID {id_usuario} actualizado.')
            return
    print(f'Usuario con ID {id_usuario} no encontrado.')


def insertar_usuario(root: ET.Element, id_usuario: int, nombre: str, edad: int):
    nuevo = ET.SubElement(root, 'usuario')

    id_el = ET.SubElement(nuevo, 'id')
    id_el.text = str(id_usuario)

    nombre_el = ET.SubElement(nuevo, 'nombre')
    nombre_el.text = nombre

    edad_el = ET.SubElement(nuevo, 'edad')
    edad_el.text = str(edad)

    print(f'Usuario {nombre} añadido con éxito.')


def eliminar_usuario(root: ET.Element, id_usuario: int):
    for usuario in root.findall('usuario'):
        id_texto = usuario.find('id').text
        if int(id_texto) == id_usuario:
            root.remove(usuario)
            print(f'Usuario con ID {id_usuario} eliminado.')
            return
    print(f'Usuario con ID {id_usuario} no encontrado.')


def mostrar_datos(root: ET.Element):
    usuarios = root.findall('usuario')

    if not usuarios:
        print('ERROR No hay usuarios en el archivo XML.')
        pausar()
        return

    print('--- Contenido Actual del XML ---')
    for usuario in usuarios:
        id_texto = usuario.find('id').text
        nombre = usuario.find('nombre').text
        edad = usuario.find('edad').text
        print(f'ID: {id_texto}, Nombre: {nombre}, Edad: {edad}')
    print('--- Fin del Contenido ---\n')

    pausar()


def inicializar_datos():
    ruta_origen = 'src/practica_xml/datos_usuarios_orig.xml'
    ruta_destino = 'src/practica_xml/datos_usuarios.xml'

    try:
        tree_origen = ET.parse(ruta_origen)
    except FileNotFoundError:
        print(f"ERROR El archivo origen '{ruta_origen}' no existe. No se realizó la copia.")
        return
    except ET.ParseError:
        print(f"ERROR El archivo origen '{ruta_origen}' tiene un formato XML inválido.")
        return

    root_origen = tree_origen.getroot()
    root_copia = ET.fromstring(ET.tostring(root_origen, encoding='utf-8'))
    tree_destino = ET.ElementTree(root_copia)
    tree_destino.write(ruta_destino, encoding='utf-8', xml_declaration=True)

    print(f"Datos inicializados desde '{ruta_origen}' a '{ruta_destino}'.\n")


def crear_arbol(nombre_raiz: str) -> ET.ElementTree:
    raiz = ET.Element(nombre_raiz)
    tree = ET.ElementTree(raiz)
    return tree


def main():
    limpiar_consola()

    inicializar_datos()

    ruta_xml = 'src/practica_xml/datos_usuarios.xml'

    tree = cargar_xml(ruta_xml)

    if tree is None:
        tree = crear_arbol('usuarios')

    root = tree.getroot()

    mostrar_datos(root)

    actualizar_usuario(root, id_usuario=1, nueva_edad=31)
    mostrar_datos(root)

    insertar_usuario(root, id_usuario=3, nombre='Pedro', edad=40)
    mostrar_datos(root)

    eliminar_usuario(root, id_usuario=2)
    mostrar_datos(root)

    guardar_xml(tree, ruta_xml)

    print('Operaciones completadas. Archivo actualizado.\n')

if __name__ == '__main__':
    main()