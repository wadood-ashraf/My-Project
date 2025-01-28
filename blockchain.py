import hashlib  # Importing hashlib library to create hashes.

# Function to create a hash from given data
def hashGenerator(data):
    result = hashlib.sha256(data.encode())  # Convert data to SHA-256 hash
    return result.hexdigest()  # Return the hash in hexadecimal format

# Class to define what a block is
class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data  # Data in the block (e.g., some transactions)
        self.hash = hash  # Current block's unique hash
        self.prev_hash = prev_hash  # Hash of the previous block

# Class to represent the whole blockchain
class Blockchain:
    def __init__(self):
        # Creating the first block (genesis block)
        hashLast = hashGenerator('gen_last')  # Hash for the "previous" block (arbitrary for genesis)
        hashStart = hashGenerator('gen_hash')  # Hash for the genesis block itself

        # Creating the genesis block with some default data
        genesis = Block('gen-data', hashStart, hashLast)
        self.chain = [genesis]  # Initialize blockchain with the genesis block

    # Function to add a new block to the chain
    def add_block(self, data):
        prev_hash = self.chain[-1].hash  # Get the hash of the last block in the chain
        hash = hashGenerator(data + prev_hash)  # Create a new hash using data + last block's hash
        block = Block(data, hash, prev_hash)  # Create a new block
        self.chain.append(block)  # Add the new block to the chain

# Creating a blockchain object
bc = Blockchain()

# Adding some blocks to the blockchain
bc.add_block('1')  # Adding block with data '1'
bc.add_block('2')  # Adding block with data '2'
bc.add_block('3')  # Adding block with data '3'

# Printing the blocks in the blockchain
for block in bc.chain:
    print(block.__dict__)  # Display the block details as a dictionary
