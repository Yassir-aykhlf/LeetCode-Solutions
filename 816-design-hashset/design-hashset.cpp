class MyHashSet {
private:
    int capacity = 997;
    std::vector<std::list<int>> bucket;
    int hash(int key) {
        return key % capacity;
    }
public:
    MyHashSet() {
        bucket.resize(capacity);
    }
    
    void add(int key) {
        auto &chain = bucket[hash(key)];
        for (auto &el : chain) {
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
        return; 
    }
    
    bool contains(int key) {
        auto &chain = bucket[hash(key)];
        for (auto &el : chain) {
            if (el == key) {
                return true;
            }
        }
        return false;
    }
};