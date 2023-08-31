from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women, Category
from women.serializers import WomenSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
class WomenViewSets(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        if not pk:
            return Women.objects.all()[:7]
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all().values()
        return Response({"cats": cats})

# class WomenListAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenListAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenCreateAPIView(generics.CreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenUpdateAPIView(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenDestroyAPIView(generics.DestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer










    # def get(self, request):
    #     posts = Women.objects.all().values()
    #     return Response({'posts': posts})
    #
    # def post(self, request):
    #     serializer = WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     # post_new = Women.objects.create(
    #         # title= request.data['title'],
    #         # content= request.data['content'],
    #         # is_published=request.data['is_published']
    #
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({"error": "Method put not allowed"})
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "objects does not exist"})
    #     serializer = WomenSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})
    #
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method delete not allowed"})
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "objects does not exist"})
    #
    #     instance.delete()
    #     return Response({"message": "seccessfully deleted"})