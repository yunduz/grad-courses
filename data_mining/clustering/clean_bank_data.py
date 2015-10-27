import sys


def find_max_attrs_values(data):
    age = 0
    income = 0
    children = 0

    for record in data:
        age = max(age, record[0])
        income = max(income, record[1])
        children = max(children, record[2])

    return age, income, children

def write_normalized_data(data, f_out, max_vals):
    for record in data:
        f_out.write('%f,%f,%f\n' % (record[0]/max_vals[0], 
                                    record[1]/max_vals[1], 
                                    record[2]/max_vals[2]))


bank_data_dir_path = '/home/yunduz/CMPT741/Assn3'
bank_data_f_name = 'bank-data.csv'
relation = bank_data_f_name.split('.')[0]
bank_data_arff = '%s.arff' % (relation)

data = []

with open('%s/%s' % (bank_data_dir_path, bank_data_f_name), 'r') as f_in, \
     open(bank_data_arff, 'w') as f_out:

    f_out.write('@RELATION %s\n\n' % relation)

    f_out.write('@ATTRIBUTE age NUMERIC\n')
    f_out.write('@ATTRIBUTE income NUMERIC\n')
    f_out.write('@ATTRIBUTE children NUMERIC\n')

    f_out.write('\n@DATA\n')

    # skip header line
    f_in.readline()

    for line in f_in:
        attrs = line.split()
        if attrs:
            attrs = attrs[0].split(',')
            data.append([float(attrs[1]), float(attrs[4]), float(attrs[6])])

    max_vals = find_max_attrs_values(data)
    print max_vals
    write_normalized_data(data, f_out, max_vals)