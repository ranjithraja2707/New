#
# a = {"sowmiya","Hari","Naveen kumar"}
# b = {i : len(i)+len(i) for i in a}
# print(b)
# for i in a:
#     print(i,len(i)+len(i),end=",")

try:
    raise Exception("here is the error")
    print(x)
except Exception as e:
    print("Error Found:",e)
finally:
    print("Thank you very much")
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    unique_list = list(set(input_list))
    return unique_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result = remove_duplicates(input_list)
print("Original List:", input_list)
print("List with Duplicates Removed:", result)
