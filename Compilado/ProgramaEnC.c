#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>          //Biblioteca para las minusculas


//------------------------------
//NOTA: Este programa carece de tests debido a que todas sus funciones iteran con archivos por lo que no se vio la viabilidad
//      de realizar los mismos.
//------------------------------


//-------------
//introduccion: None -> None 
//Imprime las instrucciones de la orientación.
void introduccion(){

    printf("Bienvenido a la SOPA DE LETRAS.\n\nA continuación mostrara un cartel con las orientaciones correspondientes a las palabras que ingresaran en la sopa.\n\n");
    printf("----------------------------------------------\n");
    printf("0 es Horizontal de izquierda a derecha\n\n");
    printf("1 es Horizontal de derecha a izquierda\n\n");
    printf("2 es Vertical de arriba a bajo");
    printf("2 es Vertical de arriba a bajo\n\n");
    printf("3 es Vertical de abajo a arriba\n\n");
    printf("4 es Diagonal de izquierda arriba a derecha abajo\n\n");
    printf("5 es Diagonal de izquierda abajo a derecha arriba\n");
    printf("----------------------------------------------\n\n\n");
}

//-------------
//dimension: None -> None
//Crea o reescribe un archivo llamado jugada donde a través de un input deberemos ingresar la dimensión de nuestra sopa de letras teniendo en cuenta 
// que es de forma cuadrada por lo que dado un numero n realizara una sopa del tamaño n*n. Y luego escribirá en el archivo DIMENSIÓN \n int n \n PALABRAS.
void dimension(){
    int t;
    printf("Ingrese la dimension deseada para la sopa: ");
    scanf("%d", &t);
    printf("\n\n");


    while (t<0)           //Si el número es menor a 0, repetimos hasta que se ingrese correctamente.
    {
        printf("----------Error ingreso un numero no valido, pruebe con naturales mayores a 0.----------\n\n");
        printf("Ingrese la dimension deseada para la sopa: ");
        scanf("%d", &t);
    }
    
    FILE * fpointer = fopen("jugada.txt","w");                              //Sobreescribimos o creamos el archivo con el nombre jugada.txt.
    
    fprintf(fpointer,"DIMENSION\n%d\nPALABRAS",t);                          //Escribimos en el archivo la dimensión de la sopa.

    fclose(fpointer);                                                       //Cerramos el archivo.
}
//-------------
//aggPalabra: str int -> None
//Dada una palabra y un número los escribimos al final del txt de este modo (str int).
//Espacio limitado de 60 caracteres en el char por que convenimos en que ninguna palabra tendrá una cifra de caracteres mayor a 60.
void aggPalabra(char pal [60],int n){

    for (int indice = 0; pal[indice] != '\0'; ++indice){    //Dada una palabra convierte todos sus caracteres en minúscula.
        pal[indice] = tolower(pal[indice]);
    }

    FILE * fpointer = fopen("jugada.txt","a");              //Abrimos el archivo y nos ubicamos en la ultima línea.
    
    fprintf(fpointer,"\n%s %d",pal,n);                      //Agregamos la jugada del tipo (str int).

    fclose(fpointer);                                       //Cerramos el archivo.
}

//-------------
//lineas: None -> Int
//Devuelve la cuenta del total de jugadas que se realizaron en el archivo, es decir todas las lineas, sin contar las 3 primeras.
//También multiplicamos por dos este resultado, debido a que cada jugada representa 2 lineas una el str y otra el int.
int lineas(){
    FILE * fpointer = fopen("jugada.txt","r");         //Abrimos el archivo en modo lectura.
    int c, n =1;
    while((c = fgetc(fpointer)) != EOF){               //En este caso EOF hará referencia a que llegó al final del archivo.
        if( c == '\n'){                                //Si hay un salto de linea suma 1.
            n++;                                       //Sumamos 1.
        }
    }
    fclose(fpointer);                                  //Cerramos el archivo.
    n = n-3;                                           //Restamos las 3 primeras lineas.
    n = n*2;                                           //Multiplicamos por 2 debido a que a cada linea la debe tomar como 2 lineas, en una la palabra y en la otra el número.
    return n;
}

