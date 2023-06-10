from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(name = "Mohot",email = "mohot@gmail.com",
        is_staff = True,
        is_superuser = True,
        phone = '01765045048',
        gender = 'Male',
        
        )
        user.set_password("mohot")
        user.save()
        dependencies = [
       
    ]
    operations = [
       migrations.RunPython(seed_data), 
    ]
