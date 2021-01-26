import pytest
from day03 import answer_part1, answer_part2


testdata = [
    (["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"], 6, 30),
    (
        ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
        ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
        159,
        610,
    ),
    (
        ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
        ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
        135,
        410,
    ),
]


@pytest.mark.parametrize("wire1, wire2, distance, _", testdata)
def test_answer_part1(wire1, wire2, distance, _):
    assert answer_part1(wire1, wire2) == distance


@pytest.mark.parametrize("wire1, wire2, _, steps", testdata)
def test_answer_part2(wire1, wire2, _, steps):
    assert answer_part2(wire1, wire2) == steps
