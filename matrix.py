import sys

class Matrix:

	def __init__(self, *arg):
		try:
			if len(arg)!=4:
				raise Exception("Bad number of arguments!")
		except:
			print("Unexpected error:", sys.exc_info()[1])
		self._rows=[[arg[i*2+j] for j in range(2)] for i in range(2)]

	def __str__(self):
		return str(self._rows)

	def add(self, other):
		try:
			if isinstance(other, Matrix):
				new_mat = [[self._rows[i][j]+other._rows[i][j] for j in range(2)] for i in range(2)]
				return new_mat
			else:
				raise Exception("Bad type of argument!")
		except:
			print("Unexpected error:", sys.exc_info()[1])

	def mul(self, other):
		try:
			if isinstance(other, Matrix):
				new_mat=[]
				for i in range(2):
					new_mat.append([])
					for j in range(2):
						new_mat[i].append(sum([self._rows[i][k]*other._rows[k][j] for k in range(2)]))
				return new_mat
			else:
				raise Exception("Bad type of argument!")
		except:
			print("Unexpected error:", sys.exc_info()[1])
		




