from django.apps import AppConfig


class RobotsConfig(AppConfig):
    """Регистрация приложения robots."""

    verbose_name = 'роботы'
    name = 'robots'

    def ready(self) -> None:
        """Метод для запуска команд при запуске Django."""
        import robots.signals  # noqa: F401
