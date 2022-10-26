from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Product
from django.contrib import messages
# Create your views here.


def shopping_bag(request):

    return render(request, 'bag/bag.html')


def add_product(request, product_id):

    product = Product.objects.get(pk=product_id)
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += qty
                messages.success(request, f'Added {product.name} to your bag')
            else:
                bag[product_id]['products_by_size'][size] = qty
                messages.success(request, f'Added {product.name} to your bag')
        else:
            bag[product_id] = {'products_by_size': {size: qty}}
            messages.success(request, f'Added {product.name} to your bag')
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += qty
            messages.success(
                request, f'Updated {product.name} quantity to {bag[product_id]}')
        else:
            bag[product_id] = qty
            messages.success(request, f'Added {product.name} to your bag')
          
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_quantity(request, product_id):
    qty = int(request.POST.get('qty'))
    size = None

    if size:
        if qty > 0:
            bag[product_id]['products_by_size'][size] = qty
        else:
            del bag[product_id]['products_by_size'][size]
    else:
        if qty > 0:
            bag[product_id] = qty
        else:
            bag.pop[product_id]
        messages.success(request, f'Removed item')
   
    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))
