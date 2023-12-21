echo "******************************************************"
echo "Starting bup-schema :                                    ";
echo "******************************************************"

#!/bin/bash
app="bup-schema"
docker build -t ${app} .
docker run -d -p 8903:80 \
  --env-file ./docker-gen-ai/local.env \
  --network ailegorretaNet \
  --name=${app} \
  -v $PWD:/app  \
  ${app}
