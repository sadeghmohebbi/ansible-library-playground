import ansible_runner

def _tasks(*runs):
    for r in runs:
        print("Status:", r.status)
        print("Return Code:", r.rc)

def update_apt_cache():
    return ansible_runner.run(host_pattern='localhost', module='apt', module_args='update-cache=True')

def install_nginx():
    return ansible_runner.run(host_pattern='localhost', module='apt', module_args='name=nginx state=present')

_tasks(
    update_apt_cache(),
    install_nginx()
)