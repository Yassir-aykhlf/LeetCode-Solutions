class MyHashMap {
private:
    size_t capacity = 997;
    std::vector<std::list<std::pair<int, int>>> _hashma;
    int hash(int key) {
        return key % capacity;
    }
public:
    MyHashMap() {
        _hashma.resize(capacity);
    }
    
    void put(int key, int value) {
        auto &chain = _hashma[hash(key)];
        for (auto &el : chain) {
            if (el.first == key) {
                el.second = value;
                return;
            }
        }
        chain.push_back(std::pair(key, value));
    }
    
    int get(int key) {
        auto &chain = _hashma[hash(key)];
        for (auto &el : chain) {
            if (el.first == key) {
                return el.second;
            }
        }
        return -1;
    }
    
    void remove(int key) {
        auto &chain = _hashma[hash(key)];
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