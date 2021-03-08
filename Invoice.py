class Invoice:
    def __init__(self):
        self.items = {}
    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for v in products.values():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for v in products.values():
            total_discount += float(v['unit_price']) * int(v['qnt']) * float(v['discount']/100)
        total_discount = round(total_discount, 2)
        self.total_dicount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print('y or n! Try again.')

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again")
            else:
                return userInput

    def display(self, products):
        impurePrice = self.totalImpurePrice(products)
        discount = self.totalDiscount(products)
        purePrice = self.totalPurePrice(products)
        return f"Impure Price = {impurePrice} \nDiscount = {discount} \nPure Price = {purePrice}"

    def totalTax(self, products):
        purePrice = self.totalPurePrice(products)
        taxAmount = round(.15 * purePrice,2)
        return taxAmount

