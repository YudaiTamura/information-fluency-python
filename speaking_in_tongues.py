def make_google_english_dictionary(input_file_name, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name)
	output_data = output_file.readlines()
	output_file.close()
	
	T = int(input_data.pop(0))
	
	google_english_dictionary = {}
	for t in range(T):
		google_string = input_data.pop(0).rstrip()
		english_string = output_data.pop(0).split(':')[1]
		english_string = english_string.strip()
		for i in range(len(google_string)):
			google_english_dictionary[google_string[i]] = english_string[i]
	return google_english_dictionary
	
	
def answer(input_file_name, google_english_dictionary, output_file_name):
	input_file = open(input_file_name)
	input_data = input_file.readlines()
	input_file.close()
	
	output_file = open(output_file_name, 'w')
	T = int(input_data.pop(0))
	
	for t in range(T):
		google_string = input_data.pop(0).rstrip()
		english_string = ''
		for g in google_string:
			english_string += google_english_dictionary[g]
		output_file.write('Case #{0}: {1}\n'.format(t + 1, english_string))
	
	output_file.close()
	return
