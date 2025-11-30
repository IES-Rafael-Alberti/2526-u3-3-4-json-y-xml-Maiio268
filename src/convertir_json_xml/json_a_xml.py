import json
# Libreria para parsear y unparsear
import xmltodict


# Inicializamos las rutas del original y del transformado
ruta_json = 'src/convertir_json_xml/original.json'
ruta_xml = 'src/convertir_json_xml/transformacion.xml'
  
# Leemos el JSON y lo asignamos a un diccionario de Python
with open(ruta_json, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# xmltodict.unparse convierte diccionario de Python a XML
'''
Como un archivo xml solo puede tener 1 elemento raiz, metemos todo el contenido del archivo en una etiqueta llamada 'raiz' para q no den errores,
de lo contrario se generan mas elementos y da error de multiples elementos raiz.
'''
xml_texto = xmltodict.unparse({'raiz': datos}, pretty=True)

# Guardamos el XML en el archivo json transformacion
with open(ruta_xml, 'w', encoding='utf-8') as archivo:
    archivo.write(xml_texto)

print('Archivo xml transformado')
