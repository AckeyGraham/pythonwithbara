# Allow access only if the user is logged in
#or they area a guest
# but they must not be banned user.

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)

print((is_logged_in or is_guest) and not is_banned)