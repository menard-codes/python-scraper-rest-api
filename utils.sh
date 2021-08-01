
source venv/bin/activate

python3 -m fetch_data

git add .
git commit -m 'new scrapped data'

git push heroku master

echo "\nCronjob run at:" >> .cronjob_logger.txt
date >> .cronjob_logger.txt
