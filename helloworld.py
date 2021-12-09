def helloworld():
	f = open('helloworld.txt', 'w')
	f.write('Hello World')
	f.close()
	print('Hello Python World')
	print('helloworld.txt file created')

helloworld()
