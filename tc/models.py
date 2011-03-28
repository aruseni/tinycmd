from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from string import digits
from basenencode import baseNencode

# Create your models here.

class CommandString(models.Model):
    command_string = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)
    user_added = models.ForeignKey(User, null=True, blank=True)
    votes = models.FloatField(default=0.0)
    # When the super() first saves the object,
    # it creates and gets an ID, but
    # it doesn't yet have a string_id
    # (so the field has blank set to True).
    # The object gets the string_id
    # after creation, as the save()
    # method next adds it.
    string_id = models.CharField(max_length=255, blank=True, editable=False)

    def save(self, only_num=False, *args, **kwargs):
        """
Check if a string_id is already set, and if it's not,
convert the object id to a base N string and then
update the string_id field with the returned value.

As an ID is generated when a new command string is saved,
it becomes possible to then change the ID generation scheme:
for the new objects and still leave the old IDs working.
        """
        super(CommandString, self).save(*args, **kwargs) # Call the "real" save() method.
        if not self.string_id:
            # TODO: Need new algorithm!!!!!!!!!!!!!!!
            string_id = baseNencode(self.id + settings.BASE_N_OFFSET, 
                                    digits if only_num else settings.BASE_N_ALPHABET)
            CommandString.objects.filter(id=self.id).update(string_id=string_id)

    def __unicode__(self):
        return self.string_id
