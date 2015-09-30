HERE=$(pwd)

pip install pelican
pelican-themes -s $HERE/themes/Colourise11
make html

# Tag the old version
docker pull rcommande/blog
docker tag -f rcommande/blog rcommande/blog:previous
docker push rcommande/blog

# Create the new image
docker build -t rcommande/blog .
docker push rcommande/blog
