import subprocess


cmd1 = 'docker build -t pytask .'
cmd2 = 'aws ecr-public get-login-password --region us-east-1 | \
        docker login --username AWS --password-stdin public.ecr.aws/k5r5n7p7'
cmd3 = 'docker tag pytask:latest public.ecr.aws/k5r5n7p7/pytask:latest'
cmd4 = 'docker push public.ecr.aws/k5r5n7p7/pytask:latest'

for cmd in [cmd1, cmd2, cmd3, cmd4]:
    response = subprocess.call(cmd, shell=True)
    print(response)