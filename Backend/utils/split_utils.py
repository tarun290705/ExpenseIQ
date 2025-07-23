def equally_split(amount, users):
    share = round(amount / len(users), 2)
    splits = []
    for user in users:
        splits.append({"user_id" : user, "amount" : share})
    return splits

def percentage_split(amount, percentages):
    splits = []
    for user_id, percent in percentages.items():
        part = round((percent/100)*amount, 2)
        splits.append({"user_id" : user_id, "amount" : part})
    return splits

def exact_split(amount, contributions):
    return [{"user_id" : uid, "amount" : amt} for uid, amt in contributions.items()]