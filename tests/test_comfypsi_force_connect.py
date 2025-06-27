#!/usr/bin/env python

"""Tests for the comfypsi_force_connect node."""

import pytest
import torch
from comfy.comfy_types.node_typing import IO
from src.node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, ForceConnect


@pytest.fixture
def node():
    """Fixture to create a comfypsi_force_connect node instance."""
    return ForceConnect()


def test_node_metadata(node):
    assert node.RETURN_TYPES == (IO.ANY,)
    assert node.FUNCTION == "main"
    assert node.CATEGORY == "comfypsi/utility"

    required_inputs = node.INPUT_TYPES()["required"]
    assert "source" in required_inputs
    assert required_inputs["source"][0] == IO.ANY


def test_node_mappings():
    assert "comfypsi_force_connect" in NODE_CLASS_MAPPINGS
    assert NODE_CLASS_MAPPINGS["comfypsi_force_connect"] == ForceConnect

    assert "comfypsi_force_connect" in NODE_DISPLAY_NAME_MAPPINGS
    assert NODE_DISPLAY_NAME_MAPPINGS["comfypsi_force_connect"] == "Force Connect"


@pytest.mark.parametrize(
    "data",
    [
        torch.tensor([1, 2, 3]),
        "hello world",
        123,
        45.67,
        [1, "a", None],
        {"key": "value", "number": 99},
        True,
        None,
    ],
)
def test_main_logic(node, data):
    # Prepare the source data, cloning tensors to ensure immutability.
    source = data.clone() if isinstance(data, torch.Tensor) else data

    result = node.main(source=source)

    assert isinstance(result, tuple)
    assert len(result) == 1
    output = result[0]

    # For PyTorch tensors, we must use torch.equal for comparison.
    if isinstance(data, torch.Tensor):
        assert torch.equal(output, data)
    else:
        assert output == data
