class MyHashMap {
private:
    int capacity = 997;
    std::vector<std::list<std::pair<int,int>>> bucket;
    int hash(int key) {
        return key % capacity;
    }
public:
    MyHashMap() {
        bucket.resize(capacity);
    }
    
    void put(int key, int value) {
        auto &chain = bucket[hash(key)];
        for (auto &p : chain) {
            if (p.first == key) {
                p.second = value;
                return;
            }
        }
        chain.push_back({key, value});
    }
    
    int get(int key) {
        auto &chain = bucket[hash(key)];
        for (auto &p : chain) {
            if (p.first == key) {
                return p.second;
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