from flask_login import login_required, current_user
from flask import render_template,request,redirect,url_for, abort
from ..models import Pitches,Role,User,Comments
from .. import db,photos
from . import main
from ..email import mail_message
from .forms import PitchForm,CommentForm,UpdateProfile

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch= form.pitch.data
        title=form.title.data

        # Updated pitchinstance
        new_pitch = Pitches(title=title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form= form)

