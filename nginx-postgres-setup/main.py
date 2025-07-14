import ansible_runner

def install_nginx():
    r = ansible_runner.run(host_pattern='localhost', module='apt', module_args='update-cache=True')
    print("Status:", r.status)
    print("Return Code:", r.rc)
    return r

install_nginx()