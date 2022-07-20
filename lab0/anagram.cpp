#include <iostream>
#include <unordered_map>

int main(){
    string s = "abcde";
    unordered_map<char, int> isAng;

    for(char c1:s){
        isAng[c1]++;
    }

    for(auto check:isAng){
        std::cout << check.first << " " << check.second << std::endl;
    }


}