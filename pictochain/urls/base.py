from django.urls import path, include


urlpatterns = [
    path('', include('image2key.urls')),
    # path('account/', include('users.urls')),
    # path('community/', include('community.urls'))
]

