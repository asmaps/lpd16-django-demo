from django.views.generic import CreateView
from .models import Presentation


class PresentationListView(CreateView):
    model = Presentation
    template_name = 'lpd/presentation_list.html'
    fields = ('title', 'presenter', 'length')
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['presentation_list'] = Presentation.objects.all()
        return context
