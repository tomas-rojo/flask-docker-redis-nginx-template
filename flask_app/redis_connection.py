import redis
r = redis.Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)

