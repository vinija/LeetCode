class LFUCache:

  	def __init__(self, capacity: int):
  		# var reservation
  		self.capacity = capacity
  		# structure[frequency] => queue[key]
  		self.structure = collections.defaultdict(list)
  		# key :: val entry
  		self.lookup = {}

  	def get(self, key: int) -> int:
  		# if key not existed
  		if key not in self.lookup:
  			return -1
  		# fetch frequency with requested key
  		[frequency, var] = self.lookup[key]
  		self.lookup[key] = [frequency + 1, var]
  		self.structure[frequency].remove(key)
  		self.structure[frequency + 1].append(key)
  		return var

  	def put(self, key: int, val: int) -> None:
  		# if key exist
  		if key in self.lookup:
  			# fetch curr frequency
  			[frequency, var] = self.lookup[key]
  			# update frequency 
  			self.structure[frequency].remove(key)
  			self.structure[frequency + 1].append(key)
  			self.lookup[key] = [frequency + 1, val]
  		# if key not exist
  		else:
  			# handle empty capacity
  			if self.capacity == 0:
  				return
  			# check if capacity will exceed
  			if self.capacity == len(self.lookup):
  				# keep iteration till find valid frequency keys
  				frequent = 1
  				while not self.structure[frequent]:
  					frequent += 1
  				# pop the less recency key fro mthe least frequency
  				var = self.structure[frequent].pop(0)
  				# eliminate key :: val entry from lookup
  				self.lookup.pop(var)
  			# complete raw entry insertion
  			self.structure[1].append(key)
  			self.lookup[key] = [1, val]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)