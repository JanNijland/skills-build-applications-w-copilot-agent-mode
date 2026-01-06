from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superhelden')
        self.user = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Pushups voor kracht')
        self.activity = Activity.objects.create(user=self.user, activity_type='pushup', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')
    def test_activity_user(self):
        self.assertEqual(self.activity.user.email, 'ironman@marvel.com')
    def test_leaderboard_score(self):
        self.assertEqual(self.leaderboard.score, 100)
