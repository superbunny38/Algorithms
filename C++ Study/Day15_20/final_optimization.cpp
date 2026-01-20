#include <iostream>
#include <string>
using namespace std;

/*
Before:
struct UserSession {
    bool is_active;           // 1 byte
    std::string* username;    // 8 bytes (Pointer to heap!)
    int user_id;             // 4 bytes
    double timeout;          // 8 bytes
};

*/

struct UserSession
{
    bool is_active;
    int user_id;
    double timeout;
    string username;
};//48bytes (1 + 3 + 4 + 8 + 32)



/*
1. The "Hidden Cost" of the Pointer
Let's trace exactly what happens in memory for both versions.

Version A: The Pointer (std::string* username) Your struct on the Stack is small (32 bytes). But username is just a pointer. It points to a std::string object that must live somewhere else (on the Heap).

Stack: 32 bytes (The struct).

Heap Allocation #1: ~32 bytes (The std::string object itself).

Heap Allocation #2: ~16+ bytes (The actual character data, if not SSO).

TOTAL Memory Footprint: ~80 bytes.

Version B: The Embedded Object (std::string username) The string lives inside the struct.

Stack: 48 bytes.

Heap: 0 bytes (Assuming SSO holds the text).

TOTAL Memory Footprint: 48 bytes.

The Verdict: The "smaller" struct actually uses nearly 2x more memory in total once you account for what it points to.

2. The Real Enemy: Latency (Pointer Chasing)
Even if memory size wasn't an issue, Speed is the deciding factor.

In the Pointer version, to read the username, the CPU has to:

Read the UserSession struct (Stack).

STOP. Wait for the pointer address.

Jump to a random location in the Heap to find the std::string object. (Cache Miss: ~200 cycle penalty).

Read the string object.

STOP. Wait for the internal buffer pointer.

Jump to another random location to find the characters "Alice". (Cache Miss: ~200 cycle penalty).
*/