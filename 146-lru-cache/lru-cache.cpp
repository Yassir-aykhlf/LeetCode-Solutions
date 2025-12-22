class LRUCache {
private:
    const int capacity;
    std::list<std::pair<int, int>> cacheList;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cacheMap;
    int hash(int key) {
        return key % capacity;
    }
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            cacheMap[key] = cacheList.begin();
            return cacheList.begin()->second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            cacheMap[key] = cacheList.begin();
            cacheList.begin()->second = value;
            return;
        }
        if (cacheList.size() == capacity) {
            int del_key = cacheList.back().first;
            cacheList.pop_back();
            cacheMap.erase(del_key);
        }
        cacheList.push_front({key, value});
        cacheMap[key] = cacheList.begin();
    }
};