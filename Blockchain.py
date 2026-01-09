import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Proof of Work Algorithm:
        Find a number p' such that hash(pp') contains leading 4 zeroes
        """
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while not self.valid_proof(last_proof, proof, last_hash):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof
        """
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


blockchain = Blockchain()

# Add transactions
blockchain.new_transaction("Alice", "Bob", 10)
blockchain.new_transaction("Bob", "Charlie", 5)

# Mine a new block
proof = blockchain.proof_of_work(blockchain.last_block)
blockchain.new_block(proof)

blockchain.new_transaction("Charlie", "Dave", 2)
proof = blockchain.proof_of_work(blockchain.last_block)
blockchain.new_block(proof)

# Print the blockchain
for block in blockchain.chain:
    print("Block:", block['index'])
    print("Timestamp:", block['timestamp'])
    print("Transactions:", block['transactions'])
    print("Proof:", block['proof'])
    print("Previous Hash:", block['previous_hash'])
    print("Hash:", blockchain.hash(block))
    print("-" * 50)
