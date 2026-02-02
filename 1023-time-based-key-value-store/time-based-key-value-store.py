class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {'times': [], 'values': []}
        self.store[key]['times'].append(timestamp)
        self.store[key]['values'].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        times = self.store[key]['times']
        values = self.store[key]['values']
        idx = bisect.bisect_right(times, timestamp)
        if idx == 0:
            return ''
        return values[idx - 1]