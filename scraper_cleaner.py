import pandas as pd
 
# read by default 1st sheet of an excel file
df = pd.read_excel('Powerball_2016_2024.xlsx')
df = df.astype("string")

nums = []
data = []
vec = []
count_rows = len(df.index)
i = 0
dates = []
dates_str = ''
structured_nums = []
vec_temp = []

for col in df:
    for i in range(count_rows):
        data.append(df[col][i]) #create a copy of the data for manipulation

#Returns unstructured powerball and powerball plus numbers
for x in range(count_rows):
    inp_str = data[x]
    for i in range(285,len(inp_str)-1): #290 comes from the amount of characters with spaces we have to skip until we see lotto numbers including forein html characters
        
        #powerball value is two digits
        if inp_str[i].isdigit() and inp_str[i+1].isdigit():
            nums.append(inp_str[i]+inp_str[i+1])

        #powerball value is one digit
        elif inp_str[i].isdigit() and inp_str[i+1].isdigit() == False and inp_str[i-1].isdigit() == False:
            nums.append(inp_str[i])

#Returns dates
for y in range(count_rows):
    inp_str = data[y]
    
    for k in range(len(inp_str)-1):

        if inp_str[k] == '/' and inp_str[k+1].isdigit() and inp_str[k+4].isdigit():
            for j in range(10):
                dates_str += inp_str[k+1]
                k +=1
            dates.append(dates_str)
            dates_str = ''

nums_copy = nums[:]

while len(nums_copy) > 12:
    for i in range(12):
        vec_temp.append(nums_copy[i])
    vec.append(vec_temp)
    del nums_copy[0:12]
    vec_temp = []

vec.append(nums_copy)
del nums_copy
    
df_1 = pd.DataFrame(dates)
df_1.to_excel("PB_Analysis_2016-2024(DATES).xlsx")









