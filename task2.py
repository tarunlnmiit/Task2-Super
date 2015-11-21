from random import shuffle

punc_list = [".",",",";",":","!","'",'"',"-"]

# Input string/strings
print '***************Enter data**************** '
s = ""
while True:
	temp = raw_input() + "\n"
	if temp == "\n":
		break
	s += temp

# Opening a file to write the input sentence/sentences or paragraphs

fhand = open("inputData.txt", 'w')
fhand.write(s)
fhand.close()

# Reading the input data line by line 
fhand = open("inputData.txt", 'r')

# Writing the data after scrambling
fhand1 = open('data.txt', 'w')

# Function to perform scrambling
for line in fhand:
	s = line.rstrip().split()
	
	for i in xrange(len(s)):
		
		# Code for words with no punctuation 
		if s[i].isalpha():
			scramble_text = list(s[i][1:len(s[i])-1])
			shuffle(scramble_text)
			scramble_text = "".join(scramble_text)
			
			if len(s[i]) > 1:
				s[i] = s[i][0] + scramble_text + s[i][-1]
			
			else:
	 			s[i] = s[i][0] + scramble_text
	 	
	 	else:
	 		# For words which have same punctuation at start and end
	 		if s[i][0] == s[i][-1] and s[i][0] in punc_list and s[i][-1] in punc_list:
	 			scramble_text = list(s[i][2:len(s[i])-2])
		 		shuffle(scramble_text)
		 		scramble_text = "".join(scramble_text)
		 		s[i] = s[i][:2] + scramble_text	+ s[i][-2:]
		 	
	 		else:
		 			for item in punc_list:
		 		
			 			if item in s[i]:
			 				s1, s2 = s[i].split(item)
			 		
			 				if len(s2) == 0:
			 					scramble_text = list(s1[1:len(s1)-1])
			 					shuffle(scramble_text)
			 					scramble_text = "".join(scramble_text)
			 		
			 					if len(s1) > 1:
			 						s1 = s1[0] + scramble_text + s1[-1]
			 		
			 					else:
			 						s1 = s1[0] + scramble_text
			 					s[i] = s1 + item + s2
			 		
			 				else:
			 					scramble_text = list(s1[1:len(s1)])
			 					shuffle(scramble_text)
			 					scramble_text = "".join(scramble_text)
			 					s1 = s1[0] + scramble_text
			 					scramble_text = list(s2[:-1])
			 					shuffle(scramble_text)
			 					scramble_text = "".join(scramble_text)
			 					s2 = scramble_text + s2[-1]
			 					s[i] = s1 + item + s2
	
	s = " ".join(s)
	fhand1.write(s+  '\n')

fhand1.close()
fhand.close()

fhand = open('data.txt', 'r')

for line in fhand:
	print line.rstrip()

fhand.close()