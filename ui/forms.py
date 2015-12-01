from django import forms

from djangular.forms import NgFormValidationMixin, NgModelFormMixin
from djangular.styling.bootstrap3.forms import Bootstrap3ModelForm

from api.models import Beer


class BeerForm(forms.ModelForm):
    '''
    Classic django model form
    '''
    class Meta:
        model = Beer
        fields = ('name', 'abv', 'comments', )


class DjangularBeer(Bootstrap3ModelForm):
    '''
    Form build with metaclass from django-angular.
    The bootstrap3Mixin is only here for rendering purpose (using form.as_div)
    '''

    required_css_class = "required"

    class Meta:
        model = Beer
        fields = ('name', 'abv', 'comments', )


class ValidationAngularBeer(NgFormValidationMixin, DjangularBeer):
    pass


class ModelAngularBeer(NgModelFormMixin, NgFormValidationMixin, DjangularBeer):
    scope_prefix = 'beer_data'
    form_name = 'my_form'


# class AngularModelFormMixin(NgModelFormMixin, NgFormValidationMixin, Bootstrap3ModelForm):
