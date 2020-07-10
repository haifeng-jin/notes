# Docker

```
docker run -p 5005:5005 -i -t jhfjhfj1/tamuta2:latest _bin_bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. core.proto
docker build -t tamuta2:latest .
docker build -f Dockerfile_dry_run -t ta2image .
docker run -i --entrypoint _bin_bash tamuta2 -c 'ta2_search $CONFIG_JSON_PATH'
docker build -f Dockerfile_base -t mybase .
docker run -i --entrypoint _bin_bash ta2image d-c '_resources_executable/1.sh $CONFIG_JSON'
docker run  -p 5005:5005 -it --entrypoint _bin_bash jhfjhfj1/tamuta2:latest -c 'ta2_serve $CONFIG_JSON'
```

Create a docker image:
```
docker build -t autokeras:latest .
```

run docker as a shell:
```
docker run -it --entrypoint /bin/bash image_name
```

You save the image as a tar archive, using `docker save -o`:

```
docker save -o archive.tar sheffien/rim
```

Then you load it (on a different computer) with

```
docker load -i archive.tar
```

and now it will show up in your docker images list:

`docker images`

The Docker.

Use `ENV` to set environment variable.
```
docker build -t registry.datadrivendiscovery.org/ta2/texas-anm-university_tamu_1.0.0:latest .
docker login registry.datadrivendiscovery.org
docker push registry.datadrivendiscovery.org/ta2/texas-anm-university_tamu_1.0.0
docker tag tamuta2 jhfjhfj1/tamuta2
docker push jhfjhfj1/tamuta2
docker exec tamuta2 _bin_bash
```

Remove docker images.

```
docker rmi IMAGE_ID
```

Remove all docker images.

```
docker rmi $(docker images -a -q)
```

Remove all docker images with pattern

```
docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi
```
