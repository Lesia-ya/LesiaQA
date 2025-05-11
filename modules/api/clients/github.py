import requests


class GitHub:
    
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/defunkt')
        body = r.json()

        return body

    def get_non_exist_user(self)
        r = request.get(f'https://api.github.com/users/butenkosergii')
        body = r.json()
        
        return body 
