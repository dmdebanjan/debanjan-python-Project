# items_in_cart = 0

# assert (items_in_cart == 2)

# if items_in_cart != 2:
#    raise Exception("Product count does not match")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleanup resources")