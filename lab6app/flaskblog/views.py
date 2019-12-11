'''
from functools import wraps
#from flaskblog.forms import AdminUserCreateForm, AdminUserUpdateForm
from flask import abort
from flask_login import current_user
from flask_admin import BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flaskblog.models import User

#def admin_login_required(func):
#    @wraps(func)
#    def decorated_view(*args, **kwargs):
#        if not current_user.is_admin():
#            return abort(403)
#        return func(*args, **kwargs)
#    return decorated_view

#class HelloView(BaseView):
#    @expose('/')
#    def index(self):
#        return self.render('some-template.html')

#    def is_accessible(self):
#        return current_user.is_authenticated() and current_user.is_admin()


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_admin()


class UserAdminView(ModelView):
    column_searchable_list = ('username',)
    column_sortable_list = ('username', 'admin')
    column_exclude_list = ('pwdhash',)
    form_excluded_columns = ('pwdhash',)
    form_edit_rules = ('username', 'admin')
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_admin()

def scaffold_form(self):
    form_class = super(UserAdminView, self).scaffold_form()
    form_class.password = PasswordField('Password')
    return form_class

def create_model(self, form):
    model = self.model(form.username.data, form.password.data,form.admin.data)
    form.populate_obj(model)
    self.session.add(model)
    self._on_model_change(form, model, True)
    self.session.commit()

'''