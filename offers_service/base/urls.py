from django.urls import path

from .logic.update_state import updateStateOffer

urlpatterns = [
    path('change_offer_state/', updateStateOffer),
]
