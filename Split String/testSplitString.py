from splitString import TrieSet
import unittest

class testTrieSet(unittest.TestCase):

    def setUp(self):
        self.t = TrieSet()
        self.lexicon = "a, at, ate, boy, boys, chair, cherry, cream, ice, in, rain, sat, stood, stopped, the, topped, with".split(", ") 
    
    def testBasic(self):
        word = "big"
        self.t.insert(word)
        self.assertTrue(self.t.contains(word))

    def testInsertAll(self):
        self.t.insertAll(self.lexicon)
        for key in self.lexicon:
            self.assertTrue(self.t.contains(key))

    def testContains(self):
        word1 = "big"
        word2 = "small"
        self.t.insert(word1)
        self.assertTrue(self.t.contains(word1))
        self.assertFalse(self.t.contains(word2))

    def testContainsSimilarShorter(self):
        word1 = "dogs"
        word2 = "dog"
        self.t.insert(word1)
        self.assertTrue(self.t.contains(word1))
        self.assertFalse(self.t.contains(word2))

    def testContainsSimilarLonger(self):
        word1 = "dog"
        word2 = "dogs"
        self.t.insert(word1)
        self.assertTrue(self.t.contains(word1))
        self.assertFalse(self.t.contains(word2))

    def testSplitStringPositive(self):
        self.t.insertAll(self.lexicon)
        key = "theboyateicecream"
        target = "the boy ate ice cream"
        self.assertEqual(self.t.splitString(key), target)

    def testSplitStringNegative(self):
        self.t.insertAll(self.lexicon)
        key = "theboyatecheese"
        target = "the boy ate cheese"
        self.assertFalse(self.t.splitString(key) == target)
        self.t.insert("cheese")
        self.assertEqual(self.t.splitString(key), target)

    def testString(self):
        self.t.insert("big")
        target = "TrieSet:{value:False,children:['b':TrieSet:{value:False,children:['i':TrieSet:{value:False,children:['g':TrieSet:{value:True}]}]}]}"
        self.assertEqual(str(self.t), target)
        self.t.insert("pig")
        target = "TrieSet:{value:False,children:['b':TrieSet:{value:False,children:['i':TrieSet:{value:False,children:['g':TrieSet:{value:True}]}]},'p':TrieSet:{value:False,children:['i':TrieSet:{value:False,children:['g':TrieSet:{value:True}]}]}]}"
        self.assertEqual(str(self.t), target)
        self.t.insert("pit")
        target = "TrieSet:{value:False,children:['b':TrieSet:{value:False,children:['i':TrieSet:{value:False,children:['g':TrieSet:{value:True}]}]},'p':TrieSet:{value:False,children:['i':TrieSet:{value:False,children:['g':TrieSet:{value:True},'t':TrieSet:{value:True}]}]}]}"
        self.assertEqual(str(self.t), target)
