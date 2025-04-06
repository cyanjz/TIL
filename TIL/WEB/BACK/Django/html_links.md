# django html links

## html a tag 작성법
특정 a tag에 html 파일의 경로를 넣으면 정상적으로 동작하지 않는다.

다음의 단계를 따라 링크를 작성한다.
1. urls.py 수정
    urls 파일의 urlpatterns를 수정한다.

    name에는 참조할 이름을 넣어준다.
    ```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('todos/', views.index, name="index"),
        path('create_todo/', views.create_todo, name="create_todo"),
    ]
    ```

2. html 태그 수정
    html의 a 태그의 href를 다음과 같이 작성한다.

    `"{% url 'view_name' %}"`

    예시
    ```html
    <a href="{% url 'create_todo' %}">할 일 추가</a>
    ```