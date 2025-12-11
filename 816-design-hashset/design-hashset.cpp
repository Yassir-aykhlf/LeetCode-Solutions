class MyHashSet {
    const int buckets_size = 997;
    std::vector<std::list<int>> buckets;
    int hash(int nbr) {
        return nbr % buckets_size;
    }
public:
    MyHashSet() {
        buckets.resize(buckets_size);
    }
    
    void add(int key) {
        auto &chain = buckets[hash(key)];
        // for (auto element : chain) {

        // }
        chain.push_front(key);
    }
    
    void remove(int key) {
        auto &chain = buckets[hash(key)];
        chain.remove(key);
    }
    
    bool contains(int key) {
        auto &chain = buckets[hash(key)];
        for (int element : chain) {
            if (element == key) {
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