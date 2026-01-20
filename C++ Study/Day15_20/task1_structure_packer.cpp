#include <cstdint> // For int64_t, int32_t (or <stdint.h> in C/C++)
#include <iostream> // Useful for printing/debugging, not strictly needed for the struct

using namespace std;

struct PacketHeader {
    bool is_valid;      // 1 byte
    int64_t timestamp;  // 8 bytes
    bool has_payload;   // 1 byte
    int32_t id;         // 4 bytes
};//24 bytes

//Reorder

struct PacketHadder_reordered
{
    bool is_valid_ro;
    bool has_payload_ro;
    int32_t id;
    int64_t timestamp_ro;
};//16bytes


int main(){
    cout << sizeof(PacketHeader)<<endl;
    cout << sizeof(PacketHadder_reordered)<<endl;
    return 0;
}