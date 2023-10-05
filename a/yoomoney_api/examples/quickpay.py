from yoomoney import Quickpay

quickpay = Quickpay(
            receiver="410012025117208",
            quickpay_form="shop",
            targets="Оплата тут",
            paymentType="SB",
            sum=2,
            )

print(quickpay.base_url)
print(quickpay.redirected_url)