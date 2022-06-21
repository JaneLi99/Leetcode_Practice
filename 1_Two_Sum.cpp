#include <iostream>
#include <vector> 

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> & nums, int target) {
        vector<int> ret;
        for (int i = 0; i < nums.size(); i ++){
            for (int j = i + 1; j < nums.size(); j ++){
                int sum = nums[i] + nums[j];
                if (sum == target){
                    ret = {i, j}; 
                }

            }
        }
        return ret;
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
    vector<int> nums = {2, 7, 11, 5};
    vector<int> ans = s.twoSum(nums, 9);
    // printVector(ans);

    return 0; 
}