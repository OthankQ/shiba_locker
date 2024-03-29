from django.shortcuts import render

from django.http import HttpResponse
from shop.models import UserAdditionalInfo, Item, Invoice, LineItem, InvoiceStatus, LineItemStatus, Notification, Message, PassKey
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from datetime import datetime
import json


# Retrieve or add Item data
def getPostItem(request):

    if request.method == 'GET':

        # If user is searching based on users
        if request.GET.get('user_id'):

            requested_user_id = request.GET.get('user_id')

            Items = Item.objects.filter(
                user_id=requested_user_id)

            try:

                data = [None] * len(Items)

                for i in range(0, len(Items)):

                    data[i] = {'item_id': Items[i].item_id, 'item_name': Items[i].name, 'price':
                               str(Items[i].price), 'stock': Items[i].stock, 'image': str(Items[i].image), 'description': Items[i].desc}

                data = json.dumps(data)

                return HttpResponse(data, content_type='application/json')

            except(KeyError):

                return HttpResponse('{"status_code": -6, "message": "Key error"}', content_type='application/json')

        # If a user is searching with item name:
        elif request.GET.get('item_id'):

            # Pull item_id from passed in GET params
            requested_item_id = request.GET.get('item_id')

            # If param is not int, exit method and return error message
            try:
                int(requested_item_id)
            except:
                return HttpResponse('{"status_code": -7, "message": "Wrong data type input"}', content_type='application/json')

            # Query for any item that has the same item_id as the passed in params
            Items = Item.objects.filter(
                item_id=requested_item_id)

            try:
                # Create an empty array that has the length of number of queried data
                data = [None] * len(Items)

                # Create an array of dict for each queried data
                for i in range(0, len(Items)):

                    data[i] = {'item_id': Items[i].item_id, 'item_name': Items[i].name, 'price':
                               str(Items[i].price), 'stock': Items[i].stock, 'image': str(Items[i].image), 'description': Items[i].desc}

                data = json.dumps(data)

                return HttpResponse(data, content_type='application/json')

            except(KeyError):

                return HttpResponse('{"status_code": -6, "message": "Key error"}', content_type='application/json')

        # If there is no GET params given, return all the existing items
        Items = Item.objects.order_by()

        data = [None] * len(Items)

        for i in range(0, len(Items)):

            data[i] = {'item_id': Items[i].item_id, 'item_name': Items[i]
                       .name, 'price': str(Items[i].price), 'stock': Items[i].stock, 'image': str(Items[i].image), 'description': Items[i].desc}

        data = json.dumps(data)

        return HttpResponse(data, content_type='application/json')

    # POST method (insert or update)
    elif request.method == 'POST':

        # Check if user is logged in. If not, exit and return -1
        if not request.user.is_authenticated:

            return HttpResponse('{"status_code": -1, "message": "Login required"}', content_type='application/json')

        # Parse in the data sent by user
        data = json.loads(request.body)

        # Check if there are any existing item with matching item_id

        # Update

        # If there is item_id within passed data, it is an update
        if 'item_id' in data.keys():

            original_entry = Item.objects.get(
                item_id=data['item_id'])

            # Check if the owner of this item and the logged-in user is the same user_id
            item_owner_id = original_entry.user_id

            if not item_owner_id == request.user.id:

                return HttpResponse('{"status_code": -3, "message": "User id does not match the item seller id"}', content_type='application/json')

            # Iterate through the posted data to see which part of the data the user wishes to change.
            # Only change the field of a data that has been passed in
            if 'stock' in data.keys():
                original_entry.stock = data['stock']

            if 'name' in data.keys():
                original_entry.name = data['name']

            if 'desc' in data.keys():
                original_entry.desc = data['desc']

            if 'price' in data.keys():
                original_entry.price = data['price']

            original_entry.save()

        # Post new item
        else:

            name = data['name']
            user_id = request.user.id
            price = data['price']
            # image_id = data['image_id']
            stock = data['stock']

            new_item = Item(name=name, price=price,
                            stock=stock, user_id=user_id)

            new_item.save()

            new_item_id = new_item.item_id

            data = {
                "status_code": 0,
                "message": "Success",
                "item_id": new_item_id}

        print('A New item has been added successfully')

        return HttpResponse(f'{data}', content_type='application/json')


def deleteItem(request):

    # If the method is not POST, exit with a status code of -15
    if not request.method == 'POST':
        return HttpResponse('{"status_code": -15, "message": "Wrong method"}', content_type='application/json')

    # Needs to be logged in
    if not request.user.is_authenticated:
        return HttpResponse('{"status_code": -1, "message": "Login required"}', content_type='application/json')

    data = json.loads(request.body)
    item_id = data['item_id']
    item = Item.objects.get(item_id=item_id)
    item_user_id = item.user_id
    current_user_id = request.user.id

    # Check if the logged in user's id is the same as the item's owner id, if not, exit with error code -3
    if not item_user_id == current_user_id:
        return HttpResponse('{"status_code": -3, "message": "User id does not match the item seller id"}', content_type='application/json')

    item.delete()

    return HttpResponse('{"status_code": 0, "message": "Success"}', content_type='application/json')
