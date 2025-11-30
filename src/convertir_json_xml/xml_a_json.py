import json
# Libreria para parsear y unparsear
import xmltodict 

# Inicializamos las rutas del original y del transformado
ruta_xml = 'src/convertir_json_xml/original.xml'
ruta_json = 'src/convertir_json_xml/transformacion.json'

# Leemos el xml
with open(ruta_xml, 'r') as archivo:
    xml_texto = archivo.read()

# xmltodict.parse convierte XML a diccionario de Python
datos_dict = xmltodict.parse(xml_texto) 

# Guardamos el json en el archivo XML transformacion
with open(ruta_json, 'w') as archivo:
    json.dump(datos_dict, archivo, ensure_ascii=False, indent=4)

print('Archivo json transformado')