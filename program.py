class MathMachine():
	
	def do_other_math_magic(self, x, y):
		return x ** y

	def do_math_magic(self, x, y, z):
		return x * y / z 


if __name__ == '__main__':
	print('hello world!')
	# not backwards compatible, breaks with new changes
	#machine_1 = MathMachine(1,2,3)
	#print(machine_1.do_math_magic())
	#print(machine_1.do_other_math_magic())
	machine_2 = MathMachine()
	print(machine_2.do_math_magic(5,6,7))
	print(machine_2.do_other_math_maginc(8,9))
