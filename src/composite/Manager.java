package composite;

import java.util.LinkedList;
import java.util.List;

public class Manager extends Employee
{
    private List<Employee> employees;
    public Manager()
    {
        employees=new LinkedList<>();
    }
    public Manager(String name)
    {
        super(name);
        employees=new LinkedList<>();
    }
    public void addEmployee(Employee employee)
    {
        employees.add(employee);
    }
    public void deleteEmployee(Employee employee)
    {
        employees.remove(employee);
    }
    public List<Employee> getEmployees()
    {
        return new LinkedList<>(employees);
    }
}