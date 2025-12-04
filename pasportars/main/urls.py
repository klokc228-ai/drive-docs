from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # Основная
    path('reviews/', views.reviews, name='reviews'),   # Отзывы
    path('about/', views.about, name='about'),         # О нас
    path('leave-review/', views.leave_review, name='leave_review'),  # Оставить отзыв
    path('orders/', views.orders, name='orders'),      # Актуальные заказы
    path('review-form/', views.review_form, name='review_form'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),  # Политика конфиденциальности
]
