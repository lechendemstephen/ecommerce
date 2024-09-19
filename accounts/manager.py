from django.contrib.auth.models import BaseUserManager # type: ignore



class UserManager(BaseUserManager): 
    def create_user(self, first_name, last_name, email, username, password=None): 
        if not email: 
            raise ValueError('email field must not be None')
        if not username: 
            raise ValueError('username must not be empty')
        user = self.model(
            email = self.normalize_email(email), 
            first_name = first_name, 
            last_name = last_name
        )
        user.set_password(password)
        user.save(using = self.db)

        return user 
    
    def create_superuser(self, first_name, last_name, email, username, password): 
        user = self.create_user(
            first_name= first_name, 
            last_name= last_name, 
            email = self.normalize_email(email),
            username= username, 
            password = password
        )

        user.is_active = True
        user.is_staff = True 
        user.is_admin = True 
        user.superuser = True 
        user.save(using=self.db)

        return True 