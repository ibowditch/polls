from django.core.management.base import BaseCommand
from tenants.models import Client, Domain

class Command(BaseCommand):

    def handle(self, *args, **options):

        for tn in ['kuring-gai', 'killara', 'hkops', 'westleigh']:

            try:
                tnfound = Client.objects.filter(schema_name=tn).exists()
                if not tnfound:
                #     self.stdout.write(self.style.SUCCESS('Public tenant exists '))
                # else:
                # TODO change for public client on bushfire
                    ptenant = Client(schema_name=tn, name=tn, paid_until='2012-12-05', on_trial=False)
                    ptenant.save()
                    # pdomain = Domain(domain='toodoo.com', tenant=ptenant, is_primary=True)
                    pdomain = Domain(domain=tn+'.polls-dev.ap-southeast-2.elasticbeanstalk.com', tenant=ptenant, is_primary=True)
                    pdomain.save()
                    # self.stdout.write(self.style.SUCCESS('Successfully created public tenant '))
            except:
                pass
                # self.stdout.write(self.style.SUCCESS('public tenant exception '))
