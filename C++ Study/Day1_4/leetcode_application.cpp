#include <iostream>
#include <vector>
#include <string>

using namespace std;


class Solution {
public:
    // Helper function for recursion
    // Note: We pass 'current' by VALUE so that each recursive call has its own independent copy.
    // This allows us to safely MOVE it at the end because we don't need to backtrack on this specific object.
    void backtrack(vector<int>& nums, vector<int> current, vector<vector<int>>& result) {
        
        // ------------------------------------------
        // 1. BASE CASE: The permutation is complete
        // ------------------------------------------
        if (current.size() == nums.size()) {
            // TASK: Add 'current' to 'result'.
            // Optimization Hint: Since 'current' is a local variable that 
            // is about to die at the closing brace }, we don't need to copy it.
            // Steal its guts!
            
            result.push_back(move(current));
            return;
        }

        // ------------------------------------------
        // 2. RECURSIVE STEP
        // ------------------------------------------
        for (int num : nums) {
            // Logic to check if 'num' is already in 'current'
            // (You can use std::find or a separate boolean visited array)
            bool exists = false;
            for (int x : current) {
                if (x == num) { exists = true; break; }
            }
            
            if (!exists) {
                // Prepare the next state
                vector<int> next_state = current; // Copy current state
                next_state.push_back(num);        // Add new number
                
                // Recurse
                backtrack(nums, move(next_state), result);
                
                // Note: Because we passed 'next_state' by value (or moved it), 
                // we don't need to manually pop_back() here. The state is handled by the call stack.
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> empty_start;
        
        // Start the recursion
        backtrack(nums, empty_start, result);
        
        return result;
    }
};  