# Blockchain implementation
BLOCKCHAIN IMPLEMENTATION USING SHA-3 ALOGORITHM



Creating Blockchain using Python, mining new blocks, and displaying the whole blockchain:

The data will be stored in JSON format which is very easy to implement and easy to read. The data is stored in a block and the block contains multiple data. Each and every minute multiple blocks are added and to differentiate one from the other we will use fingerprinting.

The fingerprinting is done by using hash and to be particular we will use the SHA3-512 hashing algorithm. Every block will contain its own hash and also the hash of the previous function so that it cannot get tampered with.

This fingerprinting will be used to chain the blocks together. Every block will be attached to the previous block having its hash and to the next block by giving its hash.

The mining of the new block is done by giving successfully finding the answer to the proof of work. To make mining hard the proof of work must be hard enough to get exploited.

After mining the block successfully the block will then be added to the chain.

After mining several blocks the validity of the chain must be checked in order to prevent any kind of tampering with the blockchain.

Then the web interface will be made by using Fast api and deployed locally or publicly as per the need of the user.
