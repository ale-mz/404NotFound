# Analizador léxico en Python
## Librería PLY usada para el analizador léxico
Para trabajar con expresiones regualres (regex), se hizo uso de la libreria [ply](https://pypi.org/project/ply/), una implementación de lex y yacc escrita en Python.
Para poder trabajar con esa herramienta se debe primero de instalarla con el siguiente comando:
```
pip install ply
```
Es importante notar que se debe de tener instalado un interprete de [**Python 3**](https://www.python.org/) y el gestor de paquetes [**pip**](https://pypi.org/project/pip/).

## Cómo ejecutar el analizador léxico
Para ejecutar el analizador léxico se debe de ejecutar el siguiente comando:
```
python .\regexProve.py
```
Ya que la salida producida por el programa puede llegar a ser bastante grande, lo que usualemente hacemos es redireccionar la salida estandar hacia a un archivo de texto, lo cual hacemos usando el siguiente commando:
```
python .\regexProve.py >output.txt
```

## Cómo funciona el analizador léxico
### Expresiones regulares
Para poder resolver el problema planteado, tuvimos que desarrollar un total de 39 expresiones regulares (regex), los cuales esta representados en el codigo en dos partes:
- un identificador de token presente en la lista de tokens, tiene que ser unica para cada regex
- la expresion regular que se va a usar para reconocer el token, tambien se puede referirse como "regla" que debe de complir una hilera para ser reconocida como un token

### Modus operandi
Para desarrollar nuestro proyecto, tuvimos que pasar por varios pasos de desarrollo, los cuales se pueden resumir en los siguientes:
1. Definir los tokens que se necesitaran en el analizador léxico
2. Definir las reglas (expresiones regulares) que se se usan para reconocer los tokens
3. Implementar los identificadores de tokens y las reglas en el analizador léxico en nuestro script de Python
4. Probar el analizador léxico con nuestro archivo de trabajo *vpn-logs-2020-modified-abb-revMM.txt*, y arreglar los varios conflictos que se presentaron entre las reglas y los tokens, por lo cual tenemos que volver a la etapa de desarrollo 2 y 3 hasta que nuestro analizador léxico funcionara correctamente

## Creditos
### Codigo escrito por:
- [Madriz Agüero Jorge Alejandro](https://github.com/ale-mz)
- [Padilla Fallas Axel Fabián](https://github.com/FabianPadFal)
- [Carrion Claeys Archibald Emmanuel](https://github.com/archibald-carrion)
### Bibliografía usada
- [Documentación de PLY](https://mv1.mediacionvirtual.ucr.ac.cr/pluginfile.php/2053628/mod_resource/content/1/ply-readthedocs-io-en-latest.pdf)
- [Pagina Github oficial de PLY](https://github.com/dabeaz/ply)

