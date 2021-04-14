import dicttoxml
import csv

def personaclean(campo):
    '''
    para los campos anidados de persona de contacto, separa el nombre del campo en 2 partes y devuelve la ultima, que es el nombre del campo a añadir al XML
    '''
    campolimpio = campo.split("-")[-1]
    return str(campolimpio)

structure = {
    "NIF":"B06463749",
    "nombre":[],
    "aplicacion":[],
    "naturaleza":[],
    "subnaturaleza":[],
    "clasificacion":[],
    "personaContacto":{
        "nombre":[],
        "direccion":[],
        "codPostal":[],
        "pais":[],
        "provincia":[],
        "NUT":[],
        "municipio":[],
        "correo":[],
        "telefono1":[],
    },
    "roles":{
        "rol_beneficiario":[],
        "rol_organismo_intermedio":[],
        "rol_organismo_senda_financiera":[],
        "rol_organismo_entrega_DECA":[],
        "rol_organismo_concede_ayudas":[],
        "rol_organismo_interviniente_convenio":[],
        "rol_organismo_aprueba_seleccion_operaciones":[],
        "rol_organismo_conserva_documentacion":[],
        "rol_destinatario":[],
        "rol_organismo_certifica":[],
        "rol_destinatario_final":[],
        "rol_organismo_desarrolla_verificaciones_reembolso":[],
        "rol_organismo_desarrolla_verificaciones_terreno":[],
        "rol_organismo_firma_verificaciones":[],
        "rol_organismo_auditoria":[],
        "rol_organismo_controlado":[],
        "rol_adjudicador":[],
        "rol_adjudicatario":[],
        "rol_organismo_proyecto_cooperacion":[],
        "rol_organismo_gestor_DUSI":[],
        "rol_entidad_beneficiaria_DUSI":[],
        "rol_supervisor_operaciones_DUSI":[],
        "rol_organismo_responsable_ITI":[],
        "rol_autoridad_gestion":[],
        "rol_autoridad_certificacion":[],
        "rol_autoridad_auditoria":[],
    },

}

xml = dicttoxml.dicttoxml(structure)
print(xml)
file = "C:/Users/bllanos/Desktop/project1/prueba1/organismos-prueba.csv"
with open(file) as f:
    csv_reader = csv.DictReader(f, delimiter=";")
    lines = 0
    filecounter = 1
    organismos
    for row in csv_reader:
        '''
        itera fila a fila del csv, cada fila un diccionario(row) con los valores a introducir en los diferentes campos,
        y separa los ficheres si estos tiene n mas de 300 filas
        '''
        organismo={}
        for k,v in row.items():





