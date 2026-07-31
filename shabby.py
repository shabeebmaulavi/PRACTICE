from django.core.cache import cache



email = "shabeebmaulavi@gmail.com"
otp = 239485


cache.set(email + '_otp', {'email': email, 'otp': otp}, timeout=60)

cached_data = cache.get(email + '_otp')

print(cached_data)


# cache.set(email + '_otp', {'email': email, 'otp': otp}, timeout=60)
