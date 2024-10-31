from django.views.generic import TemplateView, ListView

from petstagram.common.view_mixins import RedirectToDashboardIfLoggedInMixin
from petstagram.main.models import PetPhoto


# def show_home(request):
#     context = {
#         'hide_additional_nav_items': True,
#     }
#
#     return render(request, 'home_page.html', context)
class HomePageView(RedirectToDashboardIfLoggedInMixin, TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardPageView(ListView):
    template_name = 'dashboard.html'
    model = PetPhoto
    context_object_name = 'pet_photos'