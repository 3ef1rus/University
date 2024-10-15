package com.example.clas;

import com.example.interfac.Strategy;

public class Context implements Strategy{
    private Strategy strategy;
    public Context(Strategy strategy){
        this.strategy=strategy;
    }
public void drive() {
    strategy.drive();
}
}
