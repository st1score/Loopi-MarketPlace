# products/cart.py

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            # если вдруг старый формат — int
            if isinstance(self.cart[product_id], int):
                self.cart[product_id] = {'quantity': self.cart[product_id]}
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def __iter__(self):
        from .models import Product
        cart = self.cart.copy()
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            product_id = str(product.id)
            item = cart[product_id]
            if isinstance(item, int):
                item = {'quantity': item}
            item['product'] = product
            cart[product_id] = item

        for item in cart.values():
            yield {
                'product': item['product'],
                'quantity': item['quantity'],
                'total_price': item['product'].price * item['quantity']
            }

    def get_total_price(self):
        return sum(item['product'].price * item['quantity'] for item in self)
