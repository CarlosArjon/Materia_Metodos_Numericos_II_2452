#include<stdio.h>
#include<math.h>
bool calcConv(double []);
void calcG(double [],double []);
double Error(double [],double []);
main()
{
    int k=1;
    double x[2]={0.2,0.35},x_aux[2]={0},er=0;
    do{
        printf("\nIteracion %d\n",k);
        if(calcConv(x)==false)
            return 0;
        else
        {
            calcG(x,x_aux);
            printf("\nx(%d) = %lf\ny(%d) = %lf\n",k,x[0],k,x[1]);
            er=Error(x,x_aux);
            printf("\nError = %lf\n",er);
            k++;
        }
    }while(er>pow(10,-6));
}
bool calcConv(double v[]){
    double a[2]={0};
    a[0]=abs(0)+abs((0.25)*cos(v[0]));
    a[1]=abs(sqrt(0.2))+abs((-0.25)*sin(v[1]));
    if(a[0]>1||a[1]>1)
    {
        printf("\nNo converge\na[0] = %lf >= 1\na[1] = %lf >= 1\n",a[0],a[1]);
        return false;
    }
    else
    {
        printf("\nConverge\na[0] = %lf < 1\na[1] = %lf < 1\n",a[0],a[1]);
        return true;
    }
}
void calcG(double v[],double v2[]){
    v2[0]=v[0];
    v2[1]=v[1];
    v[0]=v2[1]*sqrt(0.2);
    v[1]=(0.25)*(sin(v2[0])+cos(v2[1]));
}
double Error(double v[],double v2[]){
    return sqrt(pow(v[0]-v2[0],2)+pow(v[1]-v2[1],2));
}
