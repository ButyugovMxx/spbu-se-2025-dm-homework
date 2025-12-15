#include <iostream>
#include <string>
#include <vector>

int n;
std::vector<std::string> a;
std::vector<bool> used;
std::vector<std::string> cur_perestanovka;

void podschet_perestanovok(){
    if(cur_perestanovka.size() == n){
        for(int i = 0; i < n; i++){
            if(i != n-1 ) std::cout<< cur_perestanovka[i] << ' ';
            else { std::cout<< cur_perestanovka[i] << "\n"; }
        }
        return;
    }
    for(int i = 0; i < n; i++){
        if(!used[i]){
            used[i] = 1;
            cur_perestanovka.push_back(a[i]);
            podschet_perestanovok();
            cur_perestanovka.pop_back();
            used[i] = 0;
        }
    }
}    

int main(){

    std::cin >> n;
    if(n > 8 || n < 1 ) return 0;
    
    a.resize(n);
    for(size_t i = 0; i < n; i++) std::cin >> a[i];

    used.assign(n, 0);
    
    podschet_perestanovok();


}