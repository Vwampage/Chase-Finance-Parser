

def open_transactions_csv():
	unparsedcsv = []
	with open('/Users/vwampage/dev/chase_data/november2016_january2017.csv','r') as f:
		for line in f.readlines():
			unparsedcsv.append(line)
	return unparsedcsv




print open_transactions_csv()