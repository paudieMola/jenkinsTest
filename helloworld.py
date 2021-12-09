def helloworld():
	f = open('helloworld.txt', 'w')
	f.write('Hello World')
	f.close()
	print('Hello Python World!')

if __name__ == '__main__':
    helloworld()
