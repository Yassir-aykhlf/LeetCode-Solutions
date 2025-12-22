class MyHashMap {
    const int size = 997;
    std::vector<std::list<std::pair<int, int>>> bucket;
    int hash(int key) {
        return key % size;
    }
public:
    MyHashMap() {
        bucket.resize(size);
    }
    
    void put(int key, int value) {
        auto &chain = bucket[hash(key)];
        for (auto &pair : chain) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        chain.push_back({key, value});
    }
    
    int get(int key) {
        auto &chain = bucket[hash(key)];
        for (auto &pair : chain) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        return -1;
    }
    
    void remove(int key) {
        auto &chain = bucket[hash(key)];
        for (auto itr = chain.begin(); itr != chain.end(); ++itr) {
            if (itr->first == key) {
                chain.erase(itr);
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