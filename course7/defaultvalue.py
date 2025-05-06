#precio de producto, impuesto, descuento
#esta es una función
def calculate_total(price, tax = 0.16, discount = 0):
    total = price + (price * tax) - discount
    return total

total = calculate_total(800)
print('El total es:', total)