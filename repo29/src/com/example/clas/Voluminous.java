package com.example.clas;

public class Voluminous extends Figures {
    private double volume;
    public Voluminous(String name, int NumCorners, double volume) {
        super(name, NumCorners); this.volume=volume;
    }
    public double getVolume() {
        return volume;
        }
}
