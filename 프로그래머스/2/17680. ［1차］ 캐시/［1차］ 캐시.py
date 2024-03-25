def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        i = i.lower()
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(i)
            answer += 5
            
    return answer