import hashlib
def to_sha256(s):
    s1 = s.encode('utf-8')
    return hashlib.sha256(s1).hexdigest()