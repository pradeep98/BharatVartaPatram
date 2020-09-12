from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password','password2' ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, args):
        if User.objects.filter(email=args['email']).exists():
            raise serializers.ValidationError({'email',('email already registered!')})
        
        password = args['password']
        password2 = args['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Password doesn\'t match!'})
        #args['password'] = make_password(args.get('password'))
        #args['password2'] = make_password(args.get('password2'))

        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(email=validated_data['email'], username=validated_data['username'], password=validated_data['password'])
        user.save()
        Profile.objects.create(user=user)
        return user