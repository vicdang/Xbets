# Xbets
Football betting web app, built with django/bootstrap/jquery

## Requirement:
 - Python 2.7.12 or above
 - Django 1.11 or above
 
## Guide line:
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser
 - python manage.py runserver

## User Features:
 - Post prop bet with description, bet amount, quantity allowed, and an expiration date
 - View / remove your open prop bets. View your active (accepted) prop bets
 - View / accept other people's open prop bets
 - View active prop bets across all users
 - View completed prop bets across all users
 - Receive email when your prop bet accepted
 - Receive daily digest email when new prop bets are added
 - User profile settings
 - Stats! (user and global)

## Admin Features:
 - Set win/loss/tie for open or expired prop bets (only those that have at least one accepted bet)
 - Undo win/loss/tie from completed bet
 - Regular django admin site stuff
 
## Running server on AWS
 - http://13.212.24.195

## Upcomming Features:
 - Add CSRF Token:
   + https://docs.djangoproject.com/en/2.2/ref/csrf/
 - Map page - show all teams of a specific league, by table, and show match map
   + matches
   + venues
   + times, stages, match result
 - Ranking page
 - Rule page
 - Matches page
 - Genegrate group ID for registration.
 - Customize admin view to show data row in detailed.
 
## Related template:
https://betting.team/en/football
