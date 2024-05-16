# procesartexto
Proyecto de programas en python para el procesamiento de texto.
A partir de documentos PDF, que son convertidos en documentos TXT por medio de sitios web online.
Luego los documentos se colocan en una carpeta que sera procesada por medio del script. El cual genera un archivo JSON con la información de cada archivo.
Las distintas codificaciones originales de los documentos se mantienen en el documento JSON final. Por lo cual fue necesario un segundo script para codificar correctamente el contenido en UTF-8
Los archivos finales se suben a un sitio de analisis de documentos con IA generativa para poder realizar consultas sobre la información suministrada.
Sitio web para el analisis: www.cohere.com