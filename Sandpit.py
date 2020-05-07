#Imprive upon the below function
import pandas as pd

def str_check(string, *args):
	"""
	This function counts the occurance of words in a strind.
	
	str_check(string, word, word, ...)
	"""
	
	#Create an empty list
	lst = []
	
	#Convert into lower case
	string = string.lower()
	
	#Place each word into a list
	s_lst = string.split()
	
	
	#Loop through each given word
	for x in args:
		
	
		#Set counter to 0
		cnt = 0
		
		#Loop through wach word in string
		for y in s_lst:
			
			#Convert word to lower case
			y = y.lower()
			
			#Test if the words match
			if x == y:
			
				#if true + 1 to counter
				cnt += 1
				
		#Append resulrs to a list
		lst.append([x, cnt])
		
	#Import panndas without prefix
	import pandas
	
	#Convert the list into a DataFrame
	lst = pandas.DataFrame(lst)
	
	#Set  column names
	lst.columns = ["word", "count"]
	
	#Return the list as the output
	return lst
	
string = "Archaic Greece was the period in Greek history lasting from the eighth century BC to the second Persian invasion of Greece in 480 BC,[1] following the Greek Dark Ages and succeeded by the Classical period. In the archaic period, Greeks settled across the Mediterranean and the Black Seas, as far as Marseille in the west and Trapezus (Trebizond) in the east; and by the end of the archaic period, they were part of a trade network that spanned the entire Mediterranean."


		

print(str_check(string,"the","and", "of"))
