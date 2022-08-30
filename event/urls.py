from django.urls import path

from .views import CreateCounterView


urlpatterns = [
    path('', CreateCounterView.as_view()),
]