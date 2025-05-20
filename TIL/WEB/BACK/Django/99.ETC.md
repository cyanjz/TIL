# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'KR'

USE_I18N = True
	# i18n은 "internationalization"의 약자로, 소프트웨어를 여러 언어와 문화권에 맞게 지원하는 기술을 의미
    # False로 설정하면 번역기능이 동작하지 않는다.

USE_TZ = False
    # False로 설정하면 TIME_ZONE 변수에 할당된 TZ를 사용하지 않는다.
    # 즉, 로컬 시간대를 사용하여 DB 관리등을 수행한다.

    1. urls.py에 views를 import 할때 어떤식으로 해주는게 좋나?
import book_main_page.views
이게 좋아보이는데?

2. views.py에 name 인자를 전달해야 html에서 a link를 작성할 때 참조 가능한 것 같다.
이건 html의 a link를 클릭하면 views의 함수를 호출하는 걸로 이해해도 괜찮은지?
그러니까 urls.py -> views -> response를 다시 밟는 과정.