from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import BeerForm, DjangularBeer, ModelAngularBeer, ValidationAngularBeer


class ClassicDjangoFormView(FormView):
    template_name = "classic_django.html"
    form_class = BeerForm
    success_url = reverse_lazy('classic_django')


class DjangularFormView(FormView):
    template_name = "djangular_form.html"
    form_class = DjangularBeer
    success_url = reverse_lazy('djangular_beer')


class DjangularValidationFormView(FormView):
    template_name = "djangular_validation_form.html"
    form_class = ValidationAngularBeer
    success_url = reverse_lazy('djangular_validation_beer')


class DjangularModelFormView(FormView):
    template_name = "djangular_model_form.html"
    form_class = ModelAngularBeer
    success_url = reverse_lazy('djangular_model_beer')

    def post(self, request, **kwargs):
        if request.is_ajax():
            return self.ajax(request)
        return super().post(request, **kwargs)

    def ajax(self, request):
        form = self.form_class(data=json.loads(request.body))
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}
        return JsonResponse(response_data)


def internet_explorer(request):
    return render(request, 'static_pages/internet_explorer.html', {})
