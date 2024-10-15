package com.example.clas;
import com.example.interfac.Copyable;
public class People implements Copyable   {
    public String name;
    public People (String name){
this.name=name;
    }
    public People copy() {
        People people = new People(this.name);
        return people;
    }
    public void setName(String name) {
        this.name = name;
    }
}
