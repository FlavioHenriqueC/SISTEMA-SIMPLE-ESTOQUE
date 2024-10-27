#include <stdio.h>


#define varconst 100;

int main(){

    int x;
    float c = 20.9;
    x = varconst;
    
    //scanf("%d", &x);
    printf("constante =%d", x);
     

    return 0;

}


#include <stdio.h>

int main(){

int x, y;

x = 10; y = x++;

printf("y = x++ : valor de y => %d\n", y);

printf("y = x++ : valor de x => %d\n\n", x);

x = 10; y = x--;

printf("y = x-- : valor de y => %d\n", y);

printf("y = x-- : valor de x => %d\n\n", x);

x = 10; y = ++x;

printf("y = ++x : valor de y => %d\n", y);

printf("y = ++x : valor de x => %d\n\n", x);

x = 10; y = --x;

printf("y = --x : valor de y => %d\n", y);

printf("y = --x : valor de x => %d\n\n", x);

return 0;

}


#include <stdio.h>

int main(){

int n1, n2;

printf(“Digite o primeiro numero: “);

scanf(“%d”, &n1);

printf(“Digite o segundo numero: “);

scanf(“%d”, &n2);

printf(“\n n1 e n2 sao iguais? %d”, n1==n2);

printf(“\n n1 e maior que n2? %d”, n1>n2);

printf(“\n n1 e menor ou igual a n2? %d”, n1<=n2);

return 0;

}



#include <stdio.h>

int main(){

int a=5, b=10, c=5;

printf(“\n (a==b)&&(a==c) = %d”, ((a==b)&&(a==c)));

printf(“\n (a==b)||(a==c) = %d”, ((a==b)||(a==c)));

printf(“\n !(a==b)||(a==c) = %d”, !((a==b)||(a==c)));

return 0;

}