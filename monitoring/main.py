from func import RainfallFunc
from graph import Draw

# Executing
# list_dbfs = RainfallFunc.find_dbf_files()
# nlist = RainfallFunc.merge_all_dbf(list_dbfs)

file1 = 'Miedzybrodzie_2016_10_26_no00.dbf'
file2 = 'Miedzybrodzie_2017_05_24_no00.dbf'

nlist = RainfallFunc.merge_dbf(file1, file2)
daily_sum = RainfallFunc.rainfall_sum(nlist)

# Write list file (additional function)
# RainfallFunc.write_file(daily_sum)

Draw.plot_rainfall(daily_sum)