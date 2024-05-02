from rest_framework import serializers

from watchlist_app.models import Movie



def name_lenght(value):
    "validators"
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_lenght]) # for validators
    # name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name )
        instance.description = validated_data.get('description',instance.name )
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    # def validate_name(self, value):
    #     """below is field level validation"""
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     else:
    #         return value

    def validate(self, data):
        """below is Object level validation"""
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")

        return data