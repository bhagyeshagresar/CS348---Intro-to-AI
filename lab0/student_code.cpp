// #include <iostream>
// #include <vector>



// std::vector<int> order(std::vector<int> data_list){
//     int n = data_list.size(); //4

//     // if(data_list.empty()){
//     //     return data_list;
//     // }

//     for(int i = 0; i < n - 1; i++){
//         for(int j = i + 1; j < n; j++){
//             if(data_list.at(i) > data_list.at(j)){
//                 int m = data_list.at(i);
//                 data_list.at(i) = data_list.at(j);
//                 data_list.at(j) = m;
//             }
//         }
//     }





    return data_list;
}

int main(){
    std::vector<int> list{};

    std::vector<int> new_list = order(list);
    // order(list);
    // std::cout << new_list.at(0) << std::endl;
    // std::cout << new_list.at(1) << std::endl;
    // std::cout << new_list.at(2) << std::endl;
    // std::cout << new_list.at(3) << std::endl;

  
    return 0;
}