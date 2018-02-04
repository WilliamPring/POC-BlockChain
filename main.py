import Blockchain
import Block

def main():
    transaction = [10, 20, 40, 50]
    cryptoTulips = Blockchain.BlockChain()
    cryptoTulips.addingBlock(Block.Block(transaction[0]))
    cryptoTulips.addingBlock(Block.Block(transaction[1]))
    cryptoTulips.addingBlock(Block.Block(transaction[2]))
    cryptoTulips.addingBlock(Block.Block(transaction[3]))
    cryptoTulips.displayBlockChain()
    print(cryptoTulips.validateBlockChain())
    cryptoTulips.chain[1].transactions = 20
    print(cryptoTulips.validateBlockChain())

if __name__== "__main__":
    main()