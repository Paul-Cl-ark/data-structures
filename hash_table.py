class HashTable:
  def __init__(self, size = 53):
    self.key_map = [[] for i in range(size)]


  def _hash(self, key):
    total = 0
    PRIME = 31
    for i in range(0, min(len(key), 100)):
      char = key[i]
      value = ord(char) - 96
      total = (total * PRIME + value) % len(self.key_map)
    
    return total

  
  def set(self, key, value):
    index = self._hash(key)
    exists = next((item for item in self.key_map[index] if item[0] == key), None)
    
    if exists: exists[1] = value
    else: self.key_map[index].append([key, value])


  def get(self, key):
    index = self._hash(key)

    result = next((item for item in self.key_map[index] if item[0] == key), None)
    return result[1] if result else result


  def keys(self):
    return [item[0] for index in self.key_map for item in index]


  def values(self):
    return list({item[1] for index in self.key_map for item in index})


hash_table = HashTable()
print(hash_table.key_map)
print(hash_table.set('rabbit', 'abcde'))
print(hash_table.set('melon', 'hello'))
print(hash_table.set('penis', 'monkey'))
print(hash_table.set('penis', 'wenis'))
print(hash_table.set('okay', 'wenis'))
print(hash_table.key_map)
print(hash_table.get('poo'))
print(hash_table.keys())
print(hash_table.values())
