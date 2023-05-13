def solution(today, terms, privacies):
    answer = []
    terms_dict = dict();
    
    for term in terms:
        terms_dict[term.split()[0]] = int(term.split()[1])
    
    today = list(map(int, today.split('.')))
    for i, privacy in enumerate(privacies):
        p_date, term = privacy.split()
        p_date = list(map(int, p_date.split('.')))
        p_date[1] += terms_dict[term]
        p_date[2] = p_date[2] - 1 if p_date[2] - 1 > 0 else 28
        p_date[1] = p_date[1] - 1 if p_date[2] == 28 else p_date[1]
        p_date[0] += (p_date[1] // 12) - 1 if p_date[1] % 12 == 0 else p_date[1] // 12
        p_date[1] = p_date[1] % 12 if p_date[1] > 12 else p_date[1]
        p_date[1] = 12 if p_date[1] == 0 else p_date[1]
        print(p_date)
        if today[0] > p_date[0] or (today[0] == p_date[0] and today[1] > p_date[1]) or ((today[0], today[1]) ==  (p_date[0], p_date[1]) and today[2] > p_date[2]):
            answer.append(i + 1)
    return answer

