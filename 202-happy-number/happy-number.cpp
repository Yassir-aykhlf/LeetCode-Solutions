class Solution {
private:
    int calcSum(int n) {
        int res = 0;
        while (n) {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }
public:
    bool isHappy(int n) {
        int slow = n;
        int fast = n;
        while (true) {
            slow = calcSum(slow);
            fast = calcSum(calcSum(fast));
            if (slow == fast) {
                return slow == 1;
            }
        }
    }
};