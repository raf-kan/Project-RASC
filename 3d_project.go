package main

import (
	"fmt"
)

type Point3D struct {
	X, Y, Z float64
}

type Point2D struct {
	X, Y float64
}

func perspectiveProjection(point Point3D, focalLength float64) Point2D {
	scale := focalLength / (focalLength + point.Z)
	return Point2D{
		X: point.X * scale,
		Y: point.Y * scale,
	}
}

func main() {
	// Define 3D points
	points3D := []Point3D{
		{1.0, 1.0, 4.0},
		{-1.0, 1.0, 5.0},
		{-1.0, -1.0, 3.0},
		{1.0, -1.0, 6.0},
	}

	// Focal length of the camera
	focalLength := 2.0

	// Project 3D points to 2D
	points2D := make([]Point2D, len(points3D))
	for i, point := range points3D {
		points2D[i] = perspectiveProjection(point, focalLength)
	}

	// Print the projected 2D points
	for i, point := range points2D {
		fmt.Printf("Point %d: (%.2f, %.2f)\n", i+1, point.X, point.Y)
	}
}
