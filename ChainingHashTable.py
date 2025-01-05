# Chaining hash table to hold movie data
class ChainingHashTable:
    # constructor creates empty hash table size initial capacity, uses
    # loop to add empty list into each bucket
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    # inserts and updates new key-item pair into the table
    def insert(self, key, value):
        # get bucket list where this item will go
        bucket_index = hash(key) % len(self.table) # finds bucket index
        bucket_list = self.table[bucket_index] # list item will go in

        # update key if its already in the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        # otherwise insert key_value pair into list
        key_value = (key, value)
        bucket_list.append(key_value)
        return True


    # Searches for item with matching key in hash table
    def search(self, key):
        # get bucket list where item will go
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # search for the key in the bucket_list
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None


    # Removes an item with matching key from hash table
    def remove(self, key):
        # get bucket list where item will go
        bucket_index = hash(key) % len(self.table)
        bucket_list = self.table[bucket_index]

        # remove item if present
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
                return True
        return None






