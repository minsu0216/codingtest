def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report = list(set(report))
    
    from_ = list()
    to_ = list()
    for rp in report:
        tmp = rp.split()
        from_.append(tmp[0])
        to_.append(tmp[1])
    
    # 신고 당한 사람 dict
    d_rp = dict()
    for i in to_:
        d_rp[i] = d_rp.get(i, 0) + 1
    jungzi = [key for key, v in d_rp.items() if v >= k]
            
    # 신고한 사람 dict
    d_id = dict()
    for id in id_list:
        d_id[id] = [t for f, t in zip(from_, to_) if f == id]
                
    for i, dd in enumerate(d_id):
        answer[i] = len(set(d_id[dd]) & set(jungzi))

    
    
    return answer