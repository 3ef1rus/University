package com.example;

public class MainExample {
    public static void main(String[] args) {
        Figures square = new Figures();
        square.setNumCorners(4);
        square.setName("square");
        System.out.println("Figure number corners: " + square.getNumCorners());
        System.out.println("Figure Name: " + square.getName());
    }
}
