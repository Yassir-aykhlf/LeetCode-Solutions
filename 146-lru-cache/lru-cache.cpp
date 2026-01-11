class LRUCache {
private:
    const unsigned int capacity;
    std::list<std::pair<int, int>> cacheList;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cacheMap;
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (cacheMap.find(key) == cacheMap.end()) {
            return -1;
        }
        cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        cacheMap[key] = cacheList.begin();
        return cacheMap[key]->second;
    }
    
    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            cacheMap[key] = cacheList.begin();
            cacheMap[key]->second = value;
            return;
        }
        if (capacity == cacheList.size()) {
            int last = cacheList.back().first;
            cacheList.pop_back();
            cacheMap.erase(last);
        }
        cacheList.push_front({key, value});
        cacheMap[key] = cacheList.begin();
    }
};