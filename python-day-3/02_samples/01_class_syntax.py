
class ClassName:

	def __init__(self, prop):
		self.prop = prop

	def method(self):
		pass

	def method_with_input(self, input1, input2):
		pass

value = 1
object = ClassName(prop=value)
print(object.prop)