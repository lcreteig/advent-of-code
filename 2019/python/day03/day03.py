#!/usr/bin/env python3


def get_coords(wire):
    # Make this a list of dicts!
    """Get all (x,y) coords where line starts, ends, or bends"""
    x, y = [0], [0]
    for idx, point in enumerate(wire):
        dir = point[0]  # which direction to move
        val = int(point[1:])  # how much to move by
        if dir == "R":  # move along x-axis in positive direction
            x.append(x[idx] + val)
            y.append(y[idx])
        elif dir == "L":  # move along x-axis in negative direction
            x.append(x[idx] - val)
            y.append(y[idx])
        elif dir == "U":  # move along y-axis in positive direction
            y.append(y[idx] + val)
            x.append(x[idx])
        elif dir == "D":  # move along y-axis in negative direction
            y.append(y[idx] - val)
            x.append(x[idx])
    return list(zip(x, y))  # list of (x,y) coordinates


def get_intersections(coords1, coords2):
    """Return coordinates of intersections of two wires"""
    intersections = []
    for p1 in range(len(coords1) - 1):
        for p2 in range(len(coords2) - 1):
            line1_start = {"x": coords1[p1][0], "y": coords1[p1][1]}
            line1_end = {"x": coords1[p1 + 1][0], "y": coords1[p1 + 1][1]}
            line2_start = {"x": coords2[p2][0], "y": coords2[p2][1]}
            line2_end = {"x": coords2[p2 + 1][0], "y": coords2[p2 + 1][1]}
            if (line1_start["y"] == line1_end["y"]) and (
                line2_start["x"] == line2_end["x"]
            ):  # if line1 is horizontal, line2 is vertical
                # line2 will intersect line1 if its x_coord is
                # inbetween the two x-coords of line1,
                if (
                    min(line1_start["x"], line1_end["x"])
                    <= line2_start["x"]
                    <= max(line1_start["x"], line1_end["x"])
                ) and (  # and if line1s y-coord is inbetween the two y coords of line2
                    min(line2_start["y"], line2_end["y"])
                    <= line1_start["y"]
                    <= max(line2_start["y"], line2_end["y"])
                ):
                    intersections.append((line1_start["y"], line2_start["x"]))
            else:  # otherwise it's vertical
                # line1 will intersect line2 if its x_coord is
                # inbetween the two x-coords of line2,
                if (
                    min(line2_start["x"], line2_end["x"])
                    <= line1_start["x"]
                    <= max(line2_start["x"], line2_end["x"])
                ) and (  # and line2's y_coord is inbetween the two y-coords of line1
                    min(line1_start["y"], line1_end["y"])
                    <= line2_start["y"]
                    <= max(line1_start["y"], line1_end["y"])
                ):
                    intersections.append((line1_start["x"], line2_start["y"]))
    return intersections


def manhattan_dist(p, q):
    """Calculate Manhattan distance of a coordinate to zero"""
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def answer_part1(wire1, wire2):
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = get_intersections(coords1, coords2)
    return min([manhattan_dist((0, 0), p) for p in intersections if p != (0, 0)])


if __name__ == "__main__":
    with open("input_day03") as f:
        wire1 = f.readline().strip().split(",")
        wire2 = f.readline().strip().split(",")
    # Part 1
    print("Part 1:", answer_part1(wire1, wire2))
