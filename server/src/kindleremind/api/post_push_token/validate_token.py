def validate_push_token(token):
    if type(token) != str or len(token.strip()) == 0:
        raise Exception('Invalid push token')
