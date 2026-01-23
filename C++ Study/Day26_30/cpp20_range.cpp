#include <iostream>
#include <vector>
#include <string>
#include <ranges>

using namespace std;

struct Ad{
    int id;
    string region;
    double score;
};


//set up sample data
vector<Ad> ads = {
    { .id = 1, .region = "US", .score = 10.5 },
    { .id = 2, .region = "UK", .score = 8.0 },
    { .id = 3, .region = "US", .score = 12.0 },
    { .id = 4, .region = "CA", .score = 7.5 },
    { .id = 5, .region = "US", .score = 9.0 },
    { .id = 6, .region = "IN", .score = 15.0 }
};

//lazy view
auto final_results = ads
    |std::views::filter([](const auto& ad){return ad.region == "US";})
    |std::views::transform([](const auto& ad){return ad.score * 1.5;})
    |std::views::take(3);

int main(){
    cout << "Top 3 Boosted US Ad Scores:" << endl;
    for (double score : final_results) {
        cout << "- " << score << endl;
    }
    return 0;
}
