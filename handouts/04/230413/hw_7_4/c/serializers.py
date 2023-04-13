# c- serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    __(c)__ = serializers.IntegerField(
        __(a)__='__(b)__',
        read_only=True,
    )

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', '__(c)__',)