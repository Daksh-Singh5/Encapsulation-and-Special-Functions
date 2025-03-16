class sentence:
    def __init__(self,word1,word2,word3,word4,word5):
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
        self.word4 = word4
        self.word5 = word5
    def printsentence(self):
        print(self.word5,self.word4,self.word3,self.word2,self.word1)

sentence1 = sentence("hello","how","are","you","doing")
sentence1.printsentence()