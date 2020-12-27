def test_java_exists(host):
    assert host.file("/opt/openjdk-15/bin/java").exists
def test_java2_exists(host):
    assert host.file("/opt/openjdk-15/bin/java2").exists
