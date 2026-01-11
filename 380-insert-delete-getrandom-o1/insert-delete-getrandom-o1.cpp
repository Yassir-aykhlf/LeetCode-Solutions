class RandomizedSet {
private:
    std::vector<int> _vec;
    std::unordered_map<int, int> _val_idx;
public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (_val_idx.find(val) != _val_idx.end()) {
            return false;
        }
        _vec.push_back(val);
        _val_idx[val] = _vec.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (_val_idx.find(val) == _val_idx.end()) {
            return false;
        }
        int last = _vec.back();
        int idx = _val_idx[val];
        _vec[idx] = last;
        _vec.pop_back();
        _val_idx[last] = idx;
        _val_idx.erase(val);
        return true;
    }
    
    int getRandom() {
        return _vec[std::rand() % _vec.size()];
    }
};