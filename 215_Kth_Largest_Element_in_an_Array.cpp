#include <iostream>
#include <vector> 

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // int output = nums[k];
        sort(nums.begin(), nums.end());
        cout << "Sorted \n";
        for (auto x : nums)
            cout << x << " ";

        int index = nums.size() - k;
        int output = nums[index];
        return output;
    }
};

// void printVector(vector<int> & vec) {
//         for (int i: vec) {
//             cout << i << ' ';
//         }
//     cout << endl;
// }

int main(){
    Solution s;
    vector<int> nums = {3,2,1,5,6,4};
    int ans = s.findKthLargest(nums, 2);
    cout << ans << endl;
    return 0; 
}