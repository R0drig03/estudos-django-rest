from usuarios.createuser import CreateUser
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


nome_usuario_new = 'admin'
email_usuario_new = 'rodrigo.carmo@ajcred.com.br'
senha_usuario_new = 'admin'
primeiro_nome_usuario_new = 'Rodrigo'
ultimo_nome_usuario_new = 'Carmo'

create_user = CreateUser(
            nome_usuario_new, 
            email_usuario_new, 
            senha_usuario_new, 
            primeiro_nome_usuario_new, 
            ultimo_nome_usuario_new
        )

create_user.create_user_super()


