def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("PART A OUTPUT:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Explanation:
# The default list cart=[] is created only once when the function is defined.
# So the same list is reused across function calls.
# That is why "apple", "banana", and "eggs" accumulate in the same list.
# But ["bread"] is a separate list passed manually.
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart


print("\nPART B OUTPUT:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item_fixed("eggs"))

#building shopping cart system
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)

def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price
    except TypeError as e:
        print("\nTuple Error:", e)

def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = (cart["discount"] / 100) * total
    final_total = total - discount_amount

    return final_total

cart1 = create_cart("Pranav", 10)
cart2 = create_cart("Aditya", 10)

add_to_cart(cart1, "PS5", 50000, 1)
add_to_cart(cart1, "Song ult wear",16000, 1)

add_to_cart(cart2, "Xbox",60000, 1)
add_to_cart(cart2, "Sony WH-1000XM6",35000, 1)

print("\nCART 1:")
print(cart1)

print("\nCART 2:")
print(cart2)

print("\nCart 1 Total:", calculate_total(cart1))
print("Cart 2 Total:", calculate_total(cart2))

price_info = ("PS5", 50000)

update_price(price_info, 60000)

# 1.
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable.



# 2.
# Rebinding is assigning a variable to a completely new object.
# Mutating is changing the contents of the same object.


# 3.
# list, dict, set are mutable.
# tuple, str, int are immutable.


# 4.
# Yes, changes do reflect outside. Because lists are mutable and Python passes references to objects.