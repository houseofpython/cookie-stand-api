from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import CookieStand
from .serializer import ThingSerializer
from .permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CookieStandList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = ThingSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = ThingSerializer


# Create your views here.
