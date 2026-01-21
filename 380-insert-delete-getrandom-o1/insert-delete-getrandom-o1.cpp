class RandomizedSet {
private:
    std::vector<int> _vec;
    std::unordered_map<int, int> _val_idx;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (_val_idx.find(val) != _val_idx.end()){
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
        int val_idx = _val_idx[val];
        int lst_val = _vec.back();
        _vec[val_idx] = lst_val;
        _val_idx[lst_val] = val_idx;
        _vec.pop_back();
        _val_idx.erase(val);
        return true;
    }
    
    int getRandom() {
        return _vec[std::rand() % _vec.size()];
    }
};