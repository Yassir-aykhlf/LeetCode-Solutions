class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int l = 0;
        int r = people.size() - 1;
        int count = 0;
        while (l <= r) {
            int weight = people[l] + people[r];
            if (weight <= limit) {
                l += 1;
            }
            r -= 1;
            count += 1;
        }
        return count;
    }
};