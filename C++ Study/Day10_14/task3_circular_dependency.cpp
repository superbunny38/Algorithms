/*
std::weak_ptr is useful whenever you need to reference an object without owning it or extending its lifetime.
*/

#include <stdio.h>
#include <cstdio>
#include <iostream>
#include <memory>

using namespace std;

class Node{
    
    public:
    shared_ptr<Node> partner;
    Node(){}
    ~Node(){cout<<"Node destroyed"<<endl;}
};

// destructors never run

int main(){
    auto A = make_shared<Node>();
    auto B = make_shared<Node>();

    A->partner = B;
    B->partner = A;
}