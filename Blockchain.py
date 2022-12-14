#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import hashlib 
import json


# In[2]:


class Blockchain:
    def __init__(self)->None:
        self.chain=list()
        genesis_block=self.create_block(data="Genesis block",
                                        proof=1,
                                        previous_hash="0",
                                        index=1)
        self.chain.append(genesis_block)
        
        
        
    def mine_block(self, data:str)->dict:
        previous_block=self.get_previous_block()
        previous_proof=previous_block["proof"]
        index=len(self.chain)+1
        proof=self.proof_of_work(previous_proof, index, data)
        previous_hash=self._hash(block=previous_block)
        block=self.create_block(
            data=data, proof=proof, previous_hash=previous_hash, index=index
        )
        self.chain.append(block)
        return block
    
    
    def _hash(self, block:dict)->str:
        encoded_block=json.dumps(block, sort_keys=True).encode()
        return hashlib.sha3_512(encoded_block).hexdigest()
    
    
    def to_digest(self, new_proof:int, previous_proof:int, index:str, data:str)->bytes:
        to_digest=str(new_proof**2-previous_proof**2+index)+data
        return to_digest.encode()
    
    def proof_of_work(self, previous_proof:str,index:int,data:str)->int:
        new_proof=1
        check_proof=False
        
        while not check_proof:
            to_digest=self.to_digest(new_proof=new_proof,
                                    previous_proof=previous_proof,
                                    index=index,
                                    data=data,
                                    )
            
            hash_value=hashlib.sha3_512(to_digest).hexdigest()
            
            if hash_value[:4]=="0000":
                check_proof=True
            else:
                new_proof+=1
        return new_proof
    
    
    def get_previous_block(self)->dict:
        return self.chain[-1]
    
    def create_block(self, data: str, proof:int, previous_hash:str, index:int)->dict:
        block={
            "index":index,
            "timestamp":str(dt.datetime.now()),
            "data":data,
            "proof":proof,
            "previous_hash":previous_hash
        }
        
        return block
    
    def is_chain_valid(self)->bool:
        current_block=self.chain[0]
        block_index=1
        
        while block_index<len(self.chain):
            next_block=self.chain[block_index]
            
            if next_block["previous_hash"]!= self._hash(current_block):
                return False
            
            current_proof=current_block["proof"]
            next_index, next_data, next_proof=(
                next_block["index"],
                next_block["data"],
                next_block["proof"],
            )
            
            
            hash_value=hashlib.sha3_512(
                self.to_digest(new_proof=next_proof,
                previous_proof=current_proof,
                index=next_index,
                data=next_data,
                              )
            ).hexdigest()
            if hash_value[:4]!="0000":
                return False
            
            current_block=next_block
            block_index+=1
            
        return True


# In[3]:


bc=Blockchain()
bc.chain


# In[4]:


bc.mine_block("binod")


# In[5]:


bc.mine_block("blah blah blah")


# In[6]:


bc.is_chain_valid()


# In[7]:


bc.chain[1]["data"]="bucky..."


# In[9]:


bc.chain


# In[10]:


bc.is_chain_valid()


# In[11]:


bc.chain[1]["data"]="binod"


# In[12]:


bc.chain


# In[13]:


bc.is_chain_valid()


# In[ ]:




