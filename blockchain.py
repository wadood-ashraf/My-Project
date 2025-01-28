import hashlib  # To generate hashes for blocks

# Function to create a hash for any given data
def hashGenerator(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Block class to define each block's structure
class Block:
    def __init__(self, data, hash, prev_hash, nonce=0):
        self.data = data  # Block's data (can be transaction info or any data)
        self.hash = hash  # The hash of this block
        self.prev_hash = prev_hash  # The hash of the previous block
        self.nonce = nonce  # Nonce for the Proof-of-Work

# Blockchain class to handle the entire chain
class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty  # How hard the Proof-of-Work is (leading zeros in hash)
        # Genesis block (first block in the blockchain)
        genesis_hash = hashGenerator("genesis_block_data")
        genesis_prev_hash = "0" * 64  # No previous hash for the first block
        self.chain = [Block("Genesis Block", genesis_hash, genesis_prev_hash)]
    
    # Adding a new block to the blockchain
    def add_block(self, data):
        prev_block = self.chain[-1]
        prev_hash = prev_block.hash
        nonce, block_hash = self.proof_of_work(data, prev_hash)  # PoW to mine the block
        new_block = Block(data, block_hash, prev_hash, nonce)
        self.chain.append(new_block)

    # Proof-of-Work (mining a block)
    def proof_of_work(self, data, prev_hash):
        nonce = 0
        target = '0' * self.difficulty  # Target hash has 'difficulty' number of leading zeros
        while True:
            block_data = data + prev_hash + str(nonce)
            hash_result = hashGenerator(block_data)
            if hash_result[:self.difficulty] == target:
                return nonce, hash_result  # Found a valid nonce and hash
            nonce += 1

    # Validate the blockchain's integrity
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]
            # Check if the previous hash matches
            if current_block.prev_hash != prev_block.hash:
                return False
            # Recalculate the hash and check if it matches
            recalculated_hash = hashGenerator(current_block.data + current_block.prev_hash + str(current_block.nonce))
            if current_block.hash != recalculated_hash:
                return False
        return True

    # Printing the details of the blockchain
    def print_chain(self):
        for index, block in enumerate(self.chain):
            print(f"Block {index}:")
            print(f"  Data: {block.data}")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.prev_hash}")
            print(f"  Nonce: {block.nonce}")
            print("-" * 50)

# Create a blockchain with difficulty level 4 (require 4 leading zeros in the hash)
bc = Blockchain(difficulty=4)

# Adding some blocks with simple data
print("Mining block 1...")
bc.add_block("Block 1 data")
print("Mining block 2...")
bc.add_block("Block 2 data")
print("Mining block 3...")
bc.add_block("Block 3 data")

# Print the blockchain
print("\nBlockchain Details:")
bc.print_chain()

# Validate the blockchain
print("\nIs blockchain valid?", bc.validate_chain())  # Should return True

# Tampering with the blockchain (to simulate an attack)
print("\nTampering with the blockchain...")
bc.chain[1].data = "Tampered data"  # Modify the data of the second block

# Print the blockchain again after tampering
print("\nBlockchain Details After Tampering:")
bc.print_chain()

# Validate the blockchain after tampering
print("\nIs blockchain valid after tampering?", bc.validate_chain())  # Should return False

