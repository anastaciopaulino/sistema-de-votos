from django.views import generic
from partidos.models import Partido

class HomePage(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['partidos'] = Partido.objects.all()

        return context