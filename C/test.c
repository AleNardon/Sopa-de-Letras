#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>          //Biblioteca para las minusculas


int repetidos (char pal[60]){
    
    for (int indice = 0; pal[indice] != '\0'; ++indice){     //Dada una palabra convierte todos sus caracteres en minuscula 
        pal[indice] = tolower(pal[indice]);
    }
   
    char buff[200];
    FILE * fpointer = fopen("jugada.txt","r");               //Abrimos el archivo en modo lectura

    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);
    fscanf(fpointer,"%s",buff);                             //Nos posicionamos en la 4ta linea y guardamos su contenido en la variable buff

    int e = 0;                                              //Estado
    int l = lineas();                                       //Cantidad de jugadas que debe chequear si hay alguna repetida
    
    while ( l >= 0){
        if(strcmp(pal,buff) == 0){                          //Si la palabra es igual a una en el archivo
            e+=1;                                       
            break;                                         //Termina el loop
        }
        else{
            l--;                                        
            fscanf(fpointer,"%s",buff);                    //Continuamos a la siguiente linea
        }
    }
    fclose(fpointer);                                      //Cerramos el archivo 

    return e;
}