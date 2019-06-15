"""
TODO:
- tutorial 3
- make timezone stuff work / read more about it
- middleware: read about + figure out where it should go in the file system/ how to hook it up
- read: Cross Site Request Forgeries
- live debugging (in chrome or in pycharm..?)
- race conditions: https://docs.djangoproject.com/en/2.2/ref/models/expressions/#avoiding-race-conditions-using-f
- Selenium for html testing in browser (django has LiveServerTestCase to support Selenium and similar frameworks)
- code coverage in coverage.py
"""

"""
TESTING TODO:
We ought to add a similar get_queryset method to ResultsView and create a new test class for that view. It’ll be very 
similar to what we have just created; in fact there will be a lot of repetition.

We could also improve our application in other ways, adding tests along the way. For example, 
it’s silly that Questions can be published on the site that have no Choices. So, our views could check for this, 
and exclude such Questions. Our tests would create a Question without Choices and then test that it’s not published, 
as well as create a similar Question with Choices, and test that it is published.

Perhaps logged-in admin users should be allowed to see unpublished Questions, but not ordinary visitors. 
Again: whatever needs to be added to the software to accomplish this should be accompanied by a test, 
whether you write the test first and then make the code pass the test, or work out the logic in your code first 
and then write a test to prove it.

At a certain point you are bound to look at your tests and wonder whether your code is suffering from test bloat,
which brings us to:
"""