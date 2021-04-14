import csv
import xml.etree.ElementTree as ET
#Sfrom lxml import etree


def checker(file):
    '''
    obtiene la ruta del archivo para poder usarla para que el XML se cree en la ruta del archivo original.
    '''
    path = file.split("\\")
    endpath = "\\".join(path[:-1]) 
    print (endpath)
    return endpath


def organismos(file, filename):
    '''
    recibe el CSV y el nombre de archivo de salida y crea el XML en la misma carpeta con la estructura de XML de organismos
    '''
    final = checker(file)
    try: 
        with open(file) as f:
            csv_reader = csv.DictReader(f, delimiter=";")
            lines = 0
            filecounter = 1
            #header = next(csv_reader,None)
            #print( header)
            for row in csv_reader:
                '''
                itera fila a fila del csv, cada fila un diccionario(row) con los valores a introducir en los diferentes campos,
                y separa los ficheres si estos tiene n mas de 300 filas
                '''
                if lines == 0:
                    root = ET.Element("organismos")
                    itemadder(row, root)
                    lines +=1
                elif lines/3000 == 0:
                    tree = ET.ElementTree(root)
                    tree.write(endpath+ "\\" + filename + str(filecounter) +".xml",encoding="UTF-8",xml_declaration=True,)
                    filecounter += 1
                    lines = 0
                else:
                    itemadder(row,root)
                    lines +=1
            tree = ET.ElementTree(root)
            tree.write(final+ "\\" + filename + str(filecounter) + ".xml", encoding = "UTF-8", xml_declaration=True,)
    except Exception as e:
        print(e) 

def itemadder(items, root):
    '''
    crea la raiz del XML e introduce los valores que se le pasan en el diccionario
    '''
    organismo = ET.SubElement(root, "organismo")
    roles = False
    persona = False
    for k,v in items.items():
        if v == "":
            #no incluir campo si el valor de la celda esta vacio
            pass
        elif k == "nombre":
            elemento = ET.SubElement(organismo, f"{k}")
            elemento.text = f"{v}"
        elif "rol" in k:
            if roles == False:
                rol = ET.SubElement(organismo, "rol")
                ET.SubElement(rol, f"{k}").text = f"{v}"
                roles =  True
            else:
                ET.SubElement(rol, f"{k}").text = f"{v}"
        elif "persona" in k:
            if persona == False:
                personacontacto = ET.SubElement(organismo,"personaContacto")
                ET.SubElement(personacontacto, f"{personaclean(k)}").text = f"{v}"
                persona = True
            else:
                if "direccion" in k:
                    ET.SubElement(personacontacto,f"{personaclean(k)}").text = f"{v}"
                else:
                    ET.SubElement(personacontacto,f"{personaclean(k)}").text = f"{v}"
        else:
            elemento = ET.SubElement(organismo, f"{k}")
            elemento.text = f"{v}"
    
    



def personaclean(campo):
    '''
    para los campos anidados de persona de contacto, separa el nombre del campo en 2 partes y devuelve la ultima, que es el nombre del campo a añadir al XML
    '''
    campolimpio = campo.split("-")[-1]
    return str(campolimpio)
'''
def validate(xml_path= "C:/Users/bllanos/Desktop/project1/prueba1/a1.xml", xsd_path= "C:/Users/bllanos/Desktop/project1/prueba1/organismos.xsd"):
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)
    print(result)
    return result

    #"C:/Users/bllanos/Desktop/project1/prueba1/organismos.xsd"
    #"C:/Users/bllanos/Desktop/project1/prueba1/a1.xml"'''