# Style Guide

## settings.py > INSTALLED_APPS
설치된 앱은 다음 순서로 작성한다.

1. user defined apps
2. 3rd party libraries
3. built-in apps

## .gitignore
web 개발을 할 때 DB는 공용 저장소에 올리지 않는다.

1. 보안상의 문제.
2. 용량의 문제.

대신, migrate 이력인 migrations 폴더의 코드는 업로드하여 동일한 schema의 DB를 구축할 수 있도록 한다.
