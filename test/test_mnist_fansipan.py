from mnist_fansipan import mnist_fansipan


def test_fib() -> None:
    assert mnist_fansipan.fib(0) == 0
    assert mnist_fansipan.fib(1) == 1
    assert mnist_fansipan.fib(2) == 1
    assert mnist_fansipan.fib(3) == 2
    assert mnist_fansipan.fib(4) == 3
    assert mnist_fansipan.fib(5) == 5
    assert mnist_fansipan.fib(10) == 55
