// uniform_real_distribution example
#include <iostream>
#include <chrono>
#include <iomanip> 
#include <random>

using namespace std;

double time=0;

// construct a trivial random generator engine from a time-based seed:
unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
default_random_engine generator (seed);

uniform_real_distribution<double> distributionPiezasA (5.0,7.0);
uniform_real_distribution<double> distributionPiezasB (3.0,5.0);
uniform_real_distribution<double> distributionTorneado (1.0,3.0);




int main(){

    
    

}