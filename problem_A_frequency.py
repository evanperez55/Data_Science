#Open file and assign count variables
with open('datafile.din.txt', 'r') as f:
	line_count_0 = 0
	line_count_1 = 0
	line_count_2 = 0

	#Loop through each line of file
	for line in f:
		#Loop through each character of line and count for either 0,1,2
		for char in line[2:]:
			if str(char) == '0':
				line_count_0 += 1
			elif str(char) == '1':
				line_count_1 += 1
			elif str(char) == '2':
				line_count_2 +=1
		

	#Establish variables for frequency equation	
	reads = line_count_0
	writes = line_count_1	
	total = line_count_0 + line_count_1 + line_count_2
	
	#Calculate frequency
	freq_reads = reads / total
	freq_writes = writes / total
