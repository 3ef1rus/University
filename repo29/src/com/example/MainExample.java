package com.example;

import com.example.clas.Figures;
import com.example.clas.Voluminous;
import com.example.clas.Flat;
import com.example.clas.Spherical;
public class MainExample {

    private static void printFigure(Figures emp) {
        System.out.println("Figure name: " + emp.getName());
        System.out.println("Figure number corners: " + emp.getNumCorners());
        System.out.println(" ");
    }
    public static void main(String[] args) {
        Figures square = new Figures("triugl",4);
        Voluminous cube = new Voluminous("cube",8,10);
        Flat triugle = new Flat("triugle",3,9);
        Spherical oval = new Spherical("oval", 0);
        printFigure(square);
        printFigure(cube);
        printFigure(triugle);
        printFigure(oval);
    }
}
