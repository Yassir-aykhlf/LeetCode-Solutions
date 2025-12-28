class MinStack {
private:
    std::stack<std::pair<int, int>> _stk;
public:
    MinStack() {}
    
    void push(int val) {
        _stk.emplace(val, _stk.empty() ? val : std::min(val, _stk.top().second));
    }
    
    void pop() {
        _stk.pop();
    }
    
    int top() {
        return _stk.top().first;
    }
    
    int getMin() {
        return _stk.top().second;
    }
};