# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from braces.views import LoginRequiredMixin
from onix.models import Block
from tools.code_generator import generate_code


class HomeTemplateView(LoginRequiredMixin, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context={},
            **kwargs
        )


class BlockTemplateView(LoginRequiredMixin, View):
    template_name = 'block/new.html'

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
        number = request.POST.get('number')
        code = None

        while(True):
            code = generate_code()
            exist = Block.objects.filter(code=code).exists()
            if not exist:
                break

        if request.user.is_authenticated() and number:
            result = Block.objects.get_or_create(name=name, number=number, code=code)

            saved = result[0].save()

        if saved:
            return HttpResponseRedirect(reverse('blocks'))

        return HttpResponseRedirect(reverse('blocks'))

    def get_context_data(self, request):

        _question = Block.objects.all()
        paginator = Paginator(_question, 50)

        page = request.GET.get('page')

        try:
            blocks = paginator.page(page)
        except PageNotAnInteger:
            blocks = paginator.page(1)
        except (EmptyPage, InvalidPage):
            blocks = paginator.page(paginator.num_pages)

        cxt = {
            'blocks': blocks,
        }

        return cxt


class BlockListTemplateView(LoginRequiredMixin, ListView):
    template_name = 'block/list.html'
    model = Block

    # def get(self, request, *args, **kwargs):
    #     cxt = self.get_context_data(request)
    #     return TemplateResponse(
    #         request=self.request,
    #         template=self.template_name,
    #         context=cxt,
    #         **kwargs
    #     )
    #
    # def get_context_data(self, request):
    #     result = self.model.objects.all()
    #     return {'results': result}
