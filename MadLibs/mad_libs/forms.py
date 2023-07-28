from django import forms
from .models import MadLib

class MadLibForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        num_prompts = self.instance.num_prompts
        prompt_labels = self.instance.get_word_types_array()

        for i in range(num_prompts):
            self.fields[prompt_labels[(i - 1)]] = forms.CharField(label=prompt_labels[(i - 1)])

        print(self.fields)

    class Meta:
        model = MadLib
        fields = []