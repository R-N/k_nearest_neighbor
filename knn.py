from math import sqrt
class Data:
	def __init__(self, identifier, attributes, cluster):	
		self.identifier = identifier
		self.attributes = attributes
		self.attr_count = len(self.attributes)
		self.cluster = cluster
	
	def euclid_dist_sq(self, input):
		count = len(input)
		assert count == self.attr_count
		
		total = sum(
			[
				(self.attributes[i]-input[i])*(self.attributes[i]-input[i]) 
				for i in range(0, count)
			]
		)
			
		return total
	
	def euclid_dist(self, input):
		return sqrt(self.euclid_dist_sq(input))
		
		
dataset = [
	Data(4, [8, 10, 1, 8], 1),
	Data(5, [0, 5, 10, 8], 1),
	Data(8, [0, 0, 0, 10], 0),
	Data(7, [9, 2, 2, 9], 1),
	Data(8, [2, 2, 8, 9], 0),
	Data(9, [7, 2, 2, 1], 0),
	Data(10, [2, 3, 1, 2], 0)
]

clusters = {0,1}
cluster_str = ["Ditolak", "Diterima"]

def knn(k, input):
	ranked = sorted(dataset, key=lambda data: data.euclid_dist(input))[:k]
	result = min(
		clusters, 
		key=lambda cluster: len([data for data in ranked if data.cluster==cluster])
	)
	
	return result
	

def main():
	print("K Nearest Neighbor")
	print()
	k = input("Masukkan nilai k: ")
	k = int(k)
	
	harta = input("Masukkan nilai harta: ")
	harta = int(harta)
	
	keturunan = input("Masukkan nilai keturunan: ")
	keturunan = int(keturunan)
	
	wajah = input("Masukkan nilai wajah: ")
	wajah = int(wajah)
	
	agama = input("Masukkan nilai agama: ")
	agama = int(agama)
	
	#print("Hasil: " + cluster_str[knn(3, [5, 5, 8, 2])])
	print("Hasil: " + cluster_str[knn(k, [harta, keturunan, wajah, agama])])
	

if __name__== "__main__":
	main()
