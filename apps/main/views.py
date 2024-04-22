from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/index.html'

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)


class ContactView(TemplateView):
    template_name = 'main/contact.html'


class ForumView(TemplateView):
    template_name = 'main/forums.html'
