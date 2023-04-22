result_purchased = 0
max_subscribe = 0

def product(discounts, users, emoticons):
    if len(discounts) == len(emoticons):
        global result_purchased, max_subscribe
        subscribe = 0
        total_purchased = 0
        for user in users:
            purchased = 0
            for emoticon, discount in zip(emoticons, discounts):
                if discount >= user[0]:
                    purchased += emoticon * (100 - discount) // 100
            if purchased > user[1]:
                subscribe += 1
                purchased = 0
            total_purchased += purchased
        if max_subscribe < subscribe or (max_subscribe == subscribe and result_purchased < total_purchased):
            max_subscribe = subscribe
            result_purchased = total_purchased
        return 
    
    for d in [10, 20, 30, 40]:
        discounts.append(d)
        product(discounts, users, emoticons)
        discounts.pop()

def solution(users, emoticons):
    product([], users, emoticons)
    return [max_subscribe, result_purchased]

