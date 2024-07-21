import time
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start=time.time()
        response = get_response(request)
        print("Hello")
        end=time.time()
        print(f"Total time for request and response is {end-start}")
        # Code to be executed for each request/response after
        # the view is called.
        return response

    return middleware