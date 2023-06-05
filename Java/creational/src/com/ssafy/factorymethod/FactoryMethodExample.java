package com.ssafy.factorymethod;
public class FactoryMethodExample {
    
    public FactoryMethodExample() {
        new FactoryMethodClient(new ConcreteCreator());
        new FactoryMethodClient(new AnotherConcreteCreator());
    }
    
    public static void main(String args[]) {
        new FactoryMethodExample();
    }
}
