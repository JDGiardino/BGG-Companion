from src.cache.AbstractCache import AbstractCache


class DummyCache(AbstractCache):
    def get(self, key):
        return

    def set(self, key, value):
        return

# What is the purpose of this Class?
    # Any instantiation of the BggCompanionApi class requires a "cache".
    # In production, a Cache object is instantiated with a flask app via the flask_caching library and set to "cache"
    # The BggCompanionApi class code assumes & expects "cache" to be this object and thus couples it with Flask library
    # We want BggCompanionApi class to not be limited to the setup of a Flask app.  Example :
        # Testing methods within the class in dev via if __name__ == "__main__":
        # Some outside caller that wants to use the bgg_companion_api but does not utilize Flask
# Thus AbstractCache class acts as a class to be inherited by other Cache classes that do not set up a Flask app
# They must inherit from this abstract class to enforce the requirement of get() and set() used in BggCompanionApi
# DummyCache can be used to instantiate BggCompanionApi & allow methods calling get/set on cache to work but do nothing
