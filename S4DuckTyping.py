"""
    Static Vs Dynamic Typing

    static typing
    int a = 10;
    String name = "John";
    ArrayList<String> list = new ArrayList<String>();

    a = 10
    a = "John"
    a = [10, 20, 30]
"""

# dynamic typing
a = 10
print(a, type(a))

a = "John"
print(a, type(a))

a = [10, 20, 30]
print(a, type(a))


class PayByCard:
    def pay(self, amount):
        print("Paying by Card \u20b9", amount)


class PayByNetBanking:
    def pay(self, amount):
        print("Paying by NetBanking \u20b9", amount)


class PayByEWallet:
    def pay(self, amount):
        print("Paying by EWallet \u20b9", amount)


class PayEletricityBill:
    def pay_bill(self, amount, accountid):
        print("Paying \u20b9",amount, "bill for account", accountid)


def duck_testing(payment, amount):
    payment.pay(amount=amount)


duck_testing(PayByCard(), 3000)
duck_testing(PayByNetBanking(), 5000)
duck_testing(PayByEWallet(), 7000)
duck_testing(PayEletricityBill(), 4000)
