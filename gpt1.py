import codecs

# Diccionario de caracteres especiales y sus reemplazos
replacements = {
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
    '\\u00f9': 'ù'
}

def replace_special_characters(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def process_file(input_file_path, output_file_path):
    # Leer el archivo de entrada
    with codecs.open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Decodificar caracteres Unicode
    decoded_content = content.encode().decode('unicode_escape')

    # Reemplazar caracteres especiales
    processed_content = replace_special_characters(decoded_content)

    # Escribir el contenido procesado en el archivo de salida
    with codecs.open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

# Ruta del archivo de entrada y salida
input_file_path = 'd:\ESTHER\material json\compartido.txt'
output_file_path = 'd:\ESTHER\material json\compartido_procesado.txt'

# Procesar el archivo
process_file(input_file_path, output_file_path)

print(f"El documento ha sido procesado y guardado en {output_file_path}")