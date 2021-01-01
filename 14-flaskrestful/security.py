from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    selecteduser = User.find_by_username(username)
    if selecteduser and safe_str_cmp(selecteduser.password, password):
        return selecteduser
def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)