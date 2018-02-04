import hashlib
import Block

class BlockChain: 
    chain = []

    def __init__(self):
        #creating a genisis block when initing the BlockChain most of the time its hard coded that the reason
        #we provide a prev hash
        self.chain = [Block.Block("0", "04/02/2018", "0")]
    
    def addingBlock(self, block): 
        block.prevHash = self.chain[-1].hashBlock()
        #print("The previous hash: " + block.prevHash)
        block.hash = block.hashBlock()
        #print("The current hash:  " + block.hash)
        self.chain.append(block)
    
    def displayBlockChain(self):
        for block in self.chain:
            print("Time: " + block.getTimeStamp())
            print("The Previous Hash: " + block.getPreviousHash())
            print("The Current Hash: " + block.hashBlock())
            print("The Amount Trans: " + block.getTransaction())
            print("********")