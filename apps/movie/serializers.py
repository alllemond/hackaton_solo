from rest_framework import serializers
from .models import Movie, MovieImage

class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
                url = " "
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = MovieImageSerializer(MovieImage.objects.filter(film=instance.id), many=True).data
        return rep
