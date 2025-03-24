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