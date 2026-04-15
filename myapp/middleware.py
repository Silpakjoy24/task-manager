
#dos injection
import time
# from datetime import time
from django.http import HttpResponse
from django.shortcuts import redirect

blacklisted_ips = set()
request_logs = {}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class IPBlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        if ip in blacklisted_ips:
            return HttpResponse("You are blocked (IP Blacklisted).", status=403)
        return self.get_response(request)

class RateLimitMiddleware:
    THRESHOLD = 20
    WINDOW = 60  # seconds

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        now = time.time()

        logs = request_logs.get(ip, [])
        logs = [t for t in logs if now - t < self.WINDOW]
        logs.append(now)
        request_logs[ip] = logs

        count = len(logs)

        if 10 < count <= 20:
            pass
            time.sleep(1)  # Throttling delay

        if count > self.THRESHOLD:
            blacklisted_ips.add(ip)
            return redirect('http://google.com')
            # return HttpResponse("Too many requests, IP blocked!", status=403)

        return self.get_response(request)
