import pymysql
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates the initial database (use with caution)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Database creation should ideally be an infrastructure task.'))
        self.stdout.write(self.style.SUCCESS('Starting db creation'))

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        port = 3306

        con = None
        try:
            port = int(port)
            con = pymysql.connect(host=host, user=user, password=password, port=port)
            cur = con.cursor()
            cur.execute(f"CREATE DATABASE {dbname}")
            con.commit()
            cur.close()
            self.stdout.write(self.style.SUCCESS('Database created successfully'))

        except pymysql.MySQLError as e:
            self.stdout.write(self.style.ERROR(f'Error creating database: {e}'))
            raise CommandError(f'Failed to create database: {e}')
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Invalid port value: {e}'))
            raise CommandError(f'Invalid port value: {e}')
        finally:
            if con:
                con.close() #only close if connection exists.

        self.stdout.write(self.style.SUCCESS('All Done'))