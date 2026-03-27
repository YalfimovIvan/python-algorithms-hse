import heapq

def big_politics(p: list) -> int:
    '''
    Возвращает оптимальное количество паспортов, которое нужно выдать для объединения переданных провинций
    
    :param p: список населения всех провинций
    :type p: list
    :returns: количество паспортов, которые надо будет выдать
    :rtype: int
    '''
    heapq.heapify(p)
    
    totally_passports = 0
    
    while len(p) > 1:
        first = heapq.heappop(p)
        second = heapq.heappop(p)
        
        cost = first + second
        totally_passports += cost
        
        heapq.heappush(p, cost)
    
    return totally_passports
