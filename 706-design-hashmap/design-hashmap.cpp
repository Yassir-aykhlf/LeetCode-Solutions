class MyHashMap {
    int buckets_size = 997;
    std::vector<std::list<std::pair<int, int>>> buckets;
    int hash(int key) {
        return key % buckets_size;
    }
public:
    MyHashMap() {
        buckets.resize(buckets_size);
    }
    
    void put(int key, int value) {
        auto &chain = buckets[hash(key)];
        for (auto &element : chain) {
            if (element.first == key) {
                element.second = value;
                return;
            }
        }
        chain.push_back({key, value});
    }
    
    int get(int key) {
        auto &chain = buckets[hash(key)];
        for (const auto &element : chain) {
            if (element.first == key) {
                return element.second;
            }
        }
        return -1;
    }
    
    void remove(int key) {
        auto &chain = buckets[hash(key)];
        for (auto it = chain.begin(); it != chain.end(); ++it) {
            if (it->first == key) {
                chain.erase(it);
                return;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */