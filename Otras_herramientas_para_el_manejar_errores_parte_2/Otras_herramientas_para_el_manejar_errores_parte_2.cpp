#include <iostream>
using namespace std;

int main(){
    double a,b,c;
    try
    {
        cout<<"Ingrese el primer valor: ";
        cin>>a;
        cout<<"Ingrese el segundo valor: ";
        cin>>b;
        if (b == 0)
            throw "No se puede dividir entre 0";
        c = a / b;
        cout<< c <<endl;
    }
    catch(const char *error)
    {
        cout<<"Error: "<<error<<endl;
    }
    return 0;
}
