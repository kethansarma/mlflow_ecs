import boto3
import subprocess

# with open("/tmp/output.log", "a") as output:
cmds = ["docker build --rm=true -t pytask . " ]#, "docker commit 0f67eb2687a0 tcs"]
# ["docker run 0f67eb2687a0",
for cmd in cmds:
    response = subprocess.call(cmd, shell=True)
    print(response)
# response = subprocess.call("docker run --rm wappalyzer/cli https://wappalyzer.com", shell=True, stdout=output, stderr=output)
# client = boto3.client('ecr')
# response = client.put_image(
#     registryId='kethansarma',
#     repositoryName='pytask',
#     imageTag='latest',
#     imageDigest='sha256:5b40aa2430e58fc9b109d733c73c7858c5ab586460706074e1c9d055b1348377',
#     imageManifest='application/vnd.docker.distribution.manifest'
# )
# git clone https://github.com/kethansarma/mlflow_ecs.git && cd mlflw_ecs