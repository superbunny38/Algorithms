#include <iostream>

template <typename T>
class Auto_ptr2
{
    // The "raw" pointer variable. 
    // This holds the actual memory address (e.g., 0x500).
    // It is private, so only this class can touch it.
    T* m_ptr {}; 

public:
    // ---------------------------------------------------------
    // 1. CONSTRUCTOR
    // ---------------------------------------------------------
    // This runs when you type: Auto_ptr2<Resource> res(new Resource());
    Auto_ptr2(T* ptr=nullptr)
        :m_ptr(ptr) // The raw address (0x500) is saved into m_ptr immediately.
    {
    }

    // ---------------------------------------------------------
    // 2. DESTRUCTOR
    // ---------------------------------------------------------
    // This runs automatically when the variable goes out of scope (at the closing '}').
    ~Auto_ptr2()
    {
        // Delete the memory at the address we are holding.
        // If m_ptr is nullptr (0x0), this command does nothing (safe).
        delete m_ptr; 
    }

    // ---------------------------------------------------------
    // 3. COPY CONSTRUCTOR (The "Stealing" Constructor)
    // ---------------------------------------------------------
    // This runs when you create a NEW variable from an OLD one.
    // Example: Auto_ptr2<Resource> res2(res1);
    // Note: 'a' is the old variable (res1). We are the new variable (res2).
    Auto_ptr2(Auto_ptr2& a) 
    {
        // STEP A: Copy the address.
        // We take the address (0x500) from 'a' and put it in our own m_ptr.
        // Now we own the Resource.
        m_ptr = a.m_ptr; 

        // STEP B: Nullify the source.
        // We set 'a.m_ptr' to nullptr (0x0).
        // This ensures that when 'a' dies, its destructor will delete nothing.
        // We have successfully "stolen" the pointer.
        a.m_ptr = nullptr; 
    }

    // ---------------------------------------------------------
    // 4. ASSIGNMENT OPERATOR (The "Stealing" Update)
    // ---------------------------------------------------------
    // This runs when you update an EXISTING variable.
    // Example: res2 = res1;
    // Note: 'a' is the source (res1). 'this' is the destination (res2).
    Auto_ptr2& operator=(Auto_ptr2& a) 
    {
        // STEP A: Self-Assignment Check
        // Are we writing "res1 = res1;"?
        // If yes, stop immediately. Stealing from yourself is dangerous.
        if (&a == this)
            return *this;

        // STEP B: Clean up our current mess.
        // If res2 was already holding a Resource, we must delete it first.
        // Otherwise, that memory would leak (be lost forever) when we overwrite m_ptr.
        delete m_ptr; 

        // STEP C: Copy the address.
        // Take the address (0x500) from res1 and save it to res2.
        m_ptr = a.m_ptr; 

        // STEP D: Nullify the source.
        // Set res1's pointer to nullptr (0x0).
        // Now res1 is empty. It owns nothing.
        a.m_ptr = nullptr; 

        // Return a reference to ourselves (required by C++ syntax).
        return *this;
    }

    // Helper functions to make the pointer act like a real pointer
    T& operator*() const { return *m_ptr; } // Allow usage like *res
    T* operator->() const { return m_ptr; } // Allow usage like res->
    bool isNull() const { return m_ptr == nullptr; } // Check if empty
};

class Resource
{
public:
    Resource() { std::cout << "Resource acquired\n"; }
    ~Resource() { std::cout << "Resource destroyed\n"; }
};

int main()
{
    // 1. Create res1. 
    // It calls the Constructor. m_ptr is, say, 0x500.
    // Output: "Resource acquired"
    Auto_ptr2<Resource> res1(new Resource());
    
    // 2. Create res2.
    // It calls the Constructor with no arguments. m_ptr is nullptr (0x0).
    Auto_ptr2<Resource> res2; 

    // Print status
    std::cout << "res1 is " << (res1.isNull() ? "null\n" : "not null\n"); // Prints: not null
    std::cout << "res2 is " << (res2.isNull() ? "null\n" : "not null\n"); // Prints: null

    // -------------------------------------------------
    // 3. THE TRANSFER (Move Semantics)
    // -------------------------------------------------
    // calls: res2.operator=(res1)
    res2 = res1; 

    // Inside that function:
    // a. res2 deletes its current pointer (which was null, so nothing happens).
    // b. res2 copies 0x500 from res1. (res2 is now 0x500).
    // c. res1 is set to nullptr. (res1 is now 0x0).
    
    std::cout << "Ownership transferred\n";

    // Print status again
    std::cout << "res1 is " << (res1.isNull() ? "null\n" : "not null\n"); // Prints: null
    std::cout << "res2 is " << (res2.isNull() ? "null\n" : "not null\n"); // Prints: not null

    return 0;
    
    // -------------------------------------------------
    // 4. END OF SCOPE
    // -------------------------------------------------
    // a. res2 dies first. 
    //    Its m_ptr is 0x500. It calls "delete 0x500".
    //    Output: "Resource destroyed".
    //
    // b. res1 dies next.
    //    Its m_ptr is nullptr (because we stole it!).
    //    It calls "delete nullptr".
    //    Result: Nothing happens. Safe.
} 