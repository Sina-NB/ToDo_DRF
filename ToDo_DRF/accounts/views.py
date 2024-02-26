from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class IndexView(View):
    """
    Accounts app index view. this view accepts only 'get' method.
    """

    def get(self, request, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        if request.user.is_authenticated:
            return redirect("/")

        return render(request, "accounts/index.html")