//-------------
//repetidos: str -> int
//Dado un str nos devuelve 1 si es que este str esta repetido en el archivo a partir de la 4ta linea, en caso contrario devuelve 0.
int repetidos (char pal[60]){
    
    for (int indice = 0; pal[indice] != '\0'; ++indice){     //Dada una palabra convierte todos sus caracteres en minúscula.
        pal[indice] = tolower(pal[indice]);
    }
   
    char buff[200]; 
    FILE * fpointer = fopen("jugada.txt","r");               //Abrimos el archivo en modo lectura.

    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);                             //Nos posicionamos en la 4ta linea y guardamos su contenido en la variable buff.

    int e = 0;                                              //Estado.
    int l = lineas();                                       //Cantidad de jugadas que debe chequear.
    while ( l >= 0){
        if(strcmp(pal,buff) == 0){                          //Si la palabra es igual a una en el archivo.
            e+=1;                                       
            break;                                          //Termina el loop.
        }
        else{
            l--;                                        
            fscanf(fpointer,"%s",buff);                    //Continuamos a la siguiente linea.
        }
    }
    fclose(fpointer);                                      //Cerramos el archivo. 

    return e;
}

//-------------
//termina: None -> int
//Hacemos una función que pregunta al usuario si quiere terminar, si desea esto deberá digitar "BASTA" y el programa devolvera 1, en caso contrario deberá digitar 0 y devolverá 0.
//Estará en loop hasta digitar algo válido.
int termina(){
    char pal[60];

    printf("\nSi desea seguir jugando presione 0 de lo contario escriba BASTA: ");
    scanf("%s", &pal);
    printf("\n");


    while (strcmp(pal,"BASTA") == 1 && strcmp(pal,"0") == 1){                           //Si no se ingresa 0 o BASTA lo volverá a pedir hasta que se ingrese alguno de las dos opciones.
        printf("\n\n----------Error ingreso no valido.----------\n\n");
        printf("Si desea seguir jugando presione 0 de lo contario escriba BASTA: ");
        scanf("%s", &pal);
        printf("\n");
    }
    
    if (strcmp(pal, "BASTA") == 0){                                                     //Si es BASTA devuelve 1.
        return 1;
    }
    else{
        return 0;
    }
}

//-------------
//main: None -> int
//Es la función madre, en esta estarán todas las funciones anteriores y hacemos el ingreso de la palabra y la orientación 
// que tendrá. Se repetirá hasta que no se ingrese una orientación válida o una palabra que no este repetida.

int main (){
    introduccion();
    dimension();                                                                        //Preguntamos el tamaño de la sopa y lo agregamos al archivo.

    int o;
    char pal[60];

    printf("Ingrese la palabra deseada con su orientacion con numeros del 0 al 5: ");   //Ingreso de la primer palabra con su orientación.
    scanf("%s%d", &pal, &o);
    
    
    while (o<0 || o>5){                                                                 //Si la orientación no es válida
        printf("\n\n----------Error ingreso un numero no valido, pruebe con numeros del 0 al 5.----------\n\n");
        printf("Ingrese la orientacion deseada para la palabra %s: ",pal);              //Obliga a ingresar una orientación válida.
        scanf("%d", &o);
    }

    aggPalabra(pal,o);                                                                  //Agrega la jugada.
    
    int t = termina();                                                                  //Pregunta si quiere terminar.
    

    while (t==0){
        printf("Ingrese la palabra deseada con su orientacion con numeros del 0 al 5: ");  //Genera una nueva jugada.
        scanf("%s%d", &pal, &o);

        int r = repetidos(pal) ;                                                           //Pregunta si la palabra esta repetida.
        
        if (r == 1){                                                                       //Si esta repetida.
            printf("\n\n----------Error, ingreso una palabra repetida.----------\n\n");    //Emite un aviso de error.
            t = termina();                                                                 //Pregunta si termina o sigue.
        }

        else{
            while (o<0 || o>5){                                                            //Si la palabra es válida, se fija si la orientación es válida.
                printf("\n\n----------Error ingreso un numero no valido, pruebe con numeros del 0 al 5.----------\n\n");    //Emite aviso de error.
                printf("Ingrese la orientacion deseada para la palabra %s: ",pal);         
                scanf("%d", &o);                                                           //Obliga a ingresar una orientación válida.
            }    

            aggPalabra(pal,o);                                                             //Agrega la palabra.
            t=termina();                                                                   //Pregunta si termina o sigue.
        }
    }
    
    return 0;

}
