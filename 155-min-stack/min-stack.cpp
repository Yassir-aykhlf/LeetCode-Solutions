class MinStack {
private:
    std::list<int> _min;
    std::deque<int> c;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (_min.empty() || _min.back() >= val) {
            _min.push_back(val);
        }
        c.push_back(val);
    }
    
    void pop() {
        if (!_min.empty() && c.back() == _min.back()) {
            _min.pop_back();
        }
        c.pop_back();
    }
    
    int top() {
        return c.back();
    }
    
    int getMin() {
        return _min.back();
    }
};