# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models

class ClubEvent(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.CharField(max_length=600)
    event_location = models.CharField(max_length=200)
    event_date = models.DateTimeField('event date')
    event_duration_min = models.IntegerField(default=0)
    event_cost = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.event_title
