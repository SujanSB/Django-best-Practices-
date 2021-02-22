from django.contrib import admin
from .models import About
from .models import Services
from .models import LatestWorkWD
from .models import LatestWorkP
from .models import LatestWorkK
from .models import Testimonials
from .models import Contact
from .models import Blog

# Register your models here.
admin.site.register(About)
admin.site.register(Services)
admin.site.register(LatestWorkWD)
admin.site.register(LatestWorkP)
admin.site.register(LatestWorkK)
admin.site.register(Testimonials)
admin.site.register(Contact)
admin.site.register(Blog)