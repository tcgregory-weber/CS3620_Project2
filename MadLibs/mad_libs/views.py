from django.shortcuts import render, get_object_or_404, redirect
from .models import MadLib
from .forms import MadLibForm
import random
import json

def index(request):
    random_madlib = random.choice(MadLib.objects.all())
    return redirect('mad_libs:get_words', madlib_id=random_madlib.id)

def get_words(request, madlib_id):
    madlib = get_object_or_404(MadLib, id=madlib_id)
    form = MadLibForm(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        # Save the words into a dictionary
        # Key is the word type, value is the word
        user_words = {}
        for word_type in madlib.word_types_array:
            print(word_type)
            user_words[word_type] = form.cleaned_data.get(word_type)
        # Convert the dictionary into a JSON string
        user_words = json.dumps(user_words)
        return redirect('mad_libs:mad_lib', madlib_id=madlib.id, words=user_words)

    return render(request, 'mad_libs/mad_lib_form.html', {'form': form, 'madlib': madlib})

def mad_lib(request, madlib_id, words):
    madlib = get_object_or_404(MadLib, id=madlib_id)
    new_story = madlib.story.split()
    # Convert the JSON string back into a dictionary
    words = json.loads(words)

    for i in range(len(new_story)):
        if new_story[i][0] == '[':
            # find last index of ']'
            end_index = new_story[i].index(']')
            # get the word type
            word_type = new_story[i][1:end_index]
            # recapture any punctuation
            punctuation = ''
            try:
                if not new_story[i][end_index + 1].isalpha():
                    punctuation = new_story[i][end_index + 1]
            except IndexError:
                pass
            # replace the word type with the user's word
            new_story[i] = words[word_type] + punctuation
    updated_story = " ".join(new_story)
    return render(request, 'mad_libs/display_mad_lib.html', {'madlib': updated_story})