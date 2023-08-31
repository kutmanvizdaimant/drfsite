from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from women.models import Women
import io


class WomenModel:
    def init(self, title, content, is_published):
        self.title = title
        self.content = content
        self.is_published = is_published


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = [
            "title",
            "content",
            "cat",
            'photo',
            "user",
        ]
    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance

def encode():
    model = WomenModel("Ainazik Paizullaeva", "Ноутбук алды", True)
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


def decode():
    decode = io.BytesIO(b'{"title":"Ainazik Paizullaeva","content":"\xd0\x9d\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba \xd0\xb0\xd0\xbb\xd0\xb4\xd1\x8b","is_published":true}')
    data = JSONParser().parse(decode)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)


# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = [
#             'id',
#             'title',
#             'content',
#         ]
