import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bacula_client_is_installed(host):
    assert host.package("bacula-client").is_installed


def test_bacula_client_is_running(host):
    host.service("bacula-fd").is_running


def test_bacula_client_is_enabled(host):
    host.service("bacula-fd").is_enabled


def test_bacula_client_listen_port(host):
    host.socket("tcp://0.0.0.0:9102")
