from django.shortcuts import redirect
from django.contrib import messages


class AnonymousRequiredMixin:
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            messages.info(request, 'You are already logged in!')

            return redirect('index')

        return super().dispatch(request, *args, **kwargs)
