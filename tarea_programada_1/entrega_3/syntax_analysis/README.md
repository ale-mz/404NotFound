# Analizador sintactico para el archivo *vpn-logs-2020-modified-abb-revMM.txt* realizado en Python
## Librería PLY usada para el analizador léxico
Para trabajar con expresiones regualres (regex), se hizo uso de la libreria [ply](https://pypi.org/project/ply/), una implementación de lex y yacc escrita en Python.
Para poder trabajar con esa herramienta se debe primero de instalarla con el siguiente comando:
```
pip install ply
```
Es importante notar que se debe de tener instalado un interprete de [**Python 3**](https://www.python.org/) y el gestor de paquetes [**pip**](https://pypi.org/project/pip/).

## Librería yacc usada para el analizador sintactico
Para trabajar con el analizador sintactico, se hizo uso de la libreria [yacc](https://silcnitc.github.io/yacc.html), la cual es parte de la libreria [ply](https://pypi.org/project/ply/).

## Cómo ejecutar el analizador sintactico
Para ejecutar el analizador sintactico se debe de ejecutar el siguiente comando:
```
python .\regexProve.py
```
Ya que la salida producida por el programa puede llegar a ser bastante grande, lo que usualemente hacemos es redireccionar la salida estandar hacia a un archivo de texto, lo cual hacemos usando el siguiente commando:
```
python .\regexProve.py >output.txt
```

## Cómo funciona el analizador sintactico
### Expresiones regulares
Para poder resolver el problema planteado, tuvimos que desarrollar un total de 39 expresiones regulares (regex), los cuales esta representados en el codigo en dos partes:
- un identificador de token presente en la lista de tokens, tiene que ser unica para cada regex
- la expresion regular que se va a usar para reconocer el token, tambien se puede referirse como "regla" que debe de complir una hilera para ser reconocida como un token

### Gramatica
Para poder resolver el problema planteado, tuvimos que desarrollar una gramatica compuesta de reglas bien ordenadas y funcionales.
Tras varios intentos de implementación, terminamos usando una gramatica dynamica que para fines de optimización sea suficiente modular para volver a usar mas de una vez una misma regla.
Aunque hemos intentado varias implementaciones, al final no hemos logrado implementar que un mismo analizador funcione para todas las partes del archivo de log, por lo cual hemos tenido que implementar varios analizadores minimalistas para varias partes del archivo de log.

## Creditos
### Codigo escrito por:
- [Madriz Agüero Jorge Alejandro](https://github.com/ale-mz)
- [Padilla Fallas Axel Fabián](https://github.com/FabianPadFal)
- [Carrion Claeys Archibald Emmanuel](https://github.com/archibald-carrion)
### Bibliografía usada
- [Documentación de PLY](https://mv1.mediacionvirtual.ucr.ac.cr/pluginfile.php/2053628/mod_resource/content/1/ply-readthedocs-io-en-latest.pdf)
- [Pagina Github oficial de PLY](https://github.com/dabeaz/ply)
