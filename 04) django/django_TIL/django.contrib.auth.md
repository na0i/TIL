#### django.contrib.auth

장고는 로그인 · 로그아웃을 쉽게 구현할 수 있도록 django.contrib.auth 앱을 제공한다. 이 앱은 장고 프로젝트 생성 시 settings.py에 자동으로 추가된다.

```python
#settings.py 파일의 installed_apps

INSTALLED_APPS = [
    (... 생략 ...)
    'django.contrib.auth',
    (... 생략 ...)
]
```



custom user model 만드는 방법

settings.py에 추가

```
AUTH_USER_MODEL = 'myapp.MyUser'
```







##### class

models.User

그러니까 class User는 django/contrib/auth/models.py 의 class User

##### fields

username, first_name, last_name, email 등이 있다



##### attributes

- **is_authenticated**

  This is a way to tell if the user has been authenticated.

- **is_anonymous**

  This is a way of differentiating `User`and `AnonymousUser` objects. Generally, you should prefer using [`is_authenticated`](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated) to this attribute.



##### methods

- **get_username()** : Returns the username for the user



##### settings.py

Some kinds of projects may have authentication requirements for which Django’s built-in [`User`](https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User) model is not always appropriate. For instance, on some sites it makes more sense to use an email address as your identification token instead of a username.

Django allows you to override the default user model by providing a value for the [`AUTH_USER_MODEL`](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-AUTH_USER_MODEL) setting that references a custom model:

```
AUTH_USER_MODEL = 'myapp.MyUser'
```

This dotted pair describes the name of the Django app (which must be in your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-INSTALLED_APPS)), and the name of the Django model that you wish to use as your user model.





```python
def get_user_model():
    """
    Return the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.AUTH_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )


def get_user(request):
    """
    Return the user model instance associated with the given request session.
    If no user is retrieved, return an instance of `AnonymousUser`.
    """
    from .models import AnonymousUser
    user = None
    try:
        user_id = _get_user_session_key(request)
        backend_path = request.session[BACKEND_SESSION_KEY]
    except KeyError:
        pass
    else:
        if backend_path in settings.AUTHENTICATION_BACKENDS:
            backend = load_backend(backend_path)
            user = backend.get_user(user_id)
            # Verify the session
            if hasattr(user, 'get_session_auth_hash'):
                session_hash = request.session.get(HASH_SESSION_KEY)
                session_hash_verified = session_hash and constant_time_compare(
                    session_hash,
                    user.get_session_auth_hash()
                )
                if not session_hash_verified:
                    request.session.flush()
                    user = None

    return user or AnonymousUser()

```

