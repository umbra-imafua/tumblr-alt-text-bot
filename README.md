# tumblr-alt-text-bot
A bot concept to use google vision api to provide alt text from images with text in them on tumblr

TUMBLR SETUP

Uses the tumblr api
    https://www.tumblr.com/docs/en/api/v2

And pytumblr
    pip install pytumblr



GOOGLE SETUP

gcloud CLI sdk should be installed
    https://cloud.google.com/sdk/docs/install

remember to run "source ~/.bashrc" and reload the terminal after install

login with
    gcloud auth application-default login


google python libraries
    pip install google-cloud-storage
    pip install --upgrade google-cloud-storage
    pip install -U pip google-cloud-vision

Download a key json file from and put it in this directory
    https://codelabs.developers.google.com/codelabs/cloud-vision-api-python#4

