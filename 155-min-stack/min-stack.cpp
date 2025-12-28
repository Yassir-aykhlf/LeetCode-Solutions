class MinStack {
private:
    std::stack<int> _stk;
    std::stack<int> _min;
public:
    MinStack() {}
    
    void push(int val) {
        if (_min.empty() || _min.top() >= val) {
            _min.push(val);
        }
        _stk.push(val);
    }
    
    void pop() {
        if (_min.top() == _stk.top()) {
            _min.pop();
        }
        _stk.pop();
    }
    
    int top() {
        return _stk.top();
    }
    
    int getMin() {
        return _min.top();
    }
};