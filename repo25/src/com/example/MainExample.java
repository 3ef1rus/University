package com.example;

import com.example.clas.ActivePeople;
import com.example.clas.Context;
import com.example.clas.People;
import com.example.clas.Bike;

public class MainExample {

    public static void main(String[] args) {
        People boy = new People("vasia");
        People girl = boy.copy();
        girl.setName("anna");
        ActivePeople Woman = new ActivePeople("Tanya");
        Context text = new Context (new Bike());
        System.out.println(boy.name);
        System.out.println(girl.name);
        Woman.start();
        Woman.stop();  
        text.drive();
 
    }
}
