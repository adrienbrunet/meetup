import json

from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.views.generic import CreateView, FormView, TemplateView

from .forms import BeerForm, DjangularBeer, ModelAngularBeer, ValidationAngularBeer


class ClassicDjangoFormView(CreateView):
    template_name = "classic_django.html"
    form_class = BeerForm
    success_url = reverse_lazy('classic_django')


class DjangularFormView(CreateView):
    template_name = "djangular_form.html"
    form_class = DjangularBeer
    success_url = reverse_lazy('djangular_beer')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = DjangularBeer()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     form = DjangularBeer(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         form = DjangularBeer()
    #     context['form'] = form
    #     return render(request, self.template_name, context)


class DjangularValidationFormView(CreateView):
    template_name = "djangular_validation_form.html"
    form_class = ValidationAngularBeer
    success_url = reverse_lazy('djangular_validation_beer')


class DjangularModelFormView(CreateView):
    template_name = "djangular_model_form.html"
    form_class = ModelAngularBeer
    success_url = reverse_lazy('djangular_model_beer')

    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super().post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body.decode('utf-8')))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return JsonResponse(response_data)


def internet_explorer(request):
    return render(request, 'static_pages/internet_explorer.html', {})
