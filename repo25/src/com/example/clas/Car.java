package com.example.clas;

import com.example.interfac.Strategy;

public class Car implements Strategy {
    public void drive(){
        System.out.println("Поехать на машине");
    }
}
