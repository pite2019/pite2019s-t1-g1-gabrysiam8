import sys

class Matrix:

	def __init__(self, *arg):
		try:
			if len(arg)!=4:
				raise Exception("Bad number of arguments")
		except:
			print("Unexpected error:", sys.exc_info()[0])
		self._rows=[]
		for i in range(2):
			self._rows.append([])
			for j in range(2):
				self._rows[i].append(arg[i*2+j])

	def __str__(self):
		return str(self._rows)

	def add(self, other):
		if isinstance(other, Matrix):
			new_mat = [[self._rows[i][j]+other._rows[i][j] for j in range(2)] for i in range(2)]
			return new_mat
		return None

	def mul(self, other):
		if isinstance(other, Matrix):
			new_mat=[]
			for i in range(2):
				new_mat.append([])
				for j in range(2):
					new_mat[i].append(sum([self._rows[i][k]*other._rows[k][i] for k in range(2)]))
			return new_mat
		return None




