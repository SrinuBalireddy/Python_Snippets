from . import views
import requests
import json
from mishipay import settings


def get_product_list():
    """
    function to fetch the product list from shopify
    """

    query_string = f'{settings.SHOPIFY_URL}/admin/api/2020-07/products.json'
    try:
        resp = requests.get(query_string)
    except requests.exceptions.RequestException as e:
        return None, e.errors

    try:
        context = {
            'products': resp.json()['products']
        }
    except KeyError:
        return None, 'No Products to display'

    return context, ''

def inventory_update(inventory_id, purchase_quantity, order_type):
    """
    function to fetch the inventory details and triggers a post request
    to update the inventory availability
    """
    for index, value in enumerate(inventory_id):
        query_string = f'{settings.SHOPIFY_URL}/admin/api/2020-07/inventory_levels.json?inventory_item_ids={value}'
        try:
            inventory_request = requests.get(query_string)
        except requests.exceptions.RequestException as e:
            return False, e.errors

        if not inventory_request.json()['inventory_levels']:
            return False, "Invalid inventory Id"

        if not purchase_quantity:
            return False, "Enter purchase quantity"

        query_string = f'{settings.SHOPIFY_URL}/admin/api/2020-07/inventory_levels/adjust.json'
        payload = {
            "inventory_item_id": value,
            "location_id": inventory_request.json()['inventory_levels'][0]['location_id'],
            "available_adjustment": -int(purchase_quantity[index])
        }
        try:
            response = requests.post(query_string, headers=settings.HEADER, data=json.dumps(payload))
        except requests.exceptions.RequestException as e:
            return False, e.errors
    return True, 'Successully placed the order'