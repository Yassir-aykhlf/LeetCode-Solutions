class LRUCache {
private:
    int capacity;
    std::list<std::pair<int, int>> cachelist;
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cachemap;
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (cachemap.find(key) == cachemap.end()) {
            return -1;
        }
        cachelist.splice(cachelist.begin(), cachelist, cachemap[key]);
        cachemap[key] = cachelist.begin();
        return cachelist.begin()->second;
    }
    
    void put(int key, int value) {
        if (cachemap.find(key) != cachemap.end()) {
            cachelist.splice(cachelist.begin(), cachelist, cachemap[key]);
            cachemap[key] = cachelist.begin();
            cachelist.begin()->second = value;
            return;
        }
        if (cachelist.size() == capacity) {
            int del_key = cachelist.back().first;
            cachelist.pop_back();
            cachemap.erase(del_key);
        }
        cachelist.push_front(std::make_pair(key, value));
        cachemap[key] = cachelist.begin();
    }
};