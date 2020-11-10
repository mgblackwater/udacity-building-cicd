#clone the repository
git clone git@github.com:mgblackwater/udacity-building-cicd.git

#create virtual environment and activate
python3 -m venv .venv
source .venv/bin/activate

#install dependencies, lint and test
make all

#deploy webapp
az webapp up -n mgblackwater-udacity-building-cicd

#view logstresm
az webapp log tail