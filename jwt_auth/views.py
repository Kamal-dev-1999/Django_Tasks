from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import permissions
from .models import MyUser
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime


class RegisterView(APIView):
    # Allow any user (authenticated or not) to access this endpoint
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        # Initialize the serializer with the data received in the request
        serializer = UserSerializers(data=data)
        # Validate the data and raise an exception if validation fails
        serializer.is_valid(raise_exception=True)
        # Save the validated data to the database
        serializer.save()
        # Return the serialized data in the response
        return Response(serializer.data)


class LoginView(APIView):
    # Allow any user (authenticated or not) to access this endpoint
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Find the user by email
        user = MyUser.objects.filter(email=email).first()

        # Raise an exception if the user does not exist
        if user is None:
            raise AuthenticationFailed("User does not exist")

        # Check if the provided password is correct
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        # Serialize the user data
        serializer = UserSerializers(user)

        # Create a payload for the JWT token with user ID, expiration time, and issued at time
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),  # Token expires in 60 minutes
            'iat': datetime.datetime.utcnow()  # Token issued at the current UTC time
        }

        # Encode the payload into a JWT token using the HS256 algorithm and a secret key
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        # Create a response object
        response = Response()
        # Set the JWT token in a cookie, making it accessible only to the backend (HTTP-only)
        response.set_cookie(key='jwt', value=token, httponly=True)
        # Include the JWT token in the response data
        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):
    # Allow any user (authenticated or not) to access this endpoint
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Get the JWT token from the request cookies
        token = request.COOKIES.get('jwt')

        # If no token is found, raise an authentication failed exception
        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            # Decode the JWT token to get the payload
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # Raise an exception if the token has expired
            raise AuthenticationFailed("Unauthenticated")
        except jwt.DecodeError:
            # Raise an exception if the token is invalid
            raise AuthenticationFailed("Invalid token")

        # Find the user by ID from the payload
        user = MyUser.objects.filter(id=payload['id']).first()
        # Serialize the user data
        serializer = UserSerializers(user)
        # Return the serialized user data in the response
        return Response(serializer.data)


#we will just send the cookie using the get method and get the details of the user 

class LogoutView(APIView):
    # Allow only authenticated users to access this endpoint
    permission_classes = [permissions.AllowAny]
#
# When you change the permission type to AllowAny, the LogoutView works because it no longer checks for authentication credentials before processing the request. This indicates that the IsAuthenticated permission is not recognizing the JWT token in the cookies as a valid authentication credential. This can happen due to several reasons:
    def post(self, request):
        # Create a response object
        response = Response()
        # Delete the JWT cookie
        response.delete_cookie('jwt')
        # Set a success message in the response data
        response.data = {
            'message': "Successfully logged out ! cookies have been deleted ! login again "
        }
        # Return the response
        return response
