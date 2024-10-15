package com.example.domain;

public class Employee {
    public int empId;
    public String name;
    public String ssn;
    public double salary;

    public Employee(int empId, String name, String ssn, double salary) {
        this.empId = empId;
        this.name = name;
        this.ssn = ssn;
        this.salary = salary;
    }

    public void raiseSalary(double increase){ 
        if (increase>0){
        salary += increase;
        }
        }
        

    public int getEmpId() {
        return empId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSsn() {
        return ssn;
    }

    public double getSalary() {
        return salary;
    }

}


