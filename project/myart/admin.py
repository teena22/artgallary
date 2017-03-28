from django.contrib import admin
from .models import User
from .models import Msg
from .models import Painting

admin.site.register(User)
admin.site.register(Msg)
admin.site.register(Painting)
