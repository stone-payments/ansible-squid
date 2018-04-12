import os

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
