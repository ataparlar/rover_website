from django.views.generic import TemplateView

from .models import SliderImage, MainPageEntry, MainRovers
from sponsors.models import sponsor_new, sponsor_type
from oldyears.models import OldYear
from django.db.models import Prefetch
from django.http import Http404


class MainPage(TemplateView):
    template_name = 'main.html'
    not_found_message = 'Year not found for sponsors page.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)

        sponsor_types = sponsor_type.objects.all()
        sponsors = sponsor_new.objects.prefetch_related(Prefetch('sponsorship_type'))
        print(sponsors)

        extra_context = {
            'sponsors': sponsors,
            'sponsor_types': sponsor_types,
            'slide_images': SliderImage.objects.all(),
            'entries': MainPageEntry.objects.filter(is_old=False),
            'rovers': MainRovers.objects.all(),
        }
        context.update(extra_context)
        return context
