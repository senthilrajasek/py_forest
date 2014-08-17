import sys
import re

def validate( s_raw, len_m, len_n, wild_card = False ):
	#print s_raw, len_m, len_n, wild_card

	if not s_raw:
		return None
	s_clean = s_raw.strip()
	if wild_card :
		if len( s_clean ) != len_n:
			#print 'here'
			return None
	elif len( s_clean ) != len_m:
		#print len(s_clean) , len_m, len_n, type(len_n),  wild_card
		##print len(s_clean) , len_m, type(len_m)
		#print 'here 2'
		return None

	if s_raw:
		valid_char_set = ['A','B','C','D']
		if wild_card:
			valid_char_set.append('*')

		for i in range( len(s_clean) ):
			if s_clean[i] not in valid_char_set:
				return None
	return s_clean
def validate_length(n, m):
	if n < 1 or n > 1000000:
		return False
	if m < 1 or m > n:
		return False
	return True

def main():
	len_m_n = raw_input()
	len_array = [] 
	if len_m_n:
		len_array = len_m_n.strip().split(" ")
	if len( len_array ) != 2:
		#print 'invalid input'
		return
	if not validate_length(int( len_array[0]), int( len_array[1])):
		return

	s = raw_input()
	s_clean = validate( s, int(len_array[0]), int(len_array[1]) )
	if s_clean:
		#print s_clean
	else:
		#print 'invalid input ', s 
		return
	n = raw_input()
	n_clean = validate( n, int(len_array[0]), int(len_array[1]),  True )
	if n_clean:
		#print n_clean
	else:
		#print 'invalid input ', n 
		return
	n_clean = n_clean.replace('*', "['A', 'B', 'C', 'D']{1}")
	all = re.findall(n_clean, s_clean)
	print len( all ) 


if __name__ == '__main__':
	sys.exit( main() )
