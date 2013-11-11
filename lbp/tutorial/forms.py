# coding: utf-8

from django import forms
from django.conf import settings

from lbp.utils.models import Category, Licence
from lbp.tutorial.models import TYPE_CHOICES

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div

from crispy_forms_foundation.layout import Layout, Fieldset, Submit, Field, \
    ButtonHolder


class TutorialForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )
    
    image = forms.ImageField(
        label='Selectionnez le logo du tutoriel (max. '+str(settings.IMAGE_MAX_SIZE/1024)+' Ko)', 
        required=False)

    description = forms.CharField(
        max_length=200
    )
    
    type = forms.ChoiceField(choices=TYPE_CHOICES)

    category = forms.ModelMultipleChoiceField(
        label = "Catégories de votre tuto",
        queryset=Category.objects.all(),
        required = False,
    )
    
    licence = forms.ModelChoiceField(
        label = "Licence de votre publication",
        queryset=Licence.objects.all(),
        required = False,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('type'),
            Field('image'),
            Field('category'),
            Field('licence'),
            Submit('submit', 'Valider')
        )
        super(TutorialForm, self).__init__(*args, **kwargs)


class EditTutorialForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    description = forms.CharField(
        max_length=200
    )
    
    image = forms.ImageField(
        label='Selectionnez le logo du tutoriel (max. '+str(settings.IMAGE_MAX_SIZE/1024)+' Ko)', 
        required=False)


    introduction = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    conclusion = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
    
    licence = forms.ModelChoiceField(
        label = "Licence de votre publication",
        queryset=Licence.objects.all(),
        required = False,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('title'),
            Field('description'),
            Field('image'),
            Field('licence'),
            Field('introduction'),
            Field('conclusion'),
            Submit('submit', 'Valider')
        )
        super(EditTutorialForm, self).__init__(*args, **kwargs)


class PartForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    introduction = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    conclusion = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                u'Général',
                Field('title')
            ),
            Fieldset(
                u'Contenu',
                Field('introduction'),
                Field('conclusion')
            ),
            ButtonHolder(
                Submit('submit', 'Valider'),
            )
        )
        super(PartForm, self).__init__(*args, **kwargs)


class ChapterForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    introduction = forms.CharField(
        required=False,
        widget=forms.Textarea
    )
    
    image = forms.ImageField(
        label='Selectionnez le logo du tutoriel (max. '+str(settings.IMAGE_MAX_SIZE/1024)+' Ko)', 
        required=False)

    conclusion = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                u'Général',
                Field('title'),
                Field('image'),
            ),
            Fieldset(
                u'Contenu',
                Field('introduction'),
                Field('conclusion')
            ),
            ButtonHolder(
                Div(
                    Submit('submit', 'Ajouter'),
                    Submit(
                        'submit_continue', 'Ajouter et continuer',
                        css_class='secondary'),
                    css_class='button-group'
                ),
            )
        )
        super(ChapterForm, self).__init__(*args, **kwargs)


class EmbdedChapterForm(forms.Form):
    introduction = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    image = forms.ImageField(
        label='Selectionnez une image', 
        required=False)

    conclusion = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Fieldset(
                u'Contenu',
                Field('image'),
                Field('introduction'),
                Field('conclusion')
            ),
            ButtonHolder(
                Submit('submit', 'Valider')
            )
        )
        super(EmbdedChapterForm, self).__init__(*args, **kwargs)


class ExtractForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    text = forms.CharField(
        label='Texte',
        required=False,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('title'),
            Field('text'),
            Div(
                Submit('submit', 'Ajouter'),
                Submit(
                    'submit_continue', 'Ajouter et continuer',
                    css_class='secondary'),
                css_class='button-group'
            )
        )
        super(ExtractForm, self).__init__(*args, **kwargs)


class EditExtractForm(forms.Form):
    title = forms.CharField(
        label='Titre',
        max_length=80
    )

    text = forms.CharField(
        label='Texte',
        required=False,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('title'),
            Field('text'),
            Submit('submit', 'Modifier'),
        )
        super(EditExtractForm, self).__init__(*args, **kwargs)

class ImportForm(forms.Form):

    file = forms.FileField(
        label='Selectionnez le tutoriel à importer',
        required=False
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('file'),
            Submit('submit', 'Importer'),
        )
        super(ImportForm, self).__init__(*args, **kwargs)