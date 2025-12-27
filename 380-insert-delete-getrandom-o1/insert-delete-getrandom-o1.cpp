class RandomizedSet {
private:
    std::vector<int> vals;
    std::unordered_map<int, int> val_idx;
public:
    RandomizedSet() {
        std::srand(std::time(0));
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
        int del = val_idx[val];
        int last = vals.back();
        vals[del] = last;
        val_idx[last] = del;
        vals.pop_back();
        val_idx.erase(val);
        return true;
    }
    
    int getRandom() {
        return vals[std::rand() % vals.size()];
    }
};