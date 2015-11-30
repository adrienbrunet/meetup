from django import forms

from api.models import Beer


class BeerForm(forms.ModelForm):
    '''
    Classic django model form
    '''
    class Meta:
        model = Beer
        fields = ('name', 'abv', 'comments', )


class AngularBeer(BeerForm):
    pass


class ValidationAngularBeer(BeerForm):
    pass


# class AngularModelFormMixin(NgModelFormMixin, NgFormValidationMixin, Bootstrap3ModelForm):
#     required_css_class = "required"
