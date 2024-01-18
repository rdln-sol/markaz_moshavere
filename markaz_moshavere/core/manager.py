from django.contrib.auth.base_user import BaseUserManager
class ReceptionManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, phone_number, password=None, **extra_fields):
		if not phone_number:
			raise ValueError('Phone number is required')
		reception = self.model(phone_number=phone_number, **extra_fields)
		reception.set_password(password)
		reception.save()
		return reception
	
	def create_superuser(self, phone_number, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)
		return self.create_user(phone_number, password, **extra_fields)
