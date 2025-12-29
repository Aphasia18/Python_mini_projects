class HashTable:
    def __init__(self):
        #decleare empty dictionary to add key value pairs to
        self.collection = {}

    #return hash value of input text
    def hash(self,text):
        total = 0

        for char in text:
            total += ord(char)
        return total

    
    def add(self,key,val):
        key_hash = 0
        #get hash value of key
        for char in key:
            key_hash += ord(char)

        #if key hash is NOT exist create empty dictionary at that place
        #if it exists just add key value to hash positiom
        if key_hash not in self.collection:
            self.collection[key_hash] = {}

        #add key value at hashed key position              
        self.collection[key_hash][key] = val

    def remove(self,key):
        key_hash = 0
        #get hash value of key
        for char in key:
            key_hash += ord(char)
        
        #if hash value of key EXISTS DELETE it from a key hash position along with its  value
        if key_hash in self.collection:
            del self.collection[key_hash][key]


    def lookup(self,key):
        key_hash = 0
        #get hash value of key
        for char in key:
            key_hash += ord(char)
        #if hash value of key EXISTS RETURN it from a key hash position if not return NONE
        if key_hash in self.collection:
            return self.collection[key_hash][key]
        else:
            return None

Htable = HashTable()
Htable.add("dear","animal")
Htable.add("read","book")
Htable.add("melon","dingus")
Htable.remove("melon")
Htable.lookup("read")
Htable.add("lemon","yellow")
print(Htable.collection)