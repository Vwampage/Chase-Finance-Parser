

def open_transactions_csv(filename):
	unparsedcsv = []
	with open(filename,'r') as f:
		for line in f.readlines():
			unparsedcsv.append(line)
	return unparsedcsv

def generate_transaction_list(unparsed_transactions):
	all_transactions = []
	for i in unparsed_transactions:
		split_transaction = i.split(',')
		if 'Type' in split_transaction[0]:
			continue
		transaction_date_list = split_transaction[1].split('/')
		transaction_date = {'month': int(transaction_date_list[0]),'day':int(transaction_date_list[1]),'year':int(transaction_date_list[2])}
		post_date_list = split_transaction[2].split('/')
		post_date = {'month': int(post_date_list[0]),'day':int(post_date_list[1]),'year':int(post_date_list[2])}
		transaction_object = {}
		transaction_object['type'] = split_transaction[0]
		transaction_object['transaction_date'] = transaction_date
		transaction_object['post_date'] = post_date
		transaction_object['description'] = str(split_transaction[3:-1])
		transaction_object['amount'] = float(split_transaction[-1].strip())
		all_transactions.append(transaction_object)
	return all_transactions

def parsing_categories(unparsed_categories):
	categories = {}
	for i in unparsed_categories:
		split_categories = i.split(',')
		if 'Category' in split_categories[1]:
			continue
		categories[split_categories[0].strip()] = split_categories[1].strip()
	return categories


def create_unique_category_list():
	list_of_categories = {}
	for i in category_dict:
		one_category = category_dict[i]
		if one_category not in list_of_categories:
			list_of_categories[one_category] = 0.0
	return list_of_categories





def monthly_total(year, month, transaction_type):
	month_total = 0.0
	category_totals = create_unique_category_list()
	for i in parsed_transactions:
		if i['transaction_date']['year'] == year:
			if i['transaction_date']['month'] == month:
				if transaction_type in i['type']:
					month_total += i['amount']
					for j in category_dict:
						if j in i['description']:
							category_totals[category_dict[j]] += i['amount']
	return (month_total, category_totals)



raw_transactions = open_transactions_csv('/Users/vwampage/dev/chase_data/november2016_january2017.csv')

parsed_transactions = generate_transaction_list(raw_transactions)

category_dict = parsing_categories(open_transactions_csv('/Users/vwampage/dev/chase_data/categories3.csv'))

category_list = create_unique_category_list()



totals_tuple = monthly_total(2016, 11, 'Sale')

print totals_tuple[0]
print totals_tuple[1]
check_category_totals = 0.0
for i in totals_tuple[1]:
	check_category_totals += totals_tuple[1][i]
print check_category_totals




# print category_dict

# for i in raw_transactions:
# 	length_of_line = len(i.split(','))
# 	if length_of_line != 5:
# 		print length_of_line
# 		print i

# print parsed_transactions[4]




