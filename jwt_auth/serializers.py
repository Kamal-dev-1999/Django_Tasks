from rest_framework import serializers
from .models import MyUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True,'required':True}  #this means that the password is only for write purposes and not for showing to the user
        }
    #we wwill hash the password so that we dont see the poss as it is but a hash value
    def create(self, validated_data):
        password=validated_data.pop('password',None)  # Extract (pop)the 'password' from the validated_data dictionary, removing it from the dictionary if it exists. The pop method removes the password key from the dictionary and returns its value. If the key doesn't exist, it returns None.
        
        instance=self.Meta.model(**validated_data)  # Create an instance of the user model (MyUser) with the remaining validated data (excluding the password).  
        #The **validated_data syntax unpacks the dictionary into keyword arguments.
        
        
        if password is not None: # If a password was provided, set the password for the user instance. This hashes the password.
            
            
            instance.set_password(password) #The block if password is not None: instance.set_password(password) checks if a password was provided. If it was, it sets the user's password using the set_password method, which handles hashing the password.
        instance.save()
        return instance