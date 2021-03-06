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
		
		
	def coy_email(self, pre=""):
		if not pre == "":
			pre = str(pre)
		
		fn = self.f_name.lower()
		ln = self.l_name.lower()
		return fn + "." + ln \
				+ pre + "@allform.tech"
	
   
	
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

print("")

print(me.coy_email(1))


class Statistics:
	
	def __init__(self, lst):
		def Mean(lst):
			cntS = 0
			cntC = 0
			for x in lst:
				cntS += x
				cntC += 1
			return cntS/cntC
		self.mean = Mean(lst)



lst = [1,2,7,3,6]
        
myLst = Statistics(lst)
print(myLst.mean)

