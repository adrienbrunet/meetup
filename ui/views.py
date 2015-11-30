from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import BeerForm


class ClassicDjangoFormView(TemplateView):
    template_name = "classic_django.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BeerForm()
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BeerForm()
        form = BeerForm(request.POST)
        if form.is_valid():
            form.save()
        return super().render_to_response(context)


def internet_explorer(request):
    return render(request, 'static_pages/internet_explorer.html', {})

