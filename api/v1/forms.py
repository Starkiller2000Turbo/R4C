from django import forms

from robots.models import Robot


class RobotForm(forms.ModelForm):
    """Форма для создания задания."""

    class Meta:
        model = Robot
        fields = ('model', 'version', 'created')
