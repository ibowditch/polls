from django.core.management.base import BaseCommand
from tenants.models import Client, Domain

class Command(BaseCommand):

    def handle(self, *args, **options):

        try:
            pubfound = Client.objects.filter(schema_name="public").exists()
            if not pubfound:
            #     self.stdout.write(self.style.SUCCESS('Public tenant exists '))
            # else:
            # TODO change for public client on bushfire
                ptenant = Client(schema_name='public', name='Schemas Inc.', paid_until='2012-12-05', on_trial=False)
                ptenant.save()
                # pdomain = Domain(domain='toodoo.com', tenant=ptenant, is_primary=True)
                pdomain = Domain(domain='polls-dev.ap-southeast-2.elasticbeanstalk.com', tenant=ptenant, is_primary=True)
                pdomain.save()
                # self.stdout.write(self.style.SUCCESS('Successfully created public tenant '))
        except:
            pass
            # self.stdout.write(self.style.SUCCESS('public tenant exception '))
