class myClass:
	
	def __init__(self, name, age=0):
		self.name = name
		self.age = age
		self.name_list = name.split()
		self.f_name = self.name_list[0]
		
		self.l_name = sorted(
			self.name_list,
			reverse=True)[0]
	
	def __repr__(self):
		return "myClass('{}', '{}',{})".format(self.f_name, self.l_name, self.age)
    
	def __str__(self):
		return "myClass('{}','{}')".format(self.f_name, self.l_name)
   
	
me = myClass("Kristopher Takken", 36)

print(me)
print(me.__repr__())
print(me.__str__())

print("")
print("__dict__")
print(me.__dict__)

print("")

print(me.f_name)
print(me.l_name)
print(me.age)
print(me.name_list)
