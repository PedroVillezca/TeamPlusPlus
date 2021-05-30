# Manual de Usuario - TeamPlusPlus

TeamPlusPlus es un lenguaje de programación imperativo procedural con componentes básicos para orientación a objetos.

## Gramática
Para compilar la gramática de este lenguaje, se necesita utilizar [ANTLR](https://www.antlr.org/). El lenguaje de implementación es Python 3.

El comando para realizar la compilación es:

```
antlr4 -Dlanguage=Python3 TeamPlusPlus.g4
```

## Compilación
El comando para compilar y correr un archivo es:
```
python TeamPlusPlus.py <archivo>.tpp
```

El lenguaje incluye múltiples flags, utilizadas principalmente para debugging:
- **-d** imprime todo el Directorio General y la Lista de Cuádruplos
- **-c** imprime solamente la Lista de Cuádruplos
- **-f** imprime solamente el Directorio General
- **-o** imprime la Pila de Operadores
- **-v** imprime la Pila de Operandos

Al correr un archivo, se pueden incluir una o varias de estas flags.

## Componentes del lenguaje

### Principales secciones de un programa
- Estatuto program
- Declaración de clases
- Declaración de variables
- Declaración de funciones o métodos
- Main
- Comentarios

#### Estatuto program
Para marcar el principio del archivo, en el encabezado de todo programa se debe incluir un estatuto como el siguiente:

Ejemplo:
```
program archivo;
```
#### Declaración de clases

TeamPlusPlus soporta la definición de clases por parte del usuario. Cada clase que se define puede contener sus propios atributos y métodos, 
los cuales siguen las reglas de declaración de variables globales y funciones respectivamente.

Cada atributo y método debe definir su nivel de accesibilidad, ya sea público o privado.

Ejemplo:
```
class Person {
    attributes
        private int age;

    methods
        public func int getAge() {
            return(age);
        }

        public func void setAge(int a) {
            age = a;
        }
};      

class Student inherits Person {
    attributes
        private float grade;
    methods
        public func void setGrade(float g) {
            grade = g;
        }

        public func float getGrade(){
            return(grade);
        }
};
```
#### Declaración de variables
Las declaraciones de variables pueden ser de tipos primitivos o estructurados y además de esto se 
pueden hacer asignaciones iniciales. Adicionalmente, el lenguaje tiene soporte para arreglos de una y dos dimensiones, pero estos no pueden 
tener valor inicial.

Ejemplo:
```
vars
    int mat[3, 3];
    float x = 3.14, y, z;
    char a = 'a';
    Person obj, people[5];
```
#### Declaración de funciones o métodos
El usuario puede declarar sus propias funciones o módulos. Dado que no hay polimorfismo, las funciones deben tener nombres únicos
dentro del mismo contexto. Solamente se pueden definir parámetros de tipos primitivos y el tipo de retorno debe ser void
o primitivo. En el caso que no sea void, debe haber un estatuto **return** en el cuerpo de la función.

Ejemplo:
```
func int cyclicFactorial(int n) {
    vars
        int result = 1, i;
    
    from i=1 to n {
        result = result * i;
    }

    return(result);
}
```
#### Main
Es obligatorio incluir la función main. La estructura básica del main es:

```
main() {
    ...
}
```

#### Comentarios
TeamPlusPlus soporta comentarios de una sola línea estilo Python:

Ejemplo:
```
# Comentario
```

### Estatutos principales

#### Expresiones y Asignación
TeamPlusPlus maneja 3 tipos de expresiones:
- Aritméticas (+, -, *. /)
- Relacionales (<, >, <=, >=, ==, !=)
- Lógicas (and, or, not)

También, se pueden incluir operadores unarios de **+** (positivo) y **-** (negativo) en las expresiones.

Ejemplo:
```
vars
    int a, b, c, d;
    char x, y, z;

    a = (b + 2 - -1) * (c / 3);
    d = (x == y or z < x) and (not b);
    
```
#### Read
Existe en el lenguaje un estatuto de entrada de datos para una o más variables. Solamente se puede realizar lectura de tipos primitivos.

Ejemplo:
```
read(a, b);
```
#### Print
De la misma forma, también hay un estatuto de salida para uno o más elementos. Aquí, se puede desplegar el resultado de una expresión, o bien
un letrero.

Ejemplo:
```
print("Letrero", expresión);
```
#### Function Call
Se pueden hacer por su cuenta o también pueden usarse como parte de una expresión. Dentro de una expresión no se permiten llamadas a funciones
de tipo **void**.

Ejemplo:
```
obj.setAge(24);
f = fibonacci(10) + fibonacci(12);
```
#### If-Elif-Else
Este es uno de los dos estatutos multicondicionales que TeamPlusPlus soporta. El estatuto puede tener una cantidad infinita de **elif's**, y tanto el 
**elif** como el **else** son opcionales.

Ejemplo:
```
if (condición) {
    ...
} elif (condición) {
    ...
} else {
    ...
}
```
#### Switch
El segundo estatuto multicondicional que es parte del lenguaje es el **switch**. Aqui debe haber por lo menos un **case**, mientras que el 
**default** es opcional. El switch soporta variables de tipo entero y caracteres solamente.

Ejemplo:
```
switch(numero) {
    case 1 {...}
    case 2 {...}
    default {...}
}

switch(caracter) {
    case 'a' {...}
    ...
}
```
#### While Loop
TeamPlusPlus también permite el uso de dos estatutos cíclicos pre-condicionados. El primero es el **while**, que sigue una implementación
idéntica a C.

Ejemplo:
```
while(condición) {
    ...
}
```
#### From-To Loop
El segundo estatuto cíclico es el **from-to**. Aquí primero se asigna un valor inicial a la variable, y luego se define una expresión de terminación.
Es importante considerar que el estatuto avanza de inicio a fin, aumentado de uno en uno, y el último valor en el rango sí se incluye en el ciclo.

Ejemplo:
```
from variable = inicio to fin {
    ...
}
```
### Video Tutorial

Haz click en este [link](https://drive.google.com/file/d/19CwQ4ZBbF5-Bko2ej5xArDqHK3XBOj5L/view?usp=sharing) para ver una pequeña demostración del lenguaje.
