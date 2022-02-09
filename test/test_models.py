from rest_framework.test import APITestCase
from authentication.models import MyUser


class TestModel(APITestCase):
    
    def test_create_user(self):
        user = MyUser.objects.create_user('mukiibi', 'mukiibijoseph@gmail.com', '12345678@')
        self.assertIsInstance(user, MyUser)
        self.assertEqual(user.username, 'mukiibi')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(user.email, 'mukiibijoseph@gmail.com')
    
    def test_create_super_user(self):
        user = MyUser.objects.create_superuser('mukiibi', 'mukiibijoseph@gmail.com', '12345678@')
        self.assertIsInstance(user, MyUser)
        self.assertEqual(user.username, 'mukiibi')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, 'mukiibijoseph@gmail.com')
            
    
    def test_raises_error_when_no_username_is_supplied(self):
        
        self.assertRaises(ValueError, MyUser.objects.create_superuser,username='', email= 'mukiibi@gmail.com', password='12345678@')  
        self.assertRaisesMessage(ValueError,'The given username must be set' )
        
        
        
    def test_raises_error_wuth_when_username_is_supplied(self):        
        with self.assertRaisesMessage(ValueError,'The given username must be set' ):
         MyUser.objects.create_superuser(username='', email= 'hello@gamil.com', password='12345678@')
    
    
     
    def test_raises_error_when_no_email_is_supplied(self):
        
        self.assertRaises(ValueError, MyUser.objects.create_superuser,username='kali', email= '', password='12345678@')  
        self.assertRaisesMessage(ValueError,'The given email must be set' )
        
        
        
    def test_raises_error_wuth_when_eamil_is_supplied(self):        
        with self.assertRaisesMessage(ValueError,'The given email must be set' ):
         MyUser.objects.create_superuser(username='jose', email= '', password='12345678@')
         
         
         
         
        #  superuserr
        
        
    def test_create_super_user_with_superuser_stauts_is_staf(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
         MyUser.objects.create_superuser(username='jose', email= 'a@gmail.com', password='12345678@', is_staff=False)
         
        
        
    def test_create_super_user_with_superuser_stauts_is_superuser(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            MyUser.objects.create_superuser(username='jose', email= 'a@gmail.com', password='12345678@', is_superuser=False)
         