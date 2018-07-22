import hashlib as hasher
import datetime as date

#learn this from snakecoin

class Block:
	def __init__(self,index,timestamp,data,previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.block_hasher()
	def block_hasher(self):
		sha = hasher.sha256()
		sha.update(str(self.index).encode('utf-8')+str(self.timestamp).encode('utf-8')+str(self.previous_hash).encode('utf-8'))
		return sha.hexdigest()

def genesis_block():
	return Block(0,date.datetime.now(),"genesis Block","0")

blockchain = [genesis_block()]
previous_block = blockchain[0]


def create_block(previous_block,data):
	index = previous_block.index+1
	timestamp = date.datetime.now()
	data = str(data)
	previous_has = previous_block.hash

	return Block(index,timestamp,data,previous_has)

def get_data(b):
	data_collect = []
	for i in b:
		data_collect.append([i.index,i.timestamp,i.data,i.hash,i.previous_hash])
	return data_collect


