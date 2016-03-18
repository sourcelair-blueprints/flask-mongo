"""
Simple model declaration.
"""
import mongoengine

mongoengine.connect(host='mongodb://mongo/demo_db')


class IPHitCounter(mongoengine.Document):
    """
    Logs the number that each IP has hit this server.
    """
    ip = mongoengine.StringField(unique=True, required=True)
    hits = mongoengine.IntField(default=0, required=True)

    @classmethod
    def get_or_create(cls, ip):
        """
        Gets an existing, or creates a new model.
        """
        try:
            return cls.objects.create(ip=ip)
        except mongoengine.errors.NotUniqueError:
            return cls.objects.get(ip=ip)
