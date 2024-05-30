from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/portfolio.html'
    extra_context = {}
    login_url = 'login'