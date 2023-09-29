from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == "GET":
            return True

        # Ми виконуємо аутентифікацію по ключу для всіх методів окрім GET
        return super().is_authenticated(request, **kwargs)
