import os
import json

# Ruta de la carpeta que contiene los archivos TXT
carpeta_txt = 'd:\ESTHER\Material procesado\compartido'

# Lista de codificaciones a probar
codificaciones = ['utf-8', 'ansi', 'latin-1', 'windows-1252', 'iso-8859-1']

# Diccionario de traducción de caracteres especiales
traduccion_secuencias = {
    '\\u00f3': 'ó',
    '\\u00e1': 'á',
    '\\u00e9': 'é',
    '\\u00ed': 'í',
    '\\u00f6': 'ö',
    '\\u00e1': 'á',
    '\\u00e9': 'é',
    '\\u00ed': 'í',
    '\\u00f3': 'ó',
    '\\u00fa': 'ú',
    '\\u00fc': 'ü',
    '\\u00f1': 'ñ',
    '\\u00bf': '¿',
    '\\u00a1': '¡',
    '\\u00ab': '«',
    '\\u00bb': '»',
    '\\u00e1': 'á',
    '\\u00e9': 'é',
    '\\u00ed': 'í',
    '\\u00f3': 'ó',
    '\\u00fa': 'ú',
    '\\u00fc': 'ü',
    '\\u00f1': 'ñ',
    '\\u00aa': 'ª',
    '\\u00ba': 'º',
    '\\u00c0': 'À',
    '\\u00c8': 'È',
    '\\u00cc': 'Ì',
    '\\u00d2': 'Ò',
    '\\u00d9': 'Ù',
    '\\u00e0': 'à',
    '\\u00e8': 'è',
    '\\u00ec': 'ì',
    '\\u00f2': 'ò',
    '\\u00f9': 'ù',
    # Agregar más caracteres especiales según sea necesario
}

# Crear una lista para almacenar los datos JSON finales
datos_json_final = []

# Recorrer todos los archivos TXT en la carpeta
for archivo_txt in os.listdir(carpeta_txt):
    if archivo_txt.endswith('.txt'):
        # Ruta del archivo original
        ruta_original = os.path.join(carpeta_txt, archivo_txt)
        
        # Encontrar la codificación correcta para el archivo
        codificacion_correcta = None
        for codificacion in codificaciones:
            try:
                # Abrir el archivo TXT para leerlo con la codificación actual
                with open(ruta_original, 'r', encoding=codificacion) as archivo:
                    lineas = archivo.readlines()
                
                # Codificar las líneas a UTF-8
                lineas = [linea.encode('utf-8', errors='replace').decode('utf-8') for linea in lineas]
                
                # Comprobar si hay caracteres especiales en las líneas
                for linea in lineas:
                    if '\\' in linea:
                        # Saltar a la siguiente codificación
                        break
                else:
                    # Se encontró una codificación válida
                    codificacion_correcta = codificacion
                    break
            except UnicodeDecodeError:
                print(f"Error al decodificar {archivo_txt} en {codificacion}. Probando la siguiente codificación...")
        
        if codificacion_correcta is None:
            print(f"No se pudo encontrar una codificación válida para {archivo_txt}. Saltando al siguiente archivo.")
            continue
        
        # Crear una lista para almacenar los párrafos combinados
        parrafos_combinados = []
        parrafo_actual = ''
        
        # Recorrer las líneas del archivo
        for linea in lineas:
            # Quitar los saltos de línea y espacios extras
            linea_limpia = linea.strip()
            
            # Eliminar el signo '-' al final de la línea
            if linea_limpia.endswith('-'):
                linea_limpia = linea_limpia[:-1]
            
            # Comprobar si la línea actual termina con un punto
            if linea_limpia.endswith('.'):
                # Combinar el párrafo actual con la línea actual y agregar un espacio
                parrafo_actual += ' ' + linea_limpia
                
                # Agregar el párrafo combinado a la lista de párrafos
                parrafos_combinados.append(parrafo_actual)
                
                # Reiniciar el párrafo actual
                parrafo_actual = ''
            else:
                # Agregar la línea actual al párrafo actual sin saltos de línea
                parrafo_actual += linea_limpia
        
        # Combinar los párrafos en un solo texto
        texto_modificado = '\n\n'.join(parrafos_combinados)
        
        # Obtener el nombre del archivo sin la extensión
        nombre_archivo, extension = os.path.splitext(archivo_txt)
        
        # Agregar los datos al diccionario JSON final
        datos_json_final.append({
            'titulo': nombre_archivo,
            'contenido': texto_modificado
        })

# Escribir los datos combinados en un archivo JSON final
with open('archivo_combinado.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(datos_json_final, archivo_json, indent=2)

# Procesar el archivo JSON final para traducir secuencias de caracteres especiales
with open('archivo_combinado.json', 'r', encoding='utf-8') as archivo_json:
    datos_json = json.load(archivo_json)
    
    for diccionario in datos_json:
        contenido = diccionario['contenido']
        for secuencia_original, secuencia_utf8 in traduccion_secuencias.items():
            # Buscar la secuencia de caracteres en el contenido
            if secuencia_original in contenido:
                # Reemplazar la secuencia de caracteres
                contenido = contenido.replace(secuencia_original, secuencia_utf8)
        diccionario['contenido'] = contenido

# Escribir el archivo JSON final traducido
with open('archivo_combinado_traducido.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=2)

print("Archivos TXT combinados y guardados exitosamente en archivo_combinado.json.")
print("Archivo JSON final traducido y guardado exitosamente en archivo_combinado_traducido.json.")