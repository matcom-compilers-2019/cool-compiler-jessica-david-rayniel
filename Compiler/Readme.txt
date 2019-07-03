=Para correr el compilador de codigo COOL a codigo mips corre en la terminal el main.py.
+ Nuestro codigo solo usa como librerias que se tienen que instalar ply

-En \code\utils\directorio.py estan guardados como dos campos string los 2 path de input y de output, para correrlo primero 
asegurarse de poner bien estos dos campos de path para que funcione, tener en cuenta que se debe usar un raw string en windows
por ejemplo por el tema de los slahs dobles y demas 

- En input tenemos algunos casos de pruebas de codigo cool, y en la carpeta output tenemos el resultante codigo mips de correr
estos casos de prueba en nuestro compilador, tener en cuenta que no todos los casos de pruebas generan codigo mips, algunos
no pasan el chequeo semantico y de tipos, tenemos algunos ejemplos tambien de estos.

-En output tenemos el codigo mips resultante de los casos de prueba, basta correrlos en el spim para comprobarlos.

-En el reporte tenemos el pdf explicando nuestro trabajo.

-En test hay otros casos de pruebas que tenemos

-En code esta nuestro codigo dividido en 3 secciones utils, que son cosas generales que utilizamos, front_end que es toda la 
parte del compilador hasta generacion de codigo cil y en back_end tenemos la generacion de codigo mips.