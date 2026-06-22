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

        if self._is_timestamp_exceed_lower_bound(key, timestamp):
            return NO_VALUE
        
        if self._is_timestamp_exceed_upper_bound(key, timestamp):
            return self._get_most_recent_value_for_given_key(key)
        
        return self._get_data_using_binary_search_for_given_timestamp(key, timestamp)
    
    def _is_timestamp_exceed_lower_bound(self, key: str, timestamp: int) -> bool:
        return timestamp < self._storage[key][0].timestamp
    
    def _is_timestamp_exceed_upper_bound(self, key: str, timestamp: int) -> bool:
        return timestamp > self._storage[key][-1].timestamp
    
    def _get_most_recent_value_for_given_key(self, key) -> str:
        return self._storage[key][-1].data
    
    def _get_data_using_binary_search_for_given_timestamp(self, key: str, timestamp: int):
        values = self._storage[key]
        length = len(values)
        left_index = 0
        right_index = length - 1

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
                    # if given timestamp not exists in both the sub arrays (right and left),
                    # then return value that is most recent at given timestamp 
                    return values[mid_index-1].data
        return NO_VALUE
    
    def _get_mid_index(self, l: int, r: int) -> int:
        return l + (r - l)//2
