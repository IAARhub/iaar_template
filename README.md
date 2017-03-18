# Template site de capacitaciones

Template para crear y actualizar el [sitio de capacitaciones](https://iaarhub.github.io/) de [IAAR](http://iaar.site/).

Creado utilizando el generador de sitios estáticos [Pelican](https://blog.getpelican.com/)

## Instrucciones

Para poder generar el contenido del sitio se necesita tener instalado [Pelican](https://blog.getpelican.com/) y [Python](https://www.python.org/)

1. Clonar este repositorio
2. Crear un documento en [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) en la carpeta `content` 
3. Alternativamente se puede utilizar una notebook de [jupyter](http://jupyter.org/), guardarla en la carpeta `notebooks` y crear el documento [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) relacionado a la notebook en la carpeta `content`. (ver ejemplo ConvTensorFlow.md)
4. Desde la línea de comando, pararse en la carpeta principal `iaar_template` y ejecutar el comando `make publish` para generar los archivos. Se va a generar todo el contenido del sitio estático en la carpeta `output`. 
5. Clonar el repositorio https://github.com/IAARhub/IAARhub.github.io.git 
6. Copiar el contenido de la carpeta `output` reemplanza el contenido del repositorio IAARhub.github.io
7. Pushear los cambios al repositorio IAARhub.github.io
8. Visitar [IAARhub.github.io](https://IAARhub.github.io) para ver los cambios.
