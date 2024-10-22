from django.contrib.auth.models import User

class CreateUser:
    def __init__(self, username: str, email: str, password: str, first_name: str, last_name: str):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


    def create_user_padrao(self):
        userp = User.objects.create_user(self.username, self.email, self.password)
        userp.first_name = self.first_name
        userp.last_name = self.last_name
        userp.save()

        print('USUÁRIO PADRÃO CRIADO COM SUCESSO!')


    def create_user_super(self):
        users = User.objects.create_superuser (self.username, self.email, self.password)
        users.first_name = self.first_name
        users.last_name = self.last_name
        users.save()

        print('USUÁRIO SUPER CRIADO COM SUCESSO!')