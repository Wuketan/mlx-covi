from importlib.metadata import version

import mlx.core as mx

import mlx_covi


def test_version():
    assert mlx_covi.__version__ == version("mlx-covi")


def test_mlx_available():
    assert mx.array([1, 2, 3]).sum().item() == 6
