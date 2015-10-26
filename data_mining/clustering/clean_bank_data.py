import sys

bank_data_dir_path = '/home/yunduz/CMPT741/Assn3'
bank_data_f_name = 'bank-data.csv'
relation = bank_data_f_name.split('.')[0]
bank_data_arff = '%s.arff' % (relation)

with open('%s/%s' % (bank_data_dir_path, bank_data_f_name), 'r') as f_in, open(bank_data_arff, 'w') as f_out:

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
            f_out.write('%s,%s,%s\n' % (attrs[1], attrs[4], attrs[6]))