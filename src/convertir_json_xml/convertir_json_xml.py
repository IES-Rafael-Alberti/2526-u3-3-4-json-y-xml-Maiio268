'''
Convertir el archivo json a xml y viceversa
'''

import json
import xml.etree.ElementTree as xml

# Lee el archivo json y lo convierte en el diccionario 'datos'
with open("src/convertir_json_xml/datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

def dict_a_xml(tag_raiz, d):
    raiz = xml.Element(tag_raiz)
    for clave, valor in d.items():
        hijo = xml.SubElement(raiz, clave)
        hijo.text = str(valor)
    return raiz

# 3. Convertir y guardar como XML
raiz_xml = dict_a_xml("root", datos)
arbol = xml.ElementTree(raiz_xml)
arbol.write("datos.xml", encoding="utf-8", xml_declaration=True)

print("¡Convertido! datos.json → datos.xml")

