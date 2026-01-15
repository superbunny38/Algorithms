#include <queue>
#include <vector>
#include <iostream>
#include <string>


struct  Ad
{
    /* data */
    std::string id;
    double bid;
    double quality;
};

auto adComparator = [](const Ad& a, const Ad& b) {
    // 1. Calculate score for 'a'
    auto score_a = a.bid*0.7 + a.quality*0.3;
    
    // 2. Calculate score for 'b'
    auto score_b = b.bid*0.7 + b.quality*0.3;
    
    // 3. Return true if score_a is LESS THAN score_b
    return (score_a<score_b);
    // (This pushes 'b' to the top)
};

int main(){
    // <Data Type, Container Type, Comparator Type>
    std::priority_queue<Ad, std::vector<Ad>, decltype(adComparator)> ads_queue(adComparator);
    ads_queue.push({ "Ad_1", 10.0, 5.0 });
    ads_queue.push({ "Ad_2", 1.0, 15.0 });
    ads_queue.push({ "Ad_3", 2.0, 2.0 });

    std::cout << ads_queue.top().id<<std::endl;;


    return 0;
}