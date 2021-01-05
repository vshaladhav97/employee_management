from rest_framework import serializers
from .models import Employees, Documents, AddressDetails, EmployeeStatus, DocumentVersions, EmployeeDocument, DocumentFolder, Roles, Album, Musician




class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'username', 'date_of_birth', 'gender', 'email_address', 'contact_number', 'deleted','addressdetails')


class AddressDetailsSerializer(serializers.ModelSerializer):
    employees = EmployeesSerializer(many=True)

    class Meta:
        model = AddressDetails
        fields = ("id", "address_line_1", "address_line_2", "city", "country", "pincode","employees")
        
    def create(self, validated_data):
        employees_data = validated_data.pop('employees')
        addressdetails = AddressDetails.objects.create(**validated_data)
        for employee_data in employees_data:
            Employees.objects.create(addressdetails=addressdetails, **employee_data)
        return addressdetails



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

        
class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

    def create(self, validated_data):
        albums_data = validated_data.pop('album_musician')
        musician = Musician.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance