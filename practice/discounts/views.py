from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'discounts/index.html')

def discounts(request): #TODO: context from database
    context = {
        "discounts": [
            {'name': 'Чиббис', 'descr': '1600 бонусов на заказ еды из ресторанов', 'img': '/static/imgs/chibbis.png'},
            {'name': 'ВкусВилл', 'descr': 'Скидка 250 рублей на первый заказ в приложении', 'img': '/static/imgs/vkusvill.png'},
            {'name': 'Уфанет', 'descr': 'Выгодная мобильная связь от 299 руб./мес.', 'img': '/static/imgs/ufanet.png'},
            {'name': 'Делимобиль', 'descr': 'Скидка 700 рублей на первую поездку', 'img': '/static/imgs/delimobil.png'},
            {'name': 'Т-Банк', 'descr': 'Акция в подарок при оформлении кредитной карты', 'img': '/static/imgs/t-bank.png'},
            {'name': 'Доставка "Фудзияма"', 'descr': 'Скидка 54% от компании "Фудзияма"', 'img': '/static/imgs/fudziyama.png'},
            {'name': 'Lacoste', 'descr': 'Скидка 10% на первый заказ"', 'img': '/static/imgs/lacoste.png'},
        ]
    }
    return render(request, 'discounts/discounts.html', context=context)