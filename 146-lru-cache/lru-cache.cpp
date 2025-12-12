class LRUCache {
    int capacity;
    std::list<std::pair<int, int>> cacheList;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cacheMap;
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (cacheMap.find(key) == cacheMap.end()) {
            return -1;
        }
        cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        return cacheMap[key]->second;
    }
    
    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheMap[key]->second = value;
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            return;
        }
        if (cacheList.size() == capacity) {
            int del = cacheList.back().first;
            cacheList.pop_back();
            cacheMap.erase(del);
        }
        cacheList.push_front({key, value});
        cacheMap[key] = cacheList.begin();
    }
};