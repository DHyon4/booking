#!/bin/bash -e

cd /app/

if [ "$DJANGO_SETTINGS_MODULE" == "booking.settings.dev" ]
then
    ./scripts/wait-for-it.sh $MYSQL_HOST:$MYSQL_PORT --timeout=30 --strict -- echo "DB is up!!!1!!"
fi

# Run migrations
python manage.py migrate --noinput

# Move static assets into place
python manage.py collectstatic --noinput

# Load fixture data, but not in prod
if [ "$DJANGO_SETTINGS_MODULE" != "booking.settings.prod" ]
then
    echo "Fixturizing!!!1!"
    python manage.py loaddata fixtures/auth.user.json
fi
