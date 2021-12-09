#slicing = create a substring by extracting elements fromm another string
#indexing[] or slice()
# [start:stop:step]
#start is inclusive and stop is exclusive
#step is 1 by default

# name = "Navik Rana"

# first_name = name[:6]
# last_name = name[6:]

# print(first_name)
# print(last_name)

# #reverse a string
# reversed_name = name[::-1]
# print(reversed_name)

website = "https://google.com"

slice = slice(8,-4)
print(website[slice])
