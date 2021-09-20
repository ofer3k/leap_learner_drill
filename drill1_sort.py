# built in function:
prime_numbers = [4,7,1,9,4,5 ]
# print the list
print(prime_numbers,'before sort - built in')
# sort the list
prime_numbers.sort()
# print it sorted
print(prime_numbers,'after sort - built in')
# ---------------------------------------------------------------------------------

# my function:
prime_numbers_custom = [4,7,1,9,4,5 ]
# print the list
print(prime_numbers_custom,'before sort - custom func')
i=0
while i<len(prime_numbers_custom):
    key=i
    j=i+1
    while j<len(prime_numbers_custom):
        if prime_numbers_custom[key]>prime_numbers_custom[j]:
            key=j
        j+=1
    prime_numbers_custom[i],prime_numbers_custom[key]=prime_numbers_custom[key],prime_numbers_custom[i]
    i+=1
print(prime_numbers_custom,'after sort - custom func')
