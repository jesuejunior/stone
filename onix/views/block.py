from braces.views import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View, ListView

from onix.models import Block, Material
from tools.code_generator import generate_code


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
        material_id = request.POST.get('material_id')
        number = request.POST.get('number')
        code = None

        while(True):
            code = generate_code()
            if not Block.objects.filter(code=code).exists():
                break

        if request.user.is_authenticated() and number:
            result = Block.objects.get_or_create(material_id=material_id, number=number, code=code)

            saved = result[0].save()

        if saved:
            return HttpResponse(reverse('blocks'), data={'response': 200})

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
            'materials': Material.objects.all()
        }

        return cxt


class BlockListTemplateView(LoginRequiredMixin, ListView):
    template_name = 'block/list.html'
    model = Block

