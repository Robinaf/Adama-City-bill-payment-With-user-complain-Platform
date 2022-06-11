from django.contrib.auth.backends import ModelBackend
from .models import Account
from users.models import *

class CustomAuthenticate(ModelBackend):
    def authenticate(self, request, username=None, password=None, db=None):
        try:
            user = Account.objects.all().using(db).get(username=username)
            if user.check_password(password):
                return user
        except:
            return None

    def get_user(self, username):
        try:
             user = Account._default_manager.get(pk=username)
       
        except Account.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
        
        
    
    