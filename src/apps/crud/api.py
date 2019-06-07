from flask_classy import FlaskView, route
from flask import request
from flask_paginate import Pagination
from flask import render_template
from common.negotiation import render
from .controller import get_user_per_page, get_user, save_user, delete_user

PER_PAGE = 15

class UsersView(FlaskView):
    route_prefix = '/v1/'

    def index(self):
        """
        Show all users in the system
        :return: return package of users with pagination
        """
        page = int(request.args.get('page', 1))
        query = eval(request.args.get('query', '{}'))
        users_count, data = get_user_per_page(page, PER_PAGE, query)
        pagination = Pagination(page=page, per_page=PER_PAGE, total=users_count, css_framework='bootstrap3')
        context = {'data': data, 'pagination': pagination}

        return render(data, 'users.html', ctx=context)

    def insert(self):
        return render_template('insert.html')

    def destroy(self,user_id):
        """
        Remove user in db
        :param user_id: id of specific user
        :return: confirmation message
        """
        deletes = delete_user(user_id)
        context = {'data': deletes}
        return render(deletes, 'delete.html', ctx=context)

    def modify(self, user_id):
        """
        Update user with json sending with information
        :param user_id: id of specific user
        :return: user's information
        """
        pass

    def get(self, user_id):
        """
        Show information about user
        :param user_id: id of specific user
        :return: user's information
        """
        user = get_user(user_id)
        context = {'data': user}
        return render(user, 'user.html', ctx=context)

    def post(self):
        """
        create users
        :return: reference of user created
        """
        data = request.form.to_dict()
        user = save_user(**data)
        context = {'data': user}
        return render(user, 'user.html', ctx=context)
