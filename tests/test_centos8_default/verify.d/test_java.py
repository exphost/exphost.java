def test_java_exists(host):
    assert host.file("/opt/openjdk-12/bin/java").exists
