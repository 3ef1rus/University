package com.example.clas;

import com.example.interfac.Facade;

public class ActivePeople extends People implements Facade {

    public ActivePeople(String name) {
        super(name);
    }
    public void start(){
        System.out.println("Начать идти");
    }
    public void stop(){
        System.out.println("Остановиться");
    }
}
    

