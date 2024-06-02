def generate_hashtag(s):
    if len(s)> 140 or len(s)<0:
        return False
    removed="#" +"".join(s.split())
    return removed







