from django.db import models

class MadLib(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    word_types = models.TextField()
    num_prompts = models.IntegerField(default=0)

    def get_word_types_array(self):
        return [word.strip() for word in self.word_types.split(',')] if self.word_types else []

    def set_word_types_array(self, word_types):
        self.word_types = ','.join(word_types)

    word_types_array = property(get_word_types_array, set_word_types_array)

    def __str__(self):
        return self.title