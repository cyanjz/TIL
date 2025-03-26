# Model
## 개요
Django에서 Model은 DB와의 상호작용을 담당한다. 이때, 전체적인 workflow는 하나의 DB에 대해서만 작업하도록 하여 db별 rollback을 가능하게 한다.

`app_name/models.py` > `python manage.py makemigrations` > `python manage.py migrate`

## 기본 작업 과정
### 1. models.py
models.py에서 설계도를 어떻게 만들지를 작성한다.

```python
class TableName(models.Model):
    col1 = models.CharField(max_length=10)
    col2 = modles.TextField()
    col3 = models.DateTimeField(auto_now_add=True)
    col4 = models.DateTimeField(auto_now=True)
```

1. TableName : 어떤 table을 만들지 명시
2. models.Field : 특정 col(field)가 어떤 제약 조건을 가지는지 명시.
    - col1은 CharField로 짧은 길이의 string을 저장하는 field
    - col2는 TextField로 긴 길이의 string을 저장하는 field
    - col3는 날짜 시각을 저장하는 field
        - auto_now_add는 추가할 때 현재 시각을 넣는다. (UDT 기준)
        - auto_now는 값을 변경하거나 삭제할 때 현재 시각을 넣는다.

이후 `python manage.py makemigrations`를 실행하여 app/migrations/***.py 파일을 형성하여 migration을 진행하는 python 파일을 만들기.

저장된 migrations의 파일은 DB rollback에 사용될 수 있다.

### 2. migrations

만들어진 migrations의 파일들을 바탕으로 DB를 실제로 만드는 과정.

```bash
python manage.py migrate
```


## 그 외 유용한 커맨드
```bash
python manage.py showmigrations
python manage.py sqlmigrate app_name migrate_number
```

#### 1. showmigrations
지금까지 수행한 migrations를 보여준다. \[X\] 표시는 migrate가 완료되었음을 표시.

```bash
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
articles
 [X] 0001_initial
 [X] 0002_article_created_at_article_updated_at
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
```

#### 2. sqlmigrate
수행한 migration의 sql문을 표시.

아래는 `python manage.py sqlmigrate articles 0001`의 실행 결과.

```sql
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL);
COMMIT;
```