from django import forms
from django.utils.translation import ugettext_lazy as _
from django_genericfilters import forms as gf


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input"
            }
        ))


class UserListForm(gf.FilteredForm):
    is_active = gf.ChoiceField(label=_('Status'),
                               choices=(('yes', _('Active')),
                                        ('no', _('Unactive'))))

    is_staff = gf.ChoiceField(label=_('Staff'))

    is_superuser = gf.ChoiceField(label=_('Superuser'))

    def get_order_by_choices(self):
        return [('date_joined', _(u'date joined')),
                ('last_login', _(u'last login')),
                ('last_name', _(u'Name'))]
