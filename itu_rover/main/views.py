from django.views.generic import TemplateView

from .models import SliderImage, MainPageEntry, MainRovers
from sponsors.models import sponsor_new, sponsor_type
from members.models import SubTeam, TeamAdvisor, Member, TeamLeader, MembersPage as MP
from core.defaults import current_year
from django.core.exceptions import ObjectDoesNotExist
from oldyears.models import OldYear
from django.db.models import Prefetch
from django.http import Http404


class MainPage(TemplateView):
    template_name = 'main.html'
    not_found_message = 'Year not found for sponsors page.'



    def get_sponsor_context(self):
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        years_sponsors = sponsor_new.objects.filter(sponsorship_year=r_year)
        sponsor_types = (sponsor_type.objects
                         .prefetch_related(
                             Prefetch('sponsors', queryset=years_sponsors)
                         )).distinct()
        if not sponsor_types:
            raise Http404(self.not_found_message)
        return {
            'sponsor_types': sponsor_types,
        }

    def get_member_context(self, year):
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        """try:
            leader = TeamLeader.objects.filter(member__year=r_year).get().member
        except ObjectDoesNotExist:
            leader = None
        try:
            members_page = MP.objects.filter(year=r_year).get()
        except ObjectDoesNotExist:
            members_page = None"""
        years_members = Member.objects.filter(year=year)
        subteams = (SubTeam.objects.all().prefetch_related(     # filter(members__year=year)
            Prefetch('members', queryset=years_members)
        )).distinct()
        if not subteams:
            raise Http404(self.not_found_message)
        return {
            'subteams': subteams,
            'advisors': TeamAdvisor.objects.filter(year=year),
            #'leader': leader,
            'subteamless': Member.objects.filter(subteam=None, year=year),
            #'page': members_page,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        r_year = str(OldYear.objects.all().order_by('-year')[0].year)
        year = self.kwargs.get('year', current_year())

        sponsor_context = self.get_sponsor_context()
        context.update(sponsor_context)

        extra_context = {
            'slide_images': SliderImage.objects.all(),
            'entries': MainPageEntry.objects.filter(is_old=False),
            'rovers': MainRovers.objects.all(),
        }
        context.update(extra_context)

        member_context = self.get_member_context(r_year)
        context.update(member_context)

        return context
