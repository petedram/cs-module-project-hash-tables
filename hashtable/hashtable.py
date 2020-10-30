class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        # self.prev = None? Don't need to add LL class

    
    # def __str__(self):
    #     return f'{self.value}'




# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = max(capacity, MIN_CAPACITY)
        self.data = [None] * capacity

        #array full of linked lists




    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        #if < 0.7, 
        #make new array, double the size of old one
        #iterate down the old array
        #traverse down the linked list
        #rehash and 'put' in new array

        #check and trigger resize in 'put'
        #if override, don't resize, if new then resize.
        


        

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        ...prime numbers are like the atoms of other numbers. good for multiplying stuff.

        0101010101010101
        1101101101010101
        ________________
        1000111000000000

        XOR will look at each pair of bits, if one only true will return 1 - building new number.

        hashing functions are used in:
        -git
        -crypto currentcy
        -password storage
        -hash tables

        some are fast, some are are slow, some more security, some less, etc.



        """

        # Your code here
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hashed = FNV_offset_basis

        bytes_to_hash = key.encode()

        for byte in bytes_to_hash:
            hashed = hashed * FNV_prime

            hashed = hashed ^ byte

        return hashed
        
    

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.


        bit wise operation - left bit shifting. bump it.
        make it bigger by shifting it to the left.


    01010111001101000000
        
        why 5381 and * 33 because they work!
        what's work?
            - irreversable
            - nice distribution (to minimize collisions)


        """
        # Your code here
        hash = 5381

        byte_array = key.encode('utf-8')
        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        #check for collision
        if self.data != None:
            print('warning! collision')

        #Linear probing: keep going until find open slot.
        #hash key, check if it is the key, if not iterate, then change value when found, if not found, add new node.



        #turn the string into an index
        idx = self.hash_index(key)
        print(f'the index of {key} is {idx}')

        #put the string at that index in our array
        self.data[idx] = HashTableEntry(idx, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        #you delete item in LL by routing around it
        #update the previous object from node.prev to have a next of node.next from deleted node.
        #see example.

        #find value
        idx = self.hash_index(key)

        # set to none
        self.data[idx].value = None

        #or self.put(key, None)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        #Store the key unhashed and compare key and see if it matches as we iterate through the list

        #turn num into index
        idx = self.hash_index(key)

        #go and access element at that index
        item = self.data[idx]
        #return the value
        return item.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")

# ht = HashTable(0x10000)
# print(ht.capacity)
# ht.put("key-0", "val-0")
# ht.put("key-1", "val-1")
# ht.put("key-2", "val-2")

# return_value = ht.get("key-0")
# print(return_value)

# # self.assertTrue(return_value == "val-0")
# return_value = ht.get("key-1")
# print(return_value)

# # self.assertTrue(return_value == "val-1")
# return_value = ht.get("key-2")
# print(return_value)

# # self.assertTrue(return_value == "val-2")



