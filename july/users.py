users = {
    "Alice": {"reading", "hiking", "music"},
    "Bob": {"music", "gaming", "hiking"},
    "Charlie": {"cooking", "reading"},
    "David": {"music", "hiking"}
}

def common_interest(users):

    names = list(users.keys())
    result = []

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            user1 = names[i]
            user2 = names[j]
            user1_interests = users[user1]
            user2_interests = users[user2]

            common = user1_interests & user2_interests

            if len(common) >= 2:
                result.append((user1, user2))

    return result

print(common_interest(users))