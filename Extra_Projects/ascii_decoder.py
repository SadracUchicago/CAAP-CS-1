### ---ASCII Decoder---###
###By Jesus A. A.###

def ascii_dc():
	message = []
	m_lenght = input('Please input the length of your message: \n>>') #Not the most efficient input method.  Ideally, we would want the user to input the code in a list.
	print('Please input the code one character at a time.')
	for i in range(1, m_lenght + 1):
		char = input('>>')
		message.append(chr(char))
	print(message)
ascii_dc()
