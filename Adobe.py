import sys
from collections import OrderedDict

class FileCacheManager:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def accessFile(self, fileID: int, data: str) -> None:
        if fileID in self.cache:
            self.cache.move_to_end(fileID)
            self.cache[fileID] = data
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # Evict least recently used (first item)
            self.cache[fileID] = data

    def getFile(self, fileID: int) -> str:
        if fileID not in self.cache:
            return "File Not Found"
        self.cache.move_to_end(fileID)  # Mark as recently used
        return self.cache[fileID]


def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    cache_manager = None

    for line in input_data:
        line = line.strip()
        if not line:
            continue

        parts = line.split(maxsplit=2)
        cmd = parts[0]

        if cmd == "FileCacheManager":
            capacity = int(parts[1])
            cache_manager = FileCacheManager(capacity)
        elif cmd == "accessFile":
            file_id = int(parts[1])
            data = parts[2] if len(parts) > 2 else ""
            cache_manager.accessFile(file_id, data)
        elif cmd == "getFile":
            file_id = int(parts[1])
            print(cache_manager.getFile(file_id))

if __name__ == "__main__":
    main()