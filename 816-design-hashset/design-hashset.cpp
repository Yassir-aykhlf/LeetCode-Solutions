class MyHashSet {
private:
    size_t capacity = 997;
    std::vector<std::list<int>> _hashset;
    int hash(int key) {
        return key % capacity;
    }
public:
    MyHashSet() {
        _hashset.resize(capacity);
    }
    
    void add(int key) {
        auto &chain = _hashset[hash(key)];
        if (this->contains(key)) {
            return;
        }
        chain.push_back(key);
    }
    
    void remove(int key) {
        auto &chain = _hashset[hash(key)];
        for (auto itr = chain.begin(); itr != chain.end(); ++itr) {
            if (*itr == key) {
                chain.erase(itr);
                return;
            }
        }
    }
    
    bool contains(int key) {
        auto &chain = _hashset[hash(key)];
        for (auto &el : chain) {
            if (el == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */