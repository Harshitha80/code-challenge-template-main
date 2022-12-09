
from django.urls import path
from .views import WeatherApi, Corn_grain_yieldApi, DataAnalysisApi

urlpatterns = [
    path("weather",WeatherApi.as_view()),
    path("yield",Corn_grain_yieldApi.as_view()),
    path("weather/stats",DataAnalysisApi.as_view()),
]