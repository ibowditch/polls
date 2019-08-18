from django_mailbox.signals import message_received
from django.dispatch import receiver

@receiver(message_received)
def firecall(sender, message, **args):
    print("I just received a message titled %s from a mailbox named %s" % (message.subject, message.mailbox.name, ))
