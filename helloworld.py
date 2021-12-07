def helloworld()
	f = open(path_to_file, mode)
	with open('readme.txt', 'w') as f:
    	f.write('Hello World')
	f.close()

if __name__ == '__main__':
    logging.basicConfig()
    helloworld()