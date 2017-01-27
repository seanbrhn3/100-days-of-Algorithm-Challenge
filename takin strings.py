#takes a string and seperates it and puts names in a ordered array
#remember using range(len()) will change whats in you array
#for i in arr: will not let you change anything
def extract(arr):
  new_arr = []
  split_it = arr.split()
  first = ""
  for i in range(len(split_it)):
    if(len(split_it[0]) < len(split_it[i])):
        first = split_it[i]
        new_arr.append(first)
    if(len(new_arr)>0):
     for j in range(len(new_arr)):
        if(len(new_arr[j]) > len(split_it[i]) and new_arr[j] != split_it[i]):
          new_arr.append(split_it[i])
  return new_arr
string = "my name is sandy"
print(extract(string))