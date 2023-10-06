from django.shortcuts import render, redirect
from .models import Customers
from yoomoney_api.examples import history
from datetime import datetime
from django.http import HttpResponse

red = ''

def index(request):
    global red
    r = request.GET
    r = str(r)
    if request.method == 'GET':
        if 'finland' in r:
            if '1day' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=Оплата VPN в Финляндии на 1 день&paymentType=SB&sum=50'
            if '1week' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100'
            if '1month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200'
            if '3month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500'
            if '6month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000'
            if '1year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750'
            if '2year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D0%B8%D0%B8%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000'
        if 'germany' in r:
            if '1day' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B4%D0%B5%D0%BD%D1%8C&paymentType=SB&sum=50'
            if '1week' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100'
            if '1month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200'
            if '3month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500'
            if '6month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000'
            if '1year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750'
            if '2year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000'
        if 'usa' in r:
            if '1day' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%B4%D0%B5%D0%BD%D1%8C&paymentType=SB&sum=50'
            if '1week' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D1%8E&paymentType=SB&sum=100'
            if '1month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86&paymentType=SB&sum=200'
            if '3month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%203%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B0&paymentType=SB&sum=500'
            if '6month' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%206%20%D0%BC%D0%B5%D1%81%D1%8F%D1%86%D0%B5%D0%B2&paymentType=SB&sum=1000'
            if '1year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%201%20%D0%B3%D0%BE%D0%B4&paymentType=SB&sum=1750'
            if '2year' in r:
                redd = 'https://yoomoney.ru/quickpay/confirm.xml?receiver=410012025117208&quickpay-form=shop&targets=%D0%9E%D0%BF%D0%BB%D0%B0%D1%82%D0%B0%20VPN%20%D0%B2%20%D0%A1%D0%A8%D0%90%20%D0%BD%D0%B0%202%20%D0%B3%D0%BE%D0%B4%D0%B0&paymentType=SB&sum=3000'
        qq = Customers()
        qq.location = request.GET.get('location')
        qq.plan = request.GET.get('plan')
        qq.save()
        if qq.location == 'finland':
            a_location = 'Финляндии'
        if qq.location == 'germany':
            a_location = 'Германии'
        if qq.location == 'usa':
            a_location = 'США'
        if qq.plan == '1day':
            a_plan = '1 день'
            a_sum = '50 ₽'
        if qq.plan == '1week':
            a_plan = '1 неделю'
            a_sum = '100 ₽'
        if qq.plan == '1month':
            a_plan = '1 месяц'
            a_sum = '200 ₽'
        if qq.plan == '3months':
            a_plan = '3 месяца'
            a_sum = '500 ₽'
        if qq.plan == '6months':
            a_plan = '6 месяцев'
            a_sum = '1000 ₽'
        if qq.plan == '1year':
            a_plan = '1 год'
            a_sum = '1750 ₽'
        if qq.plan == '2years':
            a_plan = '2 года'
            a_sum = '3000 ₽'
        red += redd
        return render(request, 'hello/index.html', context={'a_location': a_location, 'a_plan': a_plan, 'a_sum': a_sum})
    if request.method == 'POST':
        return redirect(red)

def get_key(request):
    if request.method == 'POST':
        history.check()
        keyy = 'TEST_KEY'
        if history.ch == True:
            # print(datetime.now())
            print(Customers)
            # print(str(history.dt) == '2021-09-25 22:05:37')
        return render(request, 'hello/success.html', context={'keyy': keyy})
    # Handle other HTTP methods or cases if needed
    return HttpResponse('Method not allowed', status=405)  # Return an appropriate response for other cases

def instruction(request):
    return redirect('https://uniqvpn.com/ru/instructions/')