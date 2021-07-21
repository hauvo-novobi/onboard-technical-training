# Dictionary
# ===

# Exercise 1

def summarize_product(order_1, order_2, order_3, price_list, *args, **kwargs):
    """
    Given 3 orders from a customer within a month, which contains product’s name and quantity
    in form of dictionary key-value. Create a dictionary to summarize how much the customer
    spent on each product. Price list of products, which contains products’ name and price, given
    as below.
    """
    result = {}
    for order in (order_1,order_2,order_3):
        for product in order:
            for key,val in product.items():
                result[key] = result[key] + val*price_list[key] if key in result else val*price_list[key];
        result[key] = val*price_list[key]
    return result
# Exercise 2
def update_order_with_delivered_qty(order, delivery_order, *args, **kwargs):
    """
    Given the following order and delivery order, update the order with delivered quantity provided by the delivery order.
    """
    delivery_qty = {}
    for item in delivery_order:
        delivery_qty[item['product']] = delivery_qty[item['product']] + item['delivered_qty'] if item['product'] in delivery_qty else item['delivered_qty']
    for item in order:
        if item['product'] in delivery_qty:
            item['delivered_qty'] = delivery_qty[item['product']]

# Exercise 3
def unique_product(order, *args, **kwargs):
    """
    Give an order. Print out a consolidated order list with each dictionary contain the unique product and total sum by the given order.
    """
    qty_order = {}
    for item in order:
        qty_order[item['product']] = qty_order[item['product']] + item['ordered_qty'] if item['product'] in qty_order  else item['ordered_qty']
    result = list(map(lambda key: {
        'product': key,
        'ordered_qty': qty_order[key]
    },qty_order.keys()))
    return result

if __name__ == "__main__":
    # Ask user for input or to just execute the chosen function
    print('The program have 3 feature:')
    print('1 - Create a dictionary to summarize how much the customer spent on each product')
    print('2 - Update the order with delivered quantity provided by the delivery order.')
    print('3 - Print out a consolidated order list with each dictionary contain the unique product and total sum by the given order.')

    # result = func(a, b, c=c, d=d)
    while True:
        selection = input('Choose your selection: ')
        if selection == '1':
            order_1 = [{'PowerCore': 1}, {'PowerLine': 1}]
            order_2 = [{'PowerLine': 2}]
            order_3 = [{'PowerCore': 1}, {'PowerPort': 2}]
            price_list = {
                'PowerCore': 790000,
                'PowerLine': 200000,
                'PowerPort': 750000
            }
            print('Sample input:')
            print('order 1:', order_1)
            print('order 2:', order_1)
            print('order 3:', order_1)
            print('price list:', order_1)
            result = summarize_product(order_1,order_2,order_3,price_list)
            print('Result:', result)
        elif selection == '2':
            order = [
                {
                    "product": "PowerCore",
                    "ordered_qty": 2,
                    "delivered_qty": 0
                },
                {
                    "product": "PowerLine",
                    "ordered_qty": 5,
                    "delivered_qty": 0
                },
                {
                    "product": "PowerPort",
                    "ordered_qty": 3,
                    "delivered_qty": 0
                }
            ]
            delivery_order = [
                {
                    "product": "PowerCore",
                    "delivered_qty": 2
                },
                {
                    "product": "PowerLine",
                    "delivered_qty": 3
                }
            ]
            print('Sample input:')
            print('order:', order)
            print('delivery order:', delivery_order)
            update_order_with_delivered_qty(order, delivery_order)
            print('Updated order:', order)
        elif selection == '3':
            order = [
                {
                    "product": "PowerCore",
                    "ordered_qty": 2,
                },
                {
                    "product": "PowerLine",
                    "ordered_qty": 5,
                },
                {
                    "product": "PowerPort",
                    "ordered_qty": 3,
                },
                {
                    "product": "PowerCore",
                    "ordered_qty": 1,
                },
                {
                    "product": "PowerPort",
                    "ordered_qty": 1,
                }
            ]
            print('Sample input:')
            print('order:', order)
            result = unique_product(order)
            print('Result:', result)
        else:
            print("Your input must be 1 or 2 or 3. Please enter another")
            continue
        break