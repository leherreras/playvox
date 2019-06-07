from flask import render_template
from flask import request
from flask_classy import FlaskView

from apps.notes.controller import save_note
from common.negotiation import render


class NotesView(FlaskView):
    route_prefix = '/v1/'

    def insert(self, user_id):
        contex = {'user_id': user_id}
        return render_template('insert_note.html', **contex)

    def post(self):
        data = request.form.to_dict()
        note = save_note(**data)
        context = {'data': note}
        return render(note, 'note.html', ctx=context)
