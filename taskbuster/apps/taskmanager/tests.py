from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from . import models

# test that I wrote good regex for custom validation of color attribute
class TestProjectModel(TestCase):

    # creates user instance and related profile, saves in self for later
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(
            username="taskbuster", password="django-tutorial")
        self.profile = self.user.profile
 
    # excecuted at end of each test, and deletes user instance and all
    # related instances (profile, and project)
    def tearDown(self):
        self.user.delete()
 
    # tests different inputs of color attribute
    def test_validation_color(self):
        # This first project should use the default value, #fff
        project = models.Project(
            user=self.profile,
            name="TaskManager"
            )
        self.assertTrue(project.color == "#fff")
        # Validation shouldn't raise an Error
        project.full_clean()
 
        # Good color inputs (without Errors):
        for color in ["#1cA", "#1256aB"]:
            project.color = color
            project.full_clean()
 
        # Bad color inputs raise ValidationError
        for color in ["1cA", "1256aB", "#1", "#12", "#1234",
                      "#12345", "#1234567"]:
            with self.assertRaises(
                    ValidationError,
                    msg="%s didn't raise a ValidationError" % color):
                project.color = color
                project.full_clean()