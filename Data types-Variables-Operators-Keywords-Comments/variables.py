# to exlpain the variables concept

items_count = 10
customer_name = 'vamsi'
is_bill_paid = False
price = 15.05


print('items_count: ', items_count, 'type of items_count: ',
      type(items_count), 'memory loction: ', id(items_count))
print('customer_name: ', customer_name, 'type of customer_name: ',
      type(customer_name), 'memory loction: ', id(customer_name))
print('is_bill_paid: ', is_bill_paid, 'type of is_bill_paid: ',
      type(is_bill_paid), 'memory loction: ', id(is_bill_paid))
print('price: ', price, 'type of price: ', type(
    price), 'memory loction: ', id(price))

print('toal bill to be paid: ', items_count * price)
