#include<stdio.h>
main(){
    double xi[]={0,0.10,0.40,0.80,1},x[]={0,0.10,0.40,0.60,0.80,1},fi[]={0,0.30,0.55,1.10,1.15},polinomio=0,numerador,denominador,terminoLi=0;
    int n=5;
    for(int k=0;k<6;k++){
        printf("\nx = %lf\n",x[k]);
        for(int i=0;i<n;i++){
            numerador=1;
            denominador=1;
            for(int j=0;j<n;j++){
                if(j!=i){
                    numerador=numerador*(x[k]-xi[j]);
                    denominador=denominador*(xi[i]-xi[j]);
                }
            }
            terminoLi=numerador/denominador;
            polinomio=polinomio+terminoLi*fi[i];
        }
        printf("P(x) = %lf\n",polinomio);
        polinomio=0;
    }
}