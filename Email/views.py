import django
from Email.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import JsonResponse


class ReviewEmailView(FormView):
    template_name = "review.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for your review!"
        return JsonResponse(msg)
