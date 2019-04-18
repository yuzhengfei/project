from django.shortcuts import render
def login_requied(get):
    def authenticate(self, request):
            try:
                request.session['user_id']
                request.session['role']
                return get(self, request)
            except Exception:
                return render(request, 'index.html')
    return authenticate