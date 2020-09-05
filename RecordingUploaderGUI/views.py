from flask import render_template
from flask import render_template, flash, redirect
from pydub import AudioSegment

from . import app
from .models import CreatePostForm
from RecordingUploaderLogic.general_handler import DummyUploadFileWithMetadata
 
@app.route('/', methods=['GET', 'POST'])
def createPost():
    form = CreatePostForm()
    # when submit button pressed
    if form.validate_on_submit():
        # brief prompt at top
        flash('Title: {}, Location: {}\nDate: {}, Recording: {}'.format(
            form.recTitle.data, form.recLocation.data, form.recDate.data, form.recAudio.data.filename)
        )
        # passes form data to handler logic
        if DummyUploadFileWithMetadata(form.recTitle.data, form.recLocation.data, form.recDate.data, form.recAudio.data):
            return redirect('/success')
        else:
            return redirect('/failure')
    return render_template('form.html', title='Create Post', form=form)

@app.route('/success')
def Success():
    return render_template('results.html', title='Success')

@app.route('/failure')
def Failure():
    return render_template('results.html', title='Failure')