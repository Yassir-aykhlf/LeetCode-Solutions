class MyHashSet {
private:
    const int size = 997;
    std::vector<std::list<int>> bucket;
    int hash(int key) {
        return key % size;
    }
public:
    MyHashSet() {
        bucket.resize(size);
    }
    
    void add(int key) {
        auto &chain = bucket[hash(key)];
        for (auto el : chain) {
            if (el == key) {
                return;
            }
        }
        chain.push_back(key);
    }
    
    void remove(int key) {
        auto &chain = bucket[hash(key)];
        for (auto itr = chain.begin(); itr != chain.end(); ++itr) {
            if (*itr == key) {
                chain.erase(itr);
                return;
            }
        }
    }
    
    bool contains(int key) {
        auto &chain = bucket[hash(key)];
        for (auto el : chain) {
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