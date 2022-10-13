from app1.models import Item
from django import forms


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['valid_from'].help_text = "Date Should Be like this -> yyyy-mm-dd --> 2022-10-09"

    # valid_from = forms.DateField(
    #     widget=SelectDateWidget(
    #         empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #     ),
    # )
