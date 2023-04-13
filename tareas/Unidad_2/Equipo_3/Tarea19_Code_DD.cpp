#include <stdio.h>
main(){
    int i,j,k,n=6,m=8,diagonal,paso;
    double numerador=0,denominador=0,polinomio=0,factor=0,termino=0,dDividida[5]={0},x[]={1,4,5,6,8,12},xi[]={2,3,7,9,10,11},fi[]={2330,2950,3735,3178,3532,4556},
    tabla[n][m]={
        {0,2,2330,0,0,0,0,0},
        {1,3,2950,0,0,0,0,0},
        {2,7,3735,0,0,0,0,0},
        {3,9,3187,0,0,0,0,0},
        {4,10,3532,0,0,0,0,0},
        {5,10,4556,0,0,0,0,0}};
    diagonal = n-1;
    j = 3;
    while(j < m){
        i = 0;
        paso = j-2;
        while(i < diagonal){
            denominador = (xi[i+paso]-xi[i]);
            numerador = tabla[i+1][j-1]-tabla[i][j-1];
            tabla[i][j] = numerador/denominador;
            i++;
        }
        diagonal = diagonal - 1;
        j++;
    }
    printf("TABLA:\n");
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            printf("%lf\t",tabla[i][j]);
        }
        putchar('\n');
    }
    for(j=3,i=0;j<m;j++,i++){
        dDividida[i]=tabla[0][j];
    }
    for(i=0;i<6;i++){
        printf("\nPara x = %lf",x[i]);
        polinomio = fi[0];  
        for(j=1;j<n;j++){
            factor = dDividida[j-1];
            termino = 1;
            for(k=0;k<j;k++){
                termino = termino*(x[i]-xi[k]);
            }
            polinomio = polinomio + termino*factor;
        }
        printf("\nP(x) = %lf\n",polinomio);
    }
}