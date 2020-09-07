from django.shortcuts import render, redirect
from . import shopify_requests
from django.contrib import messages


def product_home(request):
    """
    product home page. Displays the shopify products.
    """
    context, message = shopify_requests.get_product_list()
    if context is not None:
        messages.success(request, message)
    else:
        messages.warning(request, message)

    return render(request, 'mishipay_shopify/product_list.html', context=context)


def orders(request):
    """
    view to display the products for the users to create orders
    """
    context, message = shopify_requests.get_product_list()
    if context is not None:
        messages.success(request, message)
    else:
        messages.warning(request, message)

    return render(request, 'mishipay_shopify/orders.html', context=context)


def inventory_update(request, order_type):
    """
    Reads the order information from the POST request
    Invokes inventory update function to update the inventory data
    """

    if request.method == 'POST':
        inventory_id_list = request.POST.getlist('items')
        purchase_quantity_list = [quantity for quantity in request.POST.getlist('Quantity') if quantity]

        if inventory_id_list:
            response, message = shopify_requests.inventory_update(inventory_id_list, purchase_quantity_list, order_type)
        else:
            messages.warning(request, 'Please select an item')
            return redirect('place_order')

        if response:
            messages.success(request, message)
        else:
            messages.warning(request, message)

    return redirect('place_order')






