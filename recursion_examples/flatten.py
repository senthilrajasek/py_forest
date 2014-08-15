import sys

def flatten( input_array ):
	if type( input_array ) == int:
		return [input_array]
	else:
		if len( input_array ) > 1:
			return flatten( input_array[0] ) + flatten( input_array[1:] )
		else:
			return flatten( input_array[0] )


def main():
	print flatten( [1, 3, [5, 7, 11], 13, 17, [19]] )
if __name__ == '__main__':
	sys.exit( main() )
