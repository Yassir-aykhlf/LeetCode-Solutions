class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stack;

        for (const std::string &token : tokens) {
            if (token == "+" || token == "-" || token == "/" || token == "*") {
                int b = stack.top(); stack.pop();
                int a = stack.top(); stack.pop();
                
                if (token == "+") stack.push(a + b);
                else if (token == "-") stack.push(a - b);
                else if (token == "*") stack.push(a * b);
                else if (token == "/") stack.push(a / b);
            }
            else {
                stack.push(std::stoi(token));
            }
        }
        return stack.top();
    }
};