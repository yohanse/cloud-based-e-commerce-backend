import pymysql
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Drops the entire database (use with EXTREME caution)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.ERROR('DROPPING THE ENTIRE DATABASE WILL RESULT IN IRRECOVERABLE DATA LOSS!'))
        self.stdout.write(self.style.ERROR('PROCEED ONLY IF YOU ARE ABSOLUTELY CERTAIN AND HAVE BACKUPS.'))
        self.stdout.write(self.style.SUCCESS('Starting database drop process...'))

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        port = 3306

        con = None
        try:
            port = int(port)
            con = pymysql.connect(host=host, user=user, password=password, port=port) #connect without database
            cur = con.cursor()

            # Drop the database
            cur.execute(f"DROP DATABASE IF EXISTS {dbname};")

            con.commit()
            cur.close()
            self.stdout.write(self.style.SUCCESS(f'Database "{dbname}" dropped successfully.'))

        except pymysql.MySQLError as e:
            self.stdout.write(self.style.ERROR(f'Error dropping database: {e}'))
            raise CommandError(f'Failed to drop database: {e}')
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Invalid port value: {e}'))
            raise CommandError(f'Invalid port value: {e}')
        finally:
            if con:
                con.close()

        self.stdout.write(self.style.SUCCESS('Database drop process completed.'))