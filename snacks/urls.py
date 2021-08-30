from django.urls import path
from .views import SnackListView, SnacksDetailView

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnacksDetailView.as_view(), name="snack_detail"),
]
