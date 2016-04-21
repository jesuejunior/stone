#encodgin: utf-8
from braces.views import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.views.generic import View


class HomeTemplateView(LoginRequiredMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context={},
            **kwargs
        )

