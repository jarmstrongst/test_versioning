class MathMachine():
	
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def do_math_magic(self):
		return self.x * self.y / self.z 


if __name__ == '__main__':
	print('hello world!')
	machine_1 = MathMachine(1,2,3)
	print(machine_1.do_math_magic())
