class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/static/'):
            response['Cache-Control'] = 'public, max-age=31536000'
        else:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response