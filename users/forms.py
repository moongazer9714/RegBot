from django.forms import ModelForm
from bot.models import UserInformation


class CustomUserModelForm(ModelForm):
    class Meta:
        model = UserInformation
        fields = '__all__'

