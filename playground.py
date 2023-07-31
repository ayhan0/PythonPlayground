# see a sample o what is in each file
import itertools

import constants
import csv
import  parse_utils
from datetime import datetime
from functools import partial
'''
for fname in constants.fnames:
    print(fname)
    with open(fname) as f:
        print(next(f), end ='')
        print(next(f), end='')
        print(next(f), end='')
    print()

for fname in constants.fnames:
    print(fname)
    with open(fname) as  f:
        reader = csv.reader (f,delimiter = ' ',quotechar = '"')
        print(next(reader))
        print(next(reader))
    print()
for fname in constants.fnames:
    print(fname)
    reader = parse_utils.csv_parser(fname,include_header =True)
    print(next(reader),end='\n')
print('\n')
# just the data
for fname in constants.fnames:
    print(fname)
    reader = parse_utils.csv_parser(fname)
    print(next(reader))
    print(next(reader), end='\n')

reader = parse_utils.csv_parser(constants.fname_update_status)
for _ in range(5):
    record = next(reader)
    record = [str(record[0]),parse_utils.parse_date(record[1])]
    print(record)

for fname,class_name ,parser in zip(constants.fnames,constants.class_names,constants.parsers):
    file_iter = parse_utils.iter_file(fname,class_name,parser)
    print(fname)
    for _ in range(3):
        print(next(file_iter))
    print()
    

gen = parse_utils.iter_combined_plain_tuple(constants.fnames,constants.class_names,
                                      constants.parsers,constants.compressed_fields)
print(list(next(gen)))
print(list(next(gen)))


nt = parse_utils.create_combo_named_tuple_class(constants.fnames,constants.compressed_fields)
print(nt._fields)
data_iter = parse_utils.iter_combined(constants.fnames,constants.class_names,
                                      constants.parsers,constants.compressed_fields)

for row in itertools.islice(data_iter,3):
    print(row)

print('--------------------------------------')

filtered_iter = parse_utils.filtered_iter_combined(constants.fnames,constants.class_names,
                                                   constants.parsers,constants.compressed_fields,
                                                   key = lambda row: row.language =='Icelandic')
for row in filtered_iter:
    print(row)

cutoff_date = datetime(2017,3,1)
def group_key(item):
    return item.gender, item.vehicle_make
data = parse_utils.filtered_iter_combined(constants.fnames,constants.class_names,
                                         constants.parsers,constants.compressed_fields,
                                         key = lambda row: row.last_updated >= cutoff_date)
sorted_data = sorted(data,key=group_key)

#groups = itertools.groupby(sorted_data,key=group_key)
#group_1,group_2 = itertools.tee(groups,2) #here is the solution for below error exthaustion of lists
# and another error occured  tee makes shallow copies so we are not able to call subiterator twice
# cause they have same memory address we gonna use two group by
groups1 = itertools.groupby(sorted_data,key=group_key)
groups2 = itertools.groupby(sorted_data,key=group_key)
group_f = (item for item in groups1 if item[0][0] == 'Female')
data_f = ((item[0][1] ,len(list(item[1]))) for item in group_f) # number of vehicles by brand
print('group_f')
for row in data_f:
    print(row)

print('----------------------------------------------')

group_m = (item for item in groups2 if item[0][0] == 'Male')
#for row in group_m: #why was it empty
    # the reason why groups exthausted cause we called it two times
    # it print the female gender but not the males
#    print(row)
data_m= ((item[0][1] ,len(list(item[1]))) for item in group_m)
print('group_m')
for row in data_m:
    print(row)
def group_key(item):
    return item.vehicle_make
data = parse_utils.filtered_iter_combined(constants.fnames,constants.class_names,
                                         constants.parsers,constants.compressed_fields,
                                         key = lambda row: row.last_updated >= cutoff_date)
data_1,data_2 = itertools.tee(data,2)
data_m = (row for row in data_1 if row.gender == 'Male')
# we gonna make it iterate over data twice
#its problem because its iterator its gonna be exhausted
sorted_data_m = sorted(data_m,key=group_key)
groups_m = itertools.groupby(sorted_data_m,key=group_key)
groups_m_counts = ((g[0],len(list(g[1])))for g in groups_m)
print('groupm')
for row in groups_m_counts:
    print(row)

print('------------------------------------------------------')
data_f =(row for row in data_2 if row.gender == 'Female')
sorted_data_f = sorted(data_f,key=group_key)
groups_f = itertools.groupby(sorted_data_f,key=group_key)
groups_f_counts = ((g[0],len(list(g[1])))for g in groups_f)
print(('groupf'))
for row in groups_f_counts:
    print(row)
'''
cutoff_date = datetime(2017,3,2)
def filter_key (cutoff_date,gender,row):
   return row.last_updated >= cutoff_date and row.gender == gender
results_f = parse_utils.group_data(constants.fnames,constants.class_names,
                                  constants.parsers,constants.compressed_fields,
                                  filter_key= partial(filter_key,cutoff_date,'Female'),
                                  group_key=lambda  row: row.vehicle_make)

results_m = parse_utils.group_data(constants.fnames,constants.class_names,
                                  constants.parsers,constants.compressed_fields,
                                  filter_key= partial(filter_key,cutoff_date,'Male'),
                                  group_key=lambda  row: row.vehicle_make)
for row in results_f:
    print(row)

print('-*----------------------------------------------------------------------------------*-')

for row in results_m:
    print(row)