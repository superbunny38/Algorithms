/*
. C++ (The Compiler) C++ is like a printing press. You write the book (code), but before anyone can read it, it must go through a Compiler.

Phase 1: Compile Time (The "Build" Phase)

The Compiler reads your entire code.

It checks types (like our Concept work earlier).

It translates your C++ into Assembly (machine instructions that the CPU understands, like "move this number to register A").

It optimizes the logic.

Result: It creates an executable file (binary) like my_program.exe.

Note: The program is not running yet. No memory is allocated for variables yet.

Phase 2: Runtime (The "Run" Phase)

You double-click my_program.exe.

The OS allocates memory.

The CPU executes the assembly instructions the compiler generated.
*/

consteval int fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(){

    constexpr int result = fib(10); 
    return 0;
}