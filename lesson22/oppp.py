import array as arr
array_num =arr.array("i",[1,2,3,5,3,3,7,9,3])
print("orignal array",array_num)
print("Number of occurences of the number of the number 3 in the said array:")
print(array_num.count(3))
array_num.reverse()
print("reverse the order of items")
print(array_num)