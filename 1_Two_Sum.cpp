#include <iostream>
#include <vector> 

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> & nums, int target) {
        //Solution 1
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

        //Solution 2
        /*
        vector<int> result;
        for(auto it1 = nums.begin(); it1 != nums.end(); ++it1){
            auto it2 = find(it1 + 1, nums.end(), target - *it1);
            if(it2 != nums.end()){ //found the number
                result.push_back(it1 - nums.begin());
                result.push_back(it2 - nums.begin());
                break;
            }
        }
        return result;
        */

        //Solution 3
        /*
        unordered_map<int, int> _map;
        for (int i = 0; i < nums.size(); ++i){
            int num = nums[i];
            int complement = target - num;
            auto it = _map.find(complement);
            if(it != _map.end()){//found
                return {it->second, i};
            }
            _map[num] = i;
        }
        return {};
        */
    }
};

// Another Solution
class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(auto it1 = nums.begin(); it1 != nums.end(); ++it1){
            auto it2 = find(it1 + 1, nums.end(), target - *it1);
            if(it2 != nums.end()){ //found the number
                result.push_back(it1 - nums.begin());
                result.push_back(it2 - nums.begin());
                break;
            }
        }
        return result;
    }
};

int main(){
    Solution s;
    vector<int> nums = {2, 7, 11, 5};
    vector<int> ans = s.twoSum(nums, 9);
    // printVector(ans);

    return 0; 
}