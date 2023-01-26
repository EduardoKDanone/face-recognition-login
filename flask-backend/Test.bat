set IMAGENAME=face-reco-test
docker build -t %IMAGENAME% --no-cache -f dockerfile.test .
docker run --name runtime-%IMAGENAME% %IMAGENAME%:latest python -m unittest discover tests
docker rm runtime-%IMAGENAME%
docker rmi %IMAGENAME%:latest