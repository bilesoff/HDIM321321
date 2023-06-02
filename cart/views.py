from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse

from services.models import Service
from goods.models import Good
from .models import Cart, CartGood


# Create your views here.
class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.user.cart

        if not cart:
            cart = Cart.objects.create(user=request.user)

        return render(request, 'cart.html', context={
            'cart': cart
        })

    def post(self, request):
        data = request.POST

        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)

        if data.get('action') == 'update':
            if data['type'] == 'good':
                position = get_object_or_404(cart.goods.all(), id=data['entity'])
                print(position, type(data['amount']), data['amount'])
                if data['amount'] == '0':
                    position.delete()
                    cart.save()
                else:
                    position.amount = data['amount']
                    position.save()
            else:
                position = get_object_or_404(cart.services.all(), id=data['entity'])
                if data['amount'] == '0':
                    cart.services.remove(position)
                else:
                    return HttpResponse(status=400)

            return HttpResponse(status=204)

        if data['type'] == 'good':
            good = get_object_or_404(Good, id=data['entity'])
            if CartGood.objects.filter(good=good, cart=cart).exists():
                cg = CartGood.objects.filter(good=good, cart=cart).first()
                cg.amount += 1
                cg.save()
            else:
                CartGood.objects.create(
                    amount=1,
                    cart=cart,
                    good=good
                )
        elif data['type'] == 'service':
            service = get_object_or_404(Service, id=data['entity'])
            if not cart.services.filter(id=service.id).exists():
                cart.services.add(service)

        cart.save()
        return HttpResponse(status=204)
