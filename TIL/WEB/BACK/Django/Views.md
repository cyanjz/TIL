# Views
Django에서 view를 작성하는 팁에 대해 서술한다.

## HTTP request
HTTP 의 request가 POST, GET인지에 따라서 서로 다른 페이지로 redirect 또는 render하도록 코드를 작성할 수 있다.

아래 코드는 어떤 게시글을 만들때, 입력을 위한 페이지를 rendering하는 별도의 함수를 선언하지 않고 하나의 함수에서 POST인지 아닌지를 구별하여 서로 다른 반환값을 가지도록 한 코드이다.
```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)
```