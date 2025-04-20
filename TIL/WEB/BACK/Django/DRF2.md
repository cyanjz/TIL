# DRF2 - N:1
rest_framework를 사용하여 N:1 관계를 어떻게 응답하고, 저장하는지에 대한 내용.

Comment -> Referencing -> Article

Article -> Reverse referencing -> Comment

<br/>
<br/>

# Referencing

## I. Comment - CREATE
- 댓글을 생성할 때, 사용자가 댓글이 달린 게시글이 무엇인지 직접적으로 명시할 필요가 없다.
- 유효성 검사에서는 article 외래키를 제외하되, 조회 알고리즘에서는 article 외래키를 직렬화 해야한다.
    - 이 경우, `exclude`, `fields`를 변경하는 것으로는 충분하지 않다.
    - `ModelForm`의 경우에는 `exclude`, `fields`를 변경하는 것으로 충분했으나, 직렬화는 외래키에 대해서도 이뤄져야 하므로 단순히 필드를 제외하는 것으로는 충분하지 않다.
- `read_only_fields`를 `Serializer`의 `Meta` class에 작성한다.


### 1. serializers.py
```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields를 작성.
        read_only_fields = ('articles', )
```

### 2. views.py
```python
@api_view(['POST'])
def comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # .save에 article=article 형태로 필드를 지정할 수 있다.
            # 다른 필드들에 대해서도 수행 가능.
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

<br/>

## II. Comment - READ
외래키를 전달하는게 아니라, 외래키를 참조하여 해당 테이블의 속성을 전달하는 방법.

serializers.py serializer를 정의할 때, 내부에 새로운 serializer class를 정의하고 해당 class로 model의 foreign key field method를 overriding 한다.

### 1. serializers.py
```python
class CommentSeiralizer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    
    article = ArticleTitleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
```

### 2. views.py
```python
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

<br/>
<br/>

# Reverse referencing
역참조를 직렬화 하는 방법.

## I. Reverse referencing, Nested relationships
- 역참조 매니저를 overriding.

```python
class ArticleListSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content', )
    comment_set = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )
```

<br/>

## II. Aggregation function
### 1. views.py
- 아래와 같은 형식으로 작성.
- field_name : 나중에 serializers에서 함수의 반환값을 해당 필드명으로 해야함.
- 역참조 매니저 이름 : models.py에서 related_to 속성으로 지정.

```python
def ...(request, ...):
    article = article.objects.annotate(field_name=Agg_func(<역참조 매니저 이름>)).get(pk=article_pk)
```

### 2. serializers.py
- MethodField의 반환을 위한 함수 이름은 `get_<field_name>`으로 작성한다.
```python
class ArticleSerializer(serializers.ModelSerializer):
    ...
    num_comments = serializers.SerializerMethodField()
    
    def get_num_comments(self, obj):
        return obj.field_name
```