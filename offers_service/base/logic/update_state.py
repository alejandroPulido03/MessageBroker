import json

import requests
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Offer
from ..serializers import UserSerializer
from ..utils.pika_handler import PikaHandler


@csrf_exempt
def updateStateOffer(request: HttpRequest):
    """
        POST request to update the state of an offer
    """
    if request.method == 'POST':
        offer_id = request.POST.get('offer_id')
        state = request.POST.get('state')
        offer = Offer.objects.get(id=offer_id)
        offer.state = state
        offer.save()
        notifyStateChange(offer)
    return JsonResponse({'status': 'success'}, status=200)


def notifyStateChange(offer: Offer):
    """
        Notify the user that the state of the offer has changed

        Make RPC call to message queue to notify the message service
    """
    pika_handler = PikaHandler()
    pika_handler.open_connection()
    pika_handler.declare_queue('notify_service_queue', durable=True)

    user = getUser(offer.request_id)
    message = {
        'offer_id': offer.id,
        'state': offer.state,
        'name': user.get('nombre'),
        'last_name': user.get('apellido'),
        'email': user.get('email'),
        'phone': user.get('celular')
    }
    print(message)
    pika_handler.send_json_message(json.dumps(message))
    pika_handler.close_connection()


def getUser(service_id):
    """
        make RPC call to get the user in user service

    """
    req = requests.get(f'http://127.0.0.1:8080/api/solicitud/{service_id}/cliente')

    user = UserSerializer(data=req.json())
    user.is_valid()

    return user.data
