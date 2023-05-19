from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your Cart is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N9ZgzDVaLPlrwlf8CNeENdFyKGtYtPaxYSz8nYyLZ1wCLWf4SU5iVRXYLTM7xxK2cHwjge64KQQFSiFlE8Z2UgW00e77kWYlH',
    }

    return render(request, template, context)