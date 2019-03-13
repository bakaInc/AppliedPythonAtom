
import sys


from get_parsed import get_csv,get_json,check_format
from encoding import get_c1251,get_utf_8,get_utf_16,get_encodeFile
from printtable import print_table

if __name__ == '__main__':
    filename = sys.argv[1]

    data = check_format(get_encodeFile(filename))
	print_table(data)
