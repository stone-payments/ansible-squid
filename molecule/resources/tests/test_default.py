import os
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_squid_is_installed(host):
    squid = host.package("squid")
    assert squid.is_installed


def test_squid_running_and_enabled(host):
    squid = host.service("squid")
    assert squid.is_running
    assert squid.is_enabled


def test_squid_syntax(host):
    squid = host.run("/usr/sbin/squid -k parse").rc
    assert squid == 0


def test_squid_process(host):
    squid = host.run("/usr/sbin/squid -k check").rc
    assert squid == 0


def test_squid_custom_files(host):
    custom_whitelist = yaml.load(open(
        "../resources/files/custom_whitelist.yml"))
    for access in custom_whitelist['squid_custom_whitelist']:
        # src
        cmd = host.run("cat /etc/squid/{}_src".format(access['name']))
        assert cmd.rc == 0
        files = cmd.stdout.splitlines()
        assert files == access['src']
        # dest
        cmd = host.run("cat /etc/squid/{}_dstdomain".format(access['name']))
        assert cmd.rc == 0
        files = cmd.stdout.splitlines()
        assert files == access['dest']
