#!/usr/bin/env python3


def get_coords(wire):
    """Returns list of (x,y) coords where line starts, ends, or bends"""
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
    """Returns list of (x,y) coordinates of intersections of two wires"""
    intersections = []
    for p1 in range(len(coords1) - 1):  # for each wire segment
        for p2 in range(len(coords2) - 1):
            # make a bit more expressive, for easier calculation
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
                ) and (  # and if line1's y-coord is inbetween the two y coords of line2
                    min(line2_start["y"], line2_end["y"])
                    <= line1_start["y"]
                    <= max(line2_start["y"], line2_end["y"])
                ):
                    intersections.append(
                        {  # the intersection is the y-coord of the horizontal line,
                            # and the x-coord of the vertical line
                            "coords": (line2_start["x"], line1_start["y"]),
                            # which segment the intersection is in
                            "segments_wire1": p1,
                            "segments_wire2": p2,
                        }
                    )  # ditto for wire 2
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
                    intersections.append(
                        {
                            "coords": (line1_start["x"], line2_start["y"]),
                            "segments_wire1": p1,
                            "segments_wire2": p2,
                        }
                    )
    return intersections


def manhattan_dist(p, q):
    """Return Manhattan distance between two points (x1,y1) and (x2,y2)"""
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def get_steps(coords, n_segments, intersection):
    """Number of steps on the grid until an intersection is reached"""
    steps = 0
    for i in range(n_segments):  # for all whole segments
        steps += abs(
            sum(map(lambda x, y: x - y, coords[i], coords[i + 1]))
        )  # calculate how far we moved from one coordinate to the next
        # then add the steps from the last coordinate to the intersection
    steps += abs(sum(map(lambda x, y: x - y, coords[n_segments], intersection)))
    return steps


def answer_part1(wire1, wire2):
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = get_intersections(coords1, coords2)
    # minimum manhattan distance for all intersections (disregarding the origin)
    return min(
        [
            manhattan_dist((0, 0), p["coords"])
            for p in intersections
            if p["coords"] != (0, 0)
        ]
    )


def answer_part2(wire1, wire2):
    coords1 = get_coords(wire1)
    coords2 = get_coords(wire2)
    intersections = get_intersections(coords1, coords2)
    # minimum sum of steps to all intersections (disregarding the origin)
    return min(
        [
            get_steps(coords1, p["segments_wire1"], p["coords"])
            + get_steps(coords2, p["segments_wire2"], p["coords"])
            for p in intersections
            if p["coords"] != (0, 0)
        ]
    )


if __name__ == "__main__":
    with open("input_day03") as f:
        wire1 = f.readline().strip().split(",")
        wire2 = f.readline().strip().split(",")
    print("Part 1:", answer_part1(wire1, wire2))
    print("Part 2:", answer_part2(wire1, wire2))
