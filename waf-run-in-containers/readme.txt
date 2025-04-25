in the code ensure the ftp related functions are enabled.
launch the container with ftp server using file ftp_server_image.txt
if any code changes in git hub, create image again using "Df-waf-2stage-build-deploy-root.txt"

launch the waf running containers many if require like this

docker run -d --rm -e FTP_HOST=172.17.0.2 -e LOG_LEVEL=warn waf2st
docker run -d --rm -e FTP_HOST=172.17.0.2 -e LOG_LEVEL=warn -e HEADLESS=no waf2st