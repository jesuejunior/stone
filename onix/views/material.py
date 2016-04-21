# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.generic import View
from braces.views import LoginRequiredMixin
from onix.models import Material


class MaterialTemplateView(LoginRequiredMixin, View):
    template_name = 'material/new.html'

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data(request)
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        origin = request.POST.get('origin')

        if request.user.is_authenticated() and name and origin:
            result = Material.objects.get_or_create(name=name, origin=origin)
            result[0].save()

            if result[1]:
                return redirect(reverse('material'), data={'response': 200})

        return HttpResponseRedirect(reverse('material'), data={'response': 500})

    def get_context_data(self, request):
        materials = Material.objects.all()
        cxt = {'materials': materials }
        return cxt
