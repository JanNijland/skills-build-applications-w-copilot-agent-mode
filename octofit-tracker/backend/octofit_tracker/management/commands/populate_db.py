from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Verwijder bestaande data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superhelden')
        dc = Team.objects.create(name='DC', description='DC superhelden')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spider-Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Pushups voor kracht')
        running = Workout.objects.create(name='Running', description='Hardlopen voor uithoudingsvermogen')
        pushups.suggested_for.set([ironman, batman])
        running.suggested_for.set([spiderman, superman])

        # Activities
        Activity.objects.create(user=ironman, activity_type='pushup', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, activity_type='run', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='pushup', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, activity_type='run', duration=60, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=spiderman, score=90)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata!'))
