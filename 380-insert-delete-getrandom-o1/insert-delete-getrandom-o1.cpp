class RandomizedSet {
private:
    std::vector<int> vals;
    std::unordered_map<int, int> val_idx;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if (val_idx.find(val) != val_idx.end()) {
            return false;
        }
        vals.push_back(val);
        val_idx[val] = vals.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (val_idx.find(val) == val_idx.end()) {
            return false;
        }
        int del_idx = val_idx[val];
        int last_val = vals.back();
        vals[del_idx] = last_val;
        vals.pop_back();
        val_idx[last_val] = del_idx;
        val_idx.erase(val);
        return true;
    }
    
    int getRandom() {
        return vals[std::rand() % vals.size()];
    }
};

/**
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]
 */