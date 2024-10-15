package com.example.clas;

public class Figures {
    public int NumCorners;
    public String name;

    public Figures(String name, int NumCorners) {
        this.NumCorners = NumCorners;
        this.name = name;
    }

    public int getNumCorners() {
        return NumCorners;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}
