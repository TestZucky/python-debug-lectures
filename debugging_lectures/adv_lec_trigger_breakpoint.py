def authenticate_user(user_id):
    print(f'Authenticating {user_id}....')
    return True

def get_user_data(user_id):
    print(f'getting user id for {user_id}...')
    return {
        'name': 'john',
        'role': 'user'
    }

def process():
    user_id = 101

    if authenticate_user(user_id):
        user = get_user_data(user_id=user_id)

        print(user)


def admin_report():
    print('running admint report...')
    user = get_user_data(999)
    print(user)

process()
admin_report()