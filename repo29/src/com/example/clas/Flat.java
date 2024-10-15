package com.example.clas;

public class Flat extends Figures {
    private double perimeter;
    public Flat(String name, int NumCorners, double perimeter) {
        super(name, NumCorners); this.perimeter=perimeter;
    }
    public double getPerimeter() {
        return perimeter;
        }
}