from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """


    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        pass
    else:
        bag[item_id] = 1
        messages.success(request, f'Added {product.name} to your bag')


    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try: 
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

        else:
                bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

    