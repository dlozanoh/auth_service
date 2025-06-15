import redis
import os
import time
from jose import jwt

r = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True)

def add_to_blacklist(token: str):
    try:
        payload = jwt.get_unverified_claims(token)
        exp = payload.get("exp")
        ttl = exp - int(time.time())
        r.setex(token, ttl, "blacklisted")
    except Exception:
        pass

def is_blacklisted(token: str):
    return r.get(token) is not None
