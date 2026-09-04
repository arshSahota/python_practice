# users = [
#     {"username": "alice", "role": "Admin", "active": True},
#     {"username": "bob", "role": "Viewer", "active": True},
#     {"username": "charlie", "role": "Admin", "active": False},
#     {"username": "david", "role": "Operator", "active": True},
# ]

# def analyze_users(users):

#     valid_roles = ["Admin", "Operator", "Viewer"]
#     authorized = []
#     unauthorized = []

#     for user in users:
#         reasons = []
#         if user["role"] in valid_roles and user["active"] is True:
#             authorized.append({
#                 "username": user["username"],
#             })
#         elif user["role"] not in valid_roles and user["active"] is True:
#             reasons.append("INVALID_ROLE")
#             unauthorized.append({
#                 "username": user["username"],
#                 "reason": reasons
#             })
#         elif user["role"] not in valid_roles and user["active"] is False:
#             reasons.append("INVALID_ROLE")
#             reasons.append("INACTIVE")
#             unauthorized.append({
#                 "username": user["username"],
#                 "reason": reasons
#             })
#         else:
#             reasons.append("INACTIVE")
#             unauthorized.append({
#                 "username": user["username"],
#                 "reason": reasons
                
#             })

#     return {
#         "authorized": authorized,
#         "unauthorized": unauthorized,
#         "authorized_count": len(authorized),
#         "unauthorized_count": len(unauthorized)
#     }

# print(analyze_users(users))

# def test_authorized_user():

#     user = {
#         "username": "Arshdeep",
#         "role": "Admin",
#         "active": True
#     }
#     result = analyze_users([user])

#     assert result["authorized"] == [{"username": "Arshdeep"}]

# def test_inactive_user():
#     user = {
#         "username": "Gursharan",
#         "role": "Admin",
#         "active": False
#     }
#     result = analyze_users([user])

#     assert result["unauthorized"] == [{"username": "Gursharan", "reason": ["INACTIVE"]}]

# def test_invalid_role():
#     user = {
#         "username": "Harman",
#         "role": "Manager",
#         "active": True
#     }
#     result = analyze_users([user])

#     assert result["unauthorized"] == [{"username": "Harman", "reason": ["INVALID_ROLE"]}]

# def test_invalid_role_inactve_user():
#     user = {
#         "username": "Quang",
#         "role": "Manager",
#         "active": False
#     }
#     result = analyze_users([user])

#     assert result["unauthorized"] == [{"username": "Quang", "reason": ["INVALID_ROLE", "INACTIVE"]}]