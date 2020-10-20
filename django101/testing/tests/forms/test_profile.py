from django.test import TestCase

from testing.forms.profile import ProfileForm
from testing.models import Profile


class ProfileFormTests(TestCase):
    def test_saveProfileForm_whenValidEgn_shouldBeValid(self):
        name = 'Doncho 2'
        age = 19
        egn = '1234567890'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertTrue(form.is_valid())

    def test_saveProfileForm_whenEgnContainsLetter_shouldBeInvalid(self):
        name = 'Doncho'
        age = 19
        egn = '12345678a0'

        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut9_shouldBeInvalid(self):
        name = 'Doncho'
        age = 19
        egn = '123245685'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut11_shouldBeInvalid(self):
        name = 'Doncho'
        age = 19
        egn = '12345678011'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })
        self.assertFalse(form.is_valid())
