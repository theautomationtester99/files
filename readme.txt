docker build -t gui_env -f dockerfile .
docker run -it --rm -p 5901:5901 python_gui_env

afer that connect to vpn using any vnc viewer using pwd "password".
to run browsers after connecting use --no-sandbox

file Dockerfile-usethisforwaf contains package to use python ctx build.