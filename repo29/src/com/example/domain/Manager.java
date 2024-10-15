package com.example.domain;

public class Manager extends Employee {
    public Manager(int empId, String name, String ssn, double salary, String deptName) {
        super(empId, name, ssn, salary);
        this.deptName = deptName;
    }

    private String deptName;

    public String getDeptName() {
        return deptName;
    }

}
