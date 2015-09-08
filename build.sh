HERE=$(pwd)
pip install pelican
pelican-themes -s $HERE/themes/Colourise11
make html
docker build -t rcommande/blog .
docker push rcommande/blog
