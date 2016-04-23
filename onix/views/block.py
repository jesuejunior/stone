from braces.views import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
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
        cxt = self.get_context_data(request)
        material_id = request.POST.get('material_id')
        number = request.POST.get('number')
        code = None

        while(True):
            code = generate_code()
            if not Block.objects.filter(code=code).exists():
                break

        if request.user.is_authenticated() and number and material_id:
            if Block.objects.filter(material_id=material_id, number=number).exists():
                material = Material.objects.get(pk=material_id).name
                cxt['message']= u'O código [{0}] já foi utilizada para [{1}], por favor verifique os dados.'.format(number, material)
                cxt['status'] = 'error'
                return TemplateResponse(
                    request=self.request,
                    template=self.template_name,
                    context=cxt,
                    status=400,
                    **kwargs
                )

            result = Block.objects.get_or_create(material_id=material_id, number=number, code=code)
            saved = result[0].save()

            if saved:
                return HttpResponse(reverse('blocks'), content={'message': 'Bloco criado com sucesso.', 'status': 'ok'})
        return HttpResponseRedirect(reverse('blocks'))

    def get_context_data(self, request):

        _question = Block.objects.select_related().all()
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

