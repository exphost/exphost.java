def test_java12_exists(host):
    assert host.file("/opt/openjdk-12/bin/java").exists
def test_java15_exists(host):
    assert host.file("/opt/openjdk-15/bin/java").exists
def test_java14_exists(host):
    assert host.file("/opt/openjdk-14/bin/java").exists
