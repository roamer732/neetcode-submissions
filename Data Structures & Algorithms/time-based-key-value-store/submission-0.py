class Value:
    def __init__(self, data: str, timestamp: int):
        self.data = data
        self.timestamp = timestamp

NO_VALUE = ""

class TimeMap:
    def __init__(self):
        self._storage = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self._is_key_not_exist(key):
            self._create_new_entry_for_given_key(key)
        self._append_value_for_given_key(key, Value(value, timestamp))
    
    def _is_key_not_exist(self, key: str) -> bool:
        return self._storage.get(key) is None
    
    def _create_new_entry_for_given_key(self, key: str):
        self._storage[key] = list()

    def _append_value_for_given_key(self, key: str, value: Value):
        self._storage[key].append(value) 

    def get(self, key: str, timestamp: int) -> str:
        if self._is_key_not_exist(key):
            return NO_VALUE
        
        values = self._storage[key]
        length = len(values)
        left_index = 0
        right_index = length - 1

        if self._is_timestamp_exceed_lower_bound(key, timestamp):
            return NO_VALUE
        
        if self._is_timestamp_exceed_upper_bound(key, timestamp):
            return values[-1].data
        
        while left_index <= right_index:
            mid_index = self._get_mid_index(left_index, right_index)
            value = values[mid_index]
            if value.timestamp == timestamp:
                return value.data
            
            if timestamp > values[mid_index].timestamp and timestamp <= values[right_index].timestamp:
                left_index = mid_index + 1
            else:
                if timestamp < values[mid_index].timestamp and timestamp >= values[left_index].timestamp:
                    right_index = mid_index
                else:
                    return values[mid_index-1].data
        return NO_VALUE
    
    def _is_timestamp_exceed_lower_bound(self, key: str, timestamp: int) -> bool:
        return timestamp < self._storage[key][0].timestamp
    
    def _is_timestamp_exceed_upper_bound(self, key: str, timestamp: int) -> bool:
        return timestamp > self._storage[key][-1].timestamp
    
    def _get_mid_index(self, l: int, r: int) -> int:
        return l + (r - l)//2
