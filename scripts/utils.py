import numpy as np
import math
from sklearn.cluster import DBSCAN

def cluster(data):
    data=np.array(data)
    result=DBSCAN(eps=10,min_samples=1).fit(data)
    counter=np.bincount(result.labels_)
    return counter
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def orientation(x1, y1, x2, y2, angle):
    skew_x = x2 - x1
    skew_y = y2 - y1
    dot = skew_x * 1 + skew_y * 0
    mag1 = math.sqrt(math.pow(skew_x, 2) + math.pow(skew_y, 2))
    mag2 = math.sqrt(math.pow(1, 2) + math.pow(0, 2))
    beta = math.acos(dot / (mag1 * mag2))
    if skew_y < 0:
        if skew_x < 0:
            beta = -beta
        else:
            beta = 0 - beta
    theta = beta - angle
    if theta > np.pi:
        theta = np.pi - theta
        theta = -np.pi - theta
    if theta < -np.pi:
        theta = -np.pi - theta
        theta = np.pi - theta
    return theta

def diagonal_distance(p1, p2):
    d = 0
    coord_diff = [abs(p1[0] - p2[0]), abs(p1[1] - p2[1])]
    dx = coord_diff[0]
    dy = coord_diff[1]
    min_xy = min(dx, dy)
    d = dx + dy + (math.sqrt(2) - 2) * min_xy
    return d

def PolarToCartesian(dist, angle,):
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    return x, y

def bresenham_line(x1, y1, x2, y2):
    """
    Draws a line between (x1, y1) and (x2, y2) using Bresenham's line algorithm.
    Returns a list of points on the line.
    """
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


