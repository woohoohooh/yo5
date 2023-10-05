from django.shortcuts import render, redirect
from .models import Customers

def index(requests):
    r = requests.GET
    r = str(r)
    if 'finland' in r:
        if '1day' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=Оплата VPN в Финляндии на 1 день&paymentType=SB&sum=50')
        if '1week' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100')
        if '1month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200')
        if '3month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500')
        if '6month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000')
        if '1year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750')
        if '2year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000')
    if 'germany' in r:
        if '1day' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B4%D0%B5%D0%BD%D1%8C&paymentType=SB&sum=50')
        if '1week' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100')
        if '1month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200')
        if '3month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500')
        if '6month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000')
        if '1year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750')
        if '2year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000')
    if 'usa' in r:
        if '1day' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%B4%D0%B5%D0%BD%D1%8C&paymentType=SB&sum=50')
        if '1week' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100')
        if '1month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200')
        if '3month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500')
        if '6month' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000')
        if '1year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750')
        if '2year' in r:
            return redirect('https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000')
    qq = Customers.objects.all()
    if requests.method == "GET":
        qq.location = requests.GET.get("location")
        qq.plan = requests.GET.get("plan")
        with open('saved.txt', 'a', encoding='1258') as f:
            f.write(qq.id)
            f.write(qq.location)
            f.write(qq.plan)
            f.write('\n')
        qq.save()
    return render(requests, 'hello/index.html')
