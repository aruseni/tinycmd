from django.test import TestCase
from django.conf import settings

from tc.models import CommandString

from tc.basenencode import baseNencode

class TestCommandStringModel(TestCase):
    def setUp(self):
        self.cs = CommandString.objects.create()

    def test_string_id(self):
        """
        Tests that the string_id is added to the object correctly.
        """
        string_id = baseNencode(self.cs.id+settings.BASE_N_OFFSET, settings.BASE_N_ALPHABET)
        # Reload the object to get the string_id added by the save() method
        cs = CommandString.objects.get(id=self.cs.id)
        self.assertEqual(string_id, cs.string_id)

    def tearDown(self):
        self.cs.delete()
