import Blockchain
import Block

def main():
    transaction = [10, 20, 40, 50]
    cryptoTulips = Blockchain.BlockChain()
    cryptoTulips.addingBlock(Block.Block(transaction[0], "05/02/2018"))
    cryptoTulips.displayBlockChain()

if __name__== "__main__":
    main()