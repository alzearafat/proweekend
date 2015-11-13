from django.apps import AppConfig
import watson

class JourneyAppConfig(AppConfig):
    name = "journey"
    def ready(self):
        post = self.get_model("post")
        watson.register(post)