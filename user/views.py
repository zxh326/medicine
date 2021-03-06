from django.views.generic import CreateView, ListView, DetailView, View
from dss.Mixin import JsonResponseMixin, MultipleJsonResponseMixin
from dss.Mixin import serializer
from .models import *
from .auth import UserWrap, login_required

from disease.models import Case, FavList
from comment.models import Comment
from neijing.models import NeiJingExam


class RegUserView(JsonResponseMixin, CreateView, UserWrap):
    model = User

    def post(self, request, *args, **kwargs) -> dict:
        self.check()
        if self.msg:
            return self.render_to_response({'msg': self.msg})

        if self.check_user_reg():
            token = self.gen_token(self.user)
            self.update_profile()
            # user = serializer(self.user)
            return self.render_to_response({'msg': 'success', 'user_obj': self.user, 'token': token})
        else:
            user, token = self.reg_user()
            return self.render_to_response({'msg': 'success', 'user_obj': user, 'token': token})


class LoginUserView(JsonResponseMixin, View):
    model = User

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    @login_required
    def post(self, request, *args, **kwargs):
        request.wuser.login()
        return self.render_to_response({'msg': 'success', 'user_obj': request.wuser})


class UserCaseListView(MultipleJsonResponseMixin, ListView):
    model = Case
    paginate_by = 15
    foreign = True
    datetime_format = 'string'

    def get_queryset(self):
        queryset = super(UserCaseListView, self).get_queryset()

        qr = queryset.filter(create_user=self.request.wuser)

        return qr


class UserCaseDetailView(JsonResponseMixin, DetailView):
    model = Case
    foreign = True

    many = True
    datetime_type = 'string'
    pk_url_kwarg = 'case_id'
    exclude_attr = ('main_symptoms', 'main_prescription')
    datetime_format = 'string'
    
    def get_context_data(self, **kwargs):
        context = super(UserCaseDetailView, self).get_context_data(**kwargs)
        context['result'] = serializer(context['case'].get_result(),
                 exclude_attr=('case', 'disease', 'case_id'))
        return context
    

class UserFavListView(MultipleJsonResponseMixin, ListView):
    model = FavList
    paginate_by = 15
    foreign = True
    datetime_format = 'string'
    exclude_attr = ('fa_user','openid', 'reg_date', 'last_login')

    def get_queryset(self):
        queryset = super(UserFavListView, self).get_queryset()

        qr = queryset.filter(fa_user=self.request.wuser)

        return qr


class UserCommentView(MultipleJsonResponseMixin, ListView):
    model = Comment
    datetime_format = 'string'
    exclude_attr = ('reg_date', 'last_login', 'from_user')
    paginate_by = 15

    def get_queryset(self):
        queryset = super(UserCommentView, self).get_queryset()

        qr = queryset.filter(from_user=self.request.wuser)

        return qr


class UserExamView(MultipleJsonResponseMixin, ListView):
    model = NeiJingExam
    datetime_format = 'string'
    exclude_attr = ('exam_raw_id', 'reg_date', 'openid', 'last_login', 'blanks', 'raw', 'u_answers', 'create_user_id')
    paginate_by = 15

    def get_queryset(self):
        queryset = super(UserExamView, self).get_queryset()
        qr = queryset.filter(create_user=self.request.wuser).exclude(u_answers__exact='')
        return qr
