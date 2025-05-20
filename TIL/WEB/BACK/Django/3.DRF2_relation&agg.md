# DRF2 - N:1
rest_framework를 사용하여 N:1 관계를 어떻게 응답하고, 저장하는지에 대한 내용.

**핵심은 참조/역참조 필드를 serializer를 사용하여 overriding 하기!**

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

```plaintext
Comment -> Referencing -> Article

Article -> Reverse referencing -> Comment
```

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
# CREATE comment
@api_view(['POST'])
def comment_create(request, article_pk):
    # 어떤 게시글에 작성되는 것인지 확인.
    article = Article.objects.get(pk=article_pk)
    # 사용자가 보낸 댓글 데이터를 활용.
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사
    if serializer.is_valid(raise_exception=True):
        # 추가 데이터를 save 메서드의 인자로 작성.
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
- 특별한 사항 없음.

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
    article = article.objects.annotate(field_name=Agg_func(<대상 모델명>)).get(pk=article_pk)
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