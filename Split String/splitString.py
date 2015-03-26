"""
Input: "theboyateicecream"
Output: "the boy ate ice cream"

Given a lexicon like:
a, at, ate, boy, boys, chair, cherry, cream, ice, in, 
rain, sat, stood, stopped, the, topped, with

"""

from collections import defaultdict

class TrieSet(object):
    """
    Trie structure where the keys are stored in a per-character tree structure
    and each node is True iff that node represents a key in the structure.
    """
    
    def __init__(self):
        self.children = defaultdict(TrieSet)
        self.value = False

    def __str__(self):
        value = {
            "name":self.__class__.__name__,
            "value":"value:{}".format(self.value),
            "children":",children:[{}]".format(",".join("{}:{}".format(repr(key), self.children[key])
                                               for key in sorted(self.children))) if len(self.children) else "",
        }
        return "%(name)s:{%(value)s%(children)s}" % value
        
    def insert(self, key):
        """
        key: "abc"
        Key is in the trie if value == true, else not in the trie
        """
        node = self
        for char in key:
            node = node.children[char]
        node.value = True

    def insertAll(self, iterable):
        for key in iterable:
            self.insert(key)
    
    def contains(self, key):
        """
        Checks to see if key is contained in Trie
        """
        node = self
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.value

    def splitString(self, value):
        """
        Given a string like "theboyateicecream"
        return a segmented string into "the boy ate ice cream"
    
        This iterates through the string checking it against the dictionary (using Trie.contains())
        and adding each legitimate word to a list
        """
    
        result = []
	i = 0 # use counter to enable skipping ahead
        while i < len(value):
            node = self
            char1 = value[i]
            if char1 in node.children:
                node = node.children[char1]
                # Inner loop
                for j, char2 in enumerate(value[i+1:]):
                    if char2 in node.children:# or j < len(value[i+1:]):
                        node = node.children[char2]
                    else: # Get the longest possible value
                        if node.value:
                            result.append(value[i:i+j+1])
                            i = i+j # skip ahead!
                        break
                    j += 1
                    # End case
                    if j == len(value[i+1:]):
                        if node.value:
                            result.append(value[i:i+j+1])
            # If j at the end, break
            if j == len(value[i+1:]):
                break
            i += 1
        return " ".join(result)
