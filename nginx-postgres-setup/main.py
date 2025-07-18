import ansible_runner

def update_apt_cache():
    return ansible_runner.run(host_pattern='localhost', module='apt', module_args='update-cache=True')

def install_nginx():
    return ansible_runner.run(host_pattern='localhost', module='apt', module_args='name=nginx state=present')

def enable_nginx():
    return ansible_runner.run(host_pattern='localhost', module='service', module_args='name=nginx state=started enabled=True')

def install_postgresql():
    return ansible_runner.run(host_pattern='localhost', module='apt', module_args=f"name=postgresql,postgresql-contrib state=present")

def enable_postgresql():
    return ansible_runner.run(host_pattern='localhost', module='service', module_args='name=postgresql@14-main.service state=started enabled=True')

# ----------------------------------
# --- running tasks sequentially ---
# ----------------------------------
def _tasks(*tasks):
    for task in tasks:
        r = task()
        print("Status:", r.status)
        print("Return Code:", r.rc)

_tasks(
    update_apt_cache,
    install_nginx,
    enable_nginx,
    install_postgresql,
    enable_postgresql
)