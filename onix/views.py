# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse
from django.db.models import F, Count
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from braces.views import LoginRequiredMixin
from onix.models import Question, Unity, Result


class HomeTemplateView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Unity


class QuestionTemplateView(LoginRequiredMixin, View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        lesson_id = args[0]
        question_id = args[1]
        cxt = self.get_context_data(request, lesson_id, question_id)
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        lesson_id = args[0]
        question_id = args[1]
        self.get_context_data(request, lesson_id, question_id)
        req = request.POST
        answer = req.get('answer')
        if request.user.is_authenticated() and answer:
            result = Result.objects.get_or_create(user=request.user, lesson_id=lesson_id)
            if self.question.answer_correct.id == int(answer[0]):
                result[0].correct = F('correct') + 1
            else:
                result[0].wrong = F('wrong') + 1
            result[0].save()

        if self.finish:
            return HttpResponseRedirect(reverse('results', kwargs={'lesson_id': lesson_id}))

        return HttpResponseRedirect(reverse('question', args=(lesson_id, int(question_id)+1)))

    def get_context_data(self, request, lesson_id, question_id):

        _question = Question.objects.prefetch_related().filter(lesson__id=lesson_id)[:10]
        paginator = Paginator(_question, 1)

        try:
            page = paginator.page(question_id)
        except PageNotAnInteger:
            page = paginator.page(1)
        except (EmptyPage, InvalidPage):
            page = paginator.page(paginator.num_pages)

        self.question = page.object_list[0]
        self.finish = not page.has_next()
        cxt = {
            'question': self.question,
            'answers': self.question.answers.all,
        }

        return cxt


class ResultTemplateView(LoginRequiredMixin, View):
    template_name = 'results.html'
    model = Result

    def get(self, request, *args, **kwargs):
        lesson_id = kwargs.pop('lesson_id')
        cxt = self.get_context_data(request, lesson_id)
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def get_context_data(self, request, lesson_id):
        user = request.user
        result = self.model.objects.filter(user_id=user.id, lesson_id=lesson_id).latest('finished_at').annotate(correct=Count('correct'))
        return {'results': [result], 'lesson': result.lesson}
