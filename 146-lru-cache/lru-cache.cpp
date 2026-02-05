class LRUCache {
private:
    size_t capacity;
    // DLL of KV pairs
    std::list<std::pair<int, int>> _list;
    // Hashmap of iterator to _list iterators/pointers 
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> _map;
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (_map.find(key) == _map.end()) {
            return -1;
        }
        _list.splice(_list.begin(), _list, _map[key]);
        _map[key] = _list.begin();
        return _list.begin()->second;
    }
    
    void put(int key, int value) {
        if (_map.find(key) != _map.end()) {
            _list.splice(_list.begin(), _list, _map[key]);
            _map[key] = _list.begin();
            _list.begin()->second = value;
            return;
        }
        if (capacity == _list.size()) {
            int del_key = _list.back().first;
            _list.pop_back();
            _map.erase(del_key);
        }
        _list.push_front(std::pair(key, value));
        _map[key] = _list.begin();
    }
};