from django.urls import path
from accounts.views import (RegisterView, register,
                            login_view, logout_view)
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


app_name = 'accounts'

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]
