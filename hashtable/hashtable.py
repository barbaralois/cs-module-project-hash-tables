class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.total = 0
        self.buckets = [LinkedList()] * self.capacity
        

    def __repr__(self):
        return self.table


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.total/len(self.buckets)


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for s in key:
            hash = ((hash << 5) + hash) + ord(s)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Day One
        # index = self.hash_index(key)
        # self.buckets[index] = value

        # hash the key to get its index
        index = self.hash_index(key)
        # if there is no values in the list, add it
        if self.buckets[index].head is None:
            self.buckets[index].head = HashTableEntry(key, value)
            self.total += 1
        # if there is, start at the head and check to see if it matches any
        else:
            current = self.buckets[index].head
            while current.next:
                # if it does match, update the value
                if current.key == key:
                    current.value = value
                current = current.next
            
            # if it doesn't match any, add it to the LL
            current.next = HashTableEntry(key, value)
            self.total += 1



    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Day One
        # index = self.hash_index(key)
        # self.buckets[index] = None

        # hash the key to get its index
        # set the head to a variable for ease of reference
        index = self.hash_index(key)
        current = self.buckets[index].head        
        # start at the beginning of the LL and move through
        # if the first one matches, set previous next as new head
        # reduce size of LL by one
        if current.key == key:
            self.buckets[index].head = self.buckets[index].head.next
            self.total -= 1
            return        
        # if it's not the first one, continue moving through
        while current.next:
            previous = current
            current = current.next
            # when you find the key, set previous next as new head
            # reduce size of LL by one
            if current.key == key:
                previous.next = current.next
                self.total -= 1
                return None
        


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Day One
        # index = self.hash_index(key)
        # return self.table[index]

        # hash the key to get its index
        # set the head to a variable for ease of reference
        index = self.hash_index(key)
        current = self.buckets[index].head        
        # start at the beginning of the LL and move through
        # if the LL is empty, return, if the key matches, return the value
        if current == None:
            return
        if current.key == key:
            return current.value
        
        # if it's not the first one, continue moving through
        while current.next:
            current = current.next
            if current.key == key:
                return current.value
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Add a new linked list for each slot in the new table
        self.capacity = new_capacity
        new_list = [LinkedList()] * new_capacity

        # for every row in the table, start at the first item
        for i in self.buckets:
            current = i.head

            # rehash them to their new locations? All the way thru the LL
            while current is not None:
                index = self.hash_index(current.key)

                # add the items to their new spots in the table
                if new_list[index].head == None:
                    new_list[index].head = HashTableEntry(current.key, current.value)
                else:
                    new_entry = HashTableEntry(current.key, current.value)
                    new_entry.next = new_list[index].head
                    new_list[index].head = new_entry
                current = current.next
        # set the buckets/table to this new list that has everything sorted
        self.buckets = new_list



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")